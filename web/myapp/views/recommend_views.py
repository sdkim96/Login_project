from django.shortcuts import render
from myapp.models import Recommend_02new
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import json, openai

openaiKey = ''

@csrf_exempt
def recommend_02(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        labelForlocations = {
            "0": '서도심 및 용산',
            "1": '강동',
            "2": '신림 및 구로금천',
            "3": '건대입구 및 광진',
            "4": '노원',
            "5": '강서 및 양천',
            "6": '청량리 및 월곡중랑',
            "7": '은평 및 DMC',
            "8": '여의도 및 당산영등포',
            "9": '서울대입구 및 사당인근',
            "10": '동도심 및 동대문혜화',
            "11": '신촌홍대 및 공덕인근',
            "12": '성북 및 도봉',
            "13": '송파',
            "14": '강남 및 서초',
        }


        condition1 = Q(competing_hotels_count__lt = data['competitor'])
        condition2 = Q(bus_stops_count__gt = data['bus'])
        condition3 = Q(subway_stations_count__gt = data['subway'])
        condition4 = Q(monthly_total_traffic__gt = data['population'])
        condition5 = Q(tourist_spots_count__gt = data['attraction'])
        condition6 = Q(shopping_malls_count__gt = data['shopping'])

        print(condition1)
        print(condition2)
        print(condition3)
        print(condition4)
        print(condition5)
        print(condition6)

        final_condition =  condition1 & condition2 & condition3 & condition4 & condition5 & condition6
        print(final_condition)

        recommend_02_data = Recommend_02new.objects.filter(final_condition)
        print(recommend_02_data)

        labels = [datas.label for datas in recommend_02_data]
        if labels:  # labels 리스트가 비어있지 않은지 확인
            most_common_label = max(set(labels), key=labels.count)
            most_common_label_location = labelForlocations[str(most_common_label)]
        else:
            most_common_label_location = '수치를 조정하세요.'  # 아니라면 None 혹은 원하는 기본값을 설정

        return JsonResponse({'location': most_common_label_location}, status=200)


    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)



def recommend_03(request):
    if request.method == 'POST':
        data2 = json.loads(request.body)
        print(data2)
        content1 = data2['content1']
        content2 = data2['content2']
    
        openai.api_key = openaiKey
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"{content1}성급 호텔을 {content2}지역에 만들건데, 좋은 이름을 추천해줘",
            temperature=0.5,
            max_tokens=600,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        text = response.choices[0].text.strip()  # Extract the text and remove leading/trailing whitespace
        print(text)
        return JsonResponse({'data2': text})
    return JsonResponse({'error': 'Invalid request'}, status=400)




def recommend(request):
    return render(request, 'recommend.html')
