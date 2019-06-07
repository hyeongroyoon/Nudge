from myapp.serializers import Recipe, Choice
from myapp.models import Menu, Direction
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse


# 앱 메인화면에 랜덤하게 오늘의 레시피 출력
class Today_recipes(viewsets.ModelViewSet):

    # 무작위로 정렬하여 10개 출력
    queryset = Menu.objects.order_by("?")[:10]
    serializer_class = Recipe


# 인식한 재료를 바탕으로 여러 레시피 후보를 추천
class Recommend_recipes(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Menu.objects.all()
        serializer = Recipe(queryset, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            user_ingredient = list(request.data.values())
            recipe_DB = Menu.objects.all()
            match_rate = [None] * len(recipe_DB) # 매칭 비율
            cntnum = [[0 for o in range(2)] for p in range(len(recipe_DB))]  # 사용자 재료와 DB재료의 매치 갯수

            # find 함수를 이용해서 몇 개의 재료가 매칭되는지 cntnum에 저장
            for i in range(0, len(recipe_DB)):
                cntnum[i][1] = recipe_DB[i].mname

                for j in range(0, len(user_ingredient)):
                    comparing = recipe_DB[i].main_ing.find(user_ingredient[j])
                    if comparing >= 0:
                        cntnum[i][0] += 1  # 주재료 매칭 되었을 때 가중치 +1

                each_ing = recipe_DB[i].main_ing.split(' ') # 쉼표 기준으로 구분하여 재료 갯수 파악
                match_rate[i] = cntnum[i][0] / len(each_ing) # 주재료 매칭 비율 파악


            # maxi의 최신화 (cntnum 중 최대값으로)
            maxi = 0
            for m in range(0, len(recipe_DB)):
                if cntnum[m][0] > maxi:
                    maxi = cntnum[m][0]


            # 매칭되는 재료가 하나도 없을 경우
            if maxi == 0:
                return JsonResponse({'error' : '매칭되는 재료가 없습니다.'})
            # 매칭되는 재료가 1개 이상이라도 있을 경우
            else:
                match_reci = [None] * 14
                final_reci = [None] * 14
                number = 0

                # 매칭 비율이 높은 순서대로 별도의 리스트에 저장
                for m in range(0,len(match_reci)):
                    Lindex = match_rate.index(max(match_rate))
                    match_reci[m] = cntnum[Lindex][1]
                    match_rate[Lindex] = -1
                    if max(match_rate) == 0: # 더 이상 매칭되는 레시피가 없을 때 break
                        break;

                # 레시피 이름에 재료명이 포함되어 있으면 우선순위로 가져옴
                for m in range(0, len(user_ingredient)):
                    for n in range(0, len(match_reci)):
                        if match_reci[n] is not None and match_reci[n].find(user_ingredient[m]) >= 0:
                            final_reci[number] = match_reci[n]
                            number += 1
                            match_reci[n] = ''

                # 정렬된 레시피를 final_reci 리스트로 최종 저장
                for m in range(0, len(match_reci)):
                    if match_reci[m] != '':
                        final_reci[number] = match_reci[m]
                        number += 1


                firstrecipe = final_reci[0]

                queryset = list(Menu.objects.filter(mname=firstrecipe))

                number = 1

                # 최대 14개까지 레시피 출력. queryset에 저장
                while number < 14:
                    nextrecipe = final_reci[number]
                    queryset += list(Menu.objects.filter(mname=nextrecipe))
                    number += 1

                serializer = Recipe(queryset, many=True)
                return Response(serializer.data)



# 사용자가 최종 선택한 레시피 반환
class Choice_recipe(APIView):

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            choice = list(request.data.values())

            # filter함수를 통해 해당 쿼리셋만 받아옴
            queryset = Direction.objects.filter(recipe_menu=choice[0])

            # 선택 레시피의 조회수 +1
            Cntplus = Menu.objects.get(mname=choice[0])
            Cntplus.count += 1
            Cntplus.save()

            serializer = Choice(queryset, many=True)
            return Response(serializer.data)