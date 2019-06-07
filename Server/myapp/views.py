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
            main_rate = [None] * len(recipe_DB) # 주재료 매칭 비율
            sub_rate = [None] * len(recipe_DB)  # 부재료 매칭 비율
            cntnum0 = [[0 for o in range(2)] for p in range(len(recipe_DB))]  # 사용자 재료와 DB 재료의 매치 갯수
            cntnum1 = [[0 for o in range(2)] for p in range(len(recipe_DB))]  # 사용자 재료와 DB 주재료의 매치 갯수
            cntnum2 = [[0 for o in range(2)] for p in range(len(recipe_DB))]  # 사용자 재료와 DB 부재료의 매치 갯수

            # find 함수를 이용해서 몇 개의 재료가 매칭되는지 cntnum에 저장
            for i in range(0, len(recipe_DB)):
                cntnum0[i][1] = recipe_DB[i].mname
                cntnum1[i][1] = recipe_DB[i].mname
                cntnum2[i][1] = recipe_DB[i].mname

                for j in range(0, len(user_ingredient)):
                    comparing0 = recipe_DB[i].ingredient.find(user_ingredient[j])  # 재료 매칭 비교
                    comparing1 = recipe_DB[i].main_ing.find(user_ingredient[j]) # 주재료 매칭 비교
                    comparing2 = recipe_DB[i].sub_ing.find(user_ingredient[j]) # 부재료 매칭 비교
                    if comparing0 >= 0:
                        cntnum0[i][0] += 1  # 재료 매칭시 +1
                    if comparing1 >= 0:
                        cntnum1[i][0] += 1  # 주재료 매칭시 +1
                    if comparing2 >= 0:
                        cntnum2[i][0] += 1  # 부재료 매칭시 +1

                each_ing1 = recipe_DB[i].main_ing.split(' ') # 주재료 갯수
                each_ing2 = recipe_DB[i].sub_ing.split(' ')  # 부재료 갯수
                main_rate[i] = cntnum1[i][0] / len(each_ing1) # 주재료 매칭 비율
                sub_rate[i] = cntnum2[i][0] / len(each_ing2)  # 부재료 매칭 비율


            # maxi의 최신화 (cntnum 중 최대값으로)
            maxi = 0
            for m in range(0, len(recipe_DB)):
                if cntnum0[m][0] > maxi:
                    maxi = cntnum0[m][0]


            # 매칭되는 재료가 하나도 없을 경우
            if maxi == 0:
                return JsonResponse({'error' : '매칭되는 재료가 없습니다.'})
            # 매칭되는 재료가 1개 이상이라도 있을 경우
            else:
                match_reci = [None] * 14
                final_reci = [None] * 14

                cnt = 0 # 최종 매칭 레시피 배열을 넣기 위한 카운트
                bool = True # while문 탈출을 위한 불리언

                while bool:
                    mx = list() # 주재료 비율이 같은 레시피들의 인덱스 저장하는 리스트
                    max_rate = max(main_rate)
                    for i in range(0, len(main_rate)):
                        if max_rate == main_rate[i]:
                            mx.append(i) # 주재료 비율이 같으면 저장


                    # 주재료 비율이 같은 레시피가 있다면
                    if len(mx) > 1:
                        for i in range(0, len(mx) - 1):
                            # 부재료 비율에 따라 오름차순 정렬
                            if sub_rate[mx[i]] >= sub_rate[mx[i + 1]]:
                                temp = mx[i]
                                mx[i] = mx[i + 1]
                                mx[i + 1] = temp

                        # 부재료 비율이 높은 순으로 매칭 레시피에 저장 (14개가 되면 break)
                        for i in range(0, len(mx)):
                            match_reci[cnt] = cntnum1[mx[len(mx)-1-i]][1]
                            cnt += 1
                            if cnt >= 14:
                                bool = False
                                break

                        # 저장 하면 해당 주재료 비율을 -1로 맞추어 더 이상 max 함수에서 걸리지 않도록 수정
                        for i in range(0, len(mx)):
                            main_rate[mx[i]] = -1

                    # 주재료 비율이 같은 레시피가 없다면
                    else:
                        Lindex = main_rate.index(max(main_rate))
                        match_reci[cnt] = cntnum1[Lindex][1]
                        cnt += 1
                        if cnt >= 14:
                            break
                        main_rate[Lindex] = -1


                number = 0
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
