import pandas as pd
import chardet
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import seaborn as sns
import folium

buspathraw = '../data/서울시 버스 정류소별 위치데이터.xlsx'
busraw = '../data/2022 서울시 버스 정류소별 수송데이터.csv'

# detect file encoding
with open(busraw, 'rb') as f:
    result = chardet.detect(f.read())
encoding = result['encoding']

# read CSV file
bus = pd.read_csv(busraw, encoding=encoding)

# read Excel file
buspath = pd.read_excel(buspathraw)

font_path = '/usr/share/fonts/truetype/humor-sans/Humor-Sans.ttf'
fontprop = fm.FontProperties(fname=font_path, size=12)

bus_columns = [col for col in bus.columns if '승차총승객수' in col or '하차총승객수' in col]
bus_total = bus[['표준버스정류장ID'] + bus_columns]
# 승하차 승객수 합계 계산
bus_total['총승객수'] = bus_total[bus_columns].sum(axis=1)

# 정류장별 총 승객수 합계
station_total = bus_total.groupby('표준버스정류장ID')['총승객수'].sum().reset_index()

# 데이터프레임 병합
merged_df = pd.merge(station_total, buspath, left_on='표준버스정류장ID', right_on='NODE_ID')

# 상위 10개 정류장 추출
top_10 = merged_df.nlargest(10, '총승객수')
all = merged_df.sort_values(by=['총승객수'], ascending=True)

# 시각화
plt.figure(figsize=(14, 6))
sns.barplot(x='정류소명', y='총승객수', data=top_10)
plt.title('서울시 버스 정류장 별 승객 수 Top 10', fontproperties=fontprop)
plt.ylabel('승객 수', fontproperties=fontprop)
plt.xlabel('정류소명', fontproperties=fontprop)
plt.xticks(rotation=45, fontproperties=fontprop)
plt.yticks(fontproperties=fontprop)
plt.show()

# 서울시 중심 좌표
center = [37.5665, 126.9780]

# 지도 객체 생성
map_seoul = folium.Map(location=center, zoom_start=12)

# Top 10 정류장에 마커 추가
for idx, row in top_10.iterrows():
    folium.Marker(
        location=[row['Y좌표'], row['X좌표']],
        popup=row['정류소명'],
        tooltip=f"{row['정류소명']} (총 승객 수: {row['총승객수']})",
        icon=folium.Icon(color='red')
    ).add_to(map_seoul)

# 지도 표시
map_seoul