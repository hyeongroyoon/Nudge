# 비교알고리즘

import urllib
import json
import pandas as pd
import time

FoodIdListURL = "http://openapi.foodsafetykorea.go.kr/api/6d82f3c09e2f4568b124/COOKRCP01/json/1/1000"  # json 파일

FoodIdPage = urllib.request.urlopen(FoodIdListURL)
FoodIdData = json.loads(FoodIdPage.read())
FoodIdData

FoodIDDF = pd.DataFrame()
FoodIDDF = FoodIDDF.append(
    { "RCP_NM":"", "RCP_PARTS_DTLS":"", "MANUAL01":"", "MANUAL02":"", "MANUAL03":"", "MANUAL04":"" },
    ignore_index = True)
FoodIDDF

num = len((FoodIdData["COOKRCP01"]["row"]))  # json 파일 길이


for i in range(0, num): # json 파일을 python 리스트에 파싱
    FoodIDDF.ix[i,"RCP_NM"] = FoodIdData["COOKRCP01"]["row"][i]["RCP_NM"]
    FoodIDDF.ix[i, "RCP_PARTS_DTLS"] = FoodIdData["COOKRCP01"]["row"][i]["RCP_PARTS_DTLS"]
    # FoodIDDF.ix[i, "MANUAL01"] = FoodIdData["COOKRCP01"]["row"][i]["MANUAL01"]
    # FoodIDDF.ix[i, "MANUAL02"] = FoodIdData["COOKRCP01"]["row"][i]["MANUAL02"]
    # FoodIDDF.ix[i, "MANUAL03"] = FoodIdData["COOKRCP01"]["row"][i]["MANUAL03"]
    # FoodIDDF.ix[i, "MANUAL04"] = FoodIdData["COOKRCP01"]["row"][i]["MANUAL04"]
    # print(FoodIDDF.ix[i, "RCP_NM"])
    # print(FoodIDDF.ix[i, "RCP_PARTS_DTLS"])

start = time.time()

user_ingredient = ["우유", "달걀", "닭", "두부"] # 사용자로 부터 입력 받은 재료 예시
cntnum = [0 for _ in range(num)] # 사용자 재료와 DB재료의 매치 갯수

for m in range(0, num):
    cntnum[m] = 0
    for n in range(0,len(user_ingredient)):
        comparing = FoodIDDF.ix[m, "RCP_PARTS_DTLS"].find(user_ingredient[n])
        # find() 를 통해서 사용자의 재료가 DB 재료에 매칭 되는 지 확인(매칭되면 >=0, 매칭 되지 않으면 -1)
        if comparing >= 0:
            cntnum[m] += 1  # 매칭 되었을 때 갯수 ++

maxi = 0  # 최대 매칭 레시피를 찾기 위한 변수
reci_num = 1  # 결과 레시피 번호

for m in range(0, num):  # 최대 매칭 레시피의 매칭 재료 개수 설정(maxi의 최신화)
    if cntnum[m] > maxi:
        maxi = cntnum[m]
        # print(maxi)

print("사용자 재료: %s" % (user_ingredient), "\n")

for m in range(0, num):  # maxi에 해당하는 최대 매칭 레시피 모두 출력
    if cntnum[m] == maxi:
        print("추천 레시피%d: %s" % (reci_num, FoodIDDF.ix[m, "RCP_NM"]))
        # print("\n<레시피 재료>")
        # print(FoodIDDF.ix[m, "RCP_PARTS_DTLS"])
        reci_num += 1

print("\n소요 시간: %s 초" % (round((time.time() - start), 4)))


