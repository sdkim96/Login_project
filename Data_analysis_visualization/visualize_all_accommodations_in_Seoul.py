from pyproj import Proj, transform
import pandas as pd
import folium

def tm_to_latlon(x, y):
    # 중부원점TM(EPSG:2097) 좌표계 설정
    proj_tm = Proj(init='epsg:2097')
    # 위경도 좌표계 설정 (WGS84)
    proj_latlon = Proj(init='epsg:4326')

    # 좌표 변환
    lon, lat = transform(proj_tm, proj_latlon, x, y)
    return lat, lon

coords = [
    (199345.4661, 451233.3698),
    (198591.1337, 450740.3532),
    (198037.3385, 451010.5466),
]

for coord in coords:
    lat, lon = tm_to_latlon(coord[0], coord[1])
    print(f"위도: {lat}, 경도: {lon}")


# 좌표 변환 함수 정의
def tm_to_latlon(x, y):
    proj_tm = Proj(init='epsg:2097')
    proj_latlon = Proj(init='epsg:4326')
    lon, lat = transform(proj_tm, proj_latlon, x, y)
    return lat, lon

# CSV 파일을 DataFrame으로 불러오기
df = pd.read_csv('./data/서울시 숙박업 인허가 정보.csv', encoding='cp949')

# 영업중인 숙박시설만 필터링
df = df[df['영업상태명'] == '영업/정상']

# 좌표 정보가 누락된 행 제거
df = df.dropna(subset=['좌표정보(X)', '좌표정보(Y)'])

# 서울시 중심 위경도 (지도 초기 위치 설정)
seoul_center_lat = 37.5642135
seoul_center_lon = 126.9755761

# 지도 생성
map_seoul = folium.Map(location=[seoul_center_lat, seoul_center_lon], zoom_start=12)


# 영업중인 숙박시설의 위치 정보를 지도에 표시
for index, row in df.iterrows():
    x, y = row['좌표정보(X)'], row['좌표정보(Y)']
    lat, lon = tm_to_latlon(x, y)
    folium.Marker([lat, lon], popup=row['사업장명']).add_to(map_seoul)

# 지도 표시
map_seoul.save('map_seoul.html')
