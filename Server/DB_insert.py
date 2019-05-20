# 식품안전나라 Open API의 Json 파일을 파이썬 리스트에 파싱한다.
# DB에 insert로 recipe name와 ingredient는 그대로 넣고, direction은 string을 모두 합쳐서 넣는다.

import pymysql.cursors
import urllib
import json
import pandas as pd

# 식품안전나라 open API
FoodIdListURL = "http://openapi.foodsafetykorea.go.kr/api/6d82f3c09e2f4568b124/COOKRCP01/json/1/1000"

FoodIdPage = urllib.request.urlopen(FoodIdListURL)
FoodIdData = json.loads(FoodIdPage.read())
FoodIdData

FoodIDDF = pd.DataFrame()
FoodIDDF = FoodIDDF.append(
    {   "RCP_NM":"", "RCP_PARTS_DTLS":"", "MANUAL01":"", "MANUAL02":"", "MANUAL03":"", "MANUAL04":"", "MANUAL05":"",
        "MANUAL06":"", "MANUAL07":"", "MANUAL08":"", "MANUAL09":"", "MANUAL10":"", "MANUAL11":"", "MANUAL12":"",
        "MANUAL13":"", "MANUAL14":"", "MANUAL15":"", "MANUAL16":"", "MANUAL17":"", "MANUAL18":"", "MANUAL19":"",
        "MANUAL20":""
    },
    ignore_index = True)
FoodIDDF

# json 데이터의 row 개수
num = len((FoodIdData["COOKRCP01"]["row"]))

mydict = {}
direction = ''

# json 데이터를 파이썬 list로 옮기기
for i in range(0,num):
    FoodIDDF.ix[i,"RCP_NM"] = FoodIdData["COOKRCP01"]["row"][i]["RCP_NM"]
    FoodIDDF.ix[i, "RCP_PARTS_DTLS"] = FoodIdData["COOKRCP01"]["row"][i]["RCP_PARTS_DTLS"]
    FoodIDDF.ix[i, "MANUAL01"] = FoodIdData["COOKRCP01"]["row"][i]["MANUAL01"]
    FoodIDDF.ix[i, "MANUAL02"] = FoodIdData["COOKRCP01"]["row"][i]["MANUAL02"]
    FoodIDDF.ix[i, "MANUAL03"] = FoodIdData["COOKRCP01"]["row"][i]["MANUAL03"]
    FoodIDDF.ix[i, "MANUAL04"] = FoodIdData["COOKRCP01"]["row"][i]["MANUAL04"]
    FoodIDDF.ix[i, "MANUAL05"] = FoodIdData["COOKRCP01"]["row"][i]["MANUAL05"]
    FoodIDDF.ix[i, "MANUAL06"] = FoodIdData["COOKRCP01"]["row"][i]["MANUAL06"]
    FoodIDDF.ix[i, "MANUAL07"] = FoodIdData["COOKRCP01"]["row"][i]["MANUAL07"]
    FoodIDDF.ix[i, "MANUAL08"] = FoodIdData["COOKRCP01"]["row"][i]["MANUAL08"]
    FoodIDDF.ix[i, "MANUAL09"] = FoodIdData["COOKRCP01"]["row"][i]["MANUAL09"]
    FoodIDDF.ix[i, "MANUAL10"] = FoodIdData["COOKRCP01"]["row"][i]["MANUAL10"]
    FoodIDDF.ix[i, "MANUAL11"] = FoodIdData["COOKRCP01"]["row"][i]["MANUAL11"]
    FoodIDDF.ix[i, "MANUAL12"] = FoodIdData["COOKRCP01"]["row"][i]["MANUAL12"]
    FoodIDDF.ix[i, "MANUAL13"] = FoodIdData["COOKRCP01"]["row"][i]["MANUAL13"]
    FoodIDDF.ix[i, "MANUAL14"] = FoodIdData["COOKRCP01"]["row"][i]["MANUAL14"]
    FoodIDDF.ix[i, "MANUAL15"] = FoodIdData["COOKRCP01"]["row"][i]["MANUAL15"]
    FoodIDDF.ix[i, "MANUAL16"] = FoodIdData["COOKRCP01"]["row"][i]["MANUAL16"]
    FoodIDDF.ix[i, "MANUAL17"] = FoodIdData["COOKRCP01"]["row"][i]["MANUAL17"]
    FoodIDDF.ix[i, "MANUAL18"] = FoodIdData["COOKRCP01"]["row"][i]["MANUAL18"]
    FoodIDDF.ix[i, "MANUAL19"] = FoodIdData["COOKRCP01"]["row"][i]["MANUAL19"]
    FoodIDDF.ix[i, "MANUAL20"] = FoodIdData["COOKRCP01"]["row"][i]["MANUAL20"]

    # 조리 방법을 하나의 문자열로 합치기
    direction += FoodIDDF.ix[i, "MANUAL01"] + "\n"
    direction += FoodIDDF.ix[i, "MANUAL02"] + "\n"
    direction += FoodIDDF.ix[i, "MANUAL03"] + "\n"
    direction += FoodIDDF.ix[i, "MANUAL04"] + "\n"
    direction += FoodIDDF.ix[i, "MANUAL05"] + "\n"
    direction += FoodIDDF.ix[i, "MANUAL06"] + "\n"
    direction += FoodIDDF.ix[i, "MANUAL07"] + "\n"
    direction += FoodIDDF.ix[i, "MANUAL08"] + "\n"
    direction += FoodIDDF.ix[i, "MANUAL09"] + "\n"
    direction += FoodIDDF.ix[i, "MANUAL10"] + "\n"
    direction += FoodIDDF.ix[i, "MANUAL11"] + "\n"
    direction += FoodIDDF.ix[i, "MANUAL12"] + "\n"
    direction += FoodIDDF.ix[i, "MANUAL13"] + "\n"
    direction += FoodIDDF.ix[i, "MANUAL14"] + "\n"
    direction += FoodIDDF.ix[i, "MANUAL15"] + "\n"
    direction += FoodIDDF.ix[i, "MANUAL16"] + "\n"
    direction += FoodIDDF.ix[i, "MANUAL17"] + "\n"
    direction += FoodIDDF.ix[i, "MANUAL18"] + "\n"
    direction += FoodIDDF.ix[i, "MANUAL19"] + "\n"
    direction += FoodIDDF.ix[i, "MANUAL20"]

    mydict[i] = direction
    direction = ''

# for i in mydict:
#     print(mydict[i])
#     print("\n")


# 여기서부터 DB에 넣는 과정
mydb = pymysql.connect(
  host="localhost",
  user="root",
  passwd="rladudwn01**",
  db="food",
  charset='utf8mb4',
)

try:
    with mydb.cursor() as cursor:
        sql = "INSERT INTO myapp_food (Recipe_name, Ingredients, Direction) " \
              "VALUES (%s, %s, %s)"
        for j in range(0, num):
            val = (FoodIDDF.ix[j, "RCP_NM"], FoodIDDF.ix[j, "RCP_PARTS_DTLS"], mydict[j])
            cursor.execute(sql, val)
    mydb.commit()

finally:
    mydb.close()