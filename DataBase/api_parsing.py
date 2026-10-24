import pymysql.cursors
import urllib
import json
import pandas as pd
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

FoodIdListURL = "http://openapi.foodsafetykorea.go.kr/api/6d82f3c09e2f4568b124/" \
                "COOKRCP01/json/1/1001"

FoodIdPage = urllib.request.urlopen(FoodIdListURL)
FoodIdData = json.loads(FoodIdPage.read())

FoodIDDF = pd.DataFrame()
FoodIDDF = FoodIDDF.append({"RCP_NM":"", "RCP_PARTS_DTLS":"", "MANUAL01":"", "MANUAL02":"",
                            "MANUAL03":"", "MANUAL04":""},ignore_index = True)

num = len((FoodIdData["COOKRCP01"]["row"]))

direction = []
dimage = []

for i in range(0,num):
    FoodIDDF.ix[i,"RCP_NM"] = FoodIdData["COOKRCP01"]["row"][i]["RCP_NM"]
    FoodIDDF.ix[i, "ATT_FILE_NO_MK"] = FoodIdData["COOKRCP01"]["row"][i]["ATT_FILE_NO_MK"]
    FoodIDDF.ix[i, "RCP_WAY2"] = FoodIdData["COOKRCP01"]["row"][i]["RCP_WAY2"]
    FoodIDDF.ix[i, "RCP_PAT2"] = FoodIdData["COOKRCP01"]["row"][i]["RCP_PAT2"]
    FoodIDDF.ix[i, "INFO_ENG"] = FoodIdData["COOKRCP01"]["row"][i]["INFO_ENG"]
    FoodIDDF.ix[i, "INFO_CAR"] = FoodIdData["COOKRCP01"]["row"][i]["INFO_CAR"]
    FoodIDDF.ix[i, "INFO_PRO"] = FoodIdData["COOKRCP01"]["row"][i]["INFO_PRO"]
    FoodIDDF.ix[i, "INFO_FAT"] = FoodIdData["COOKRCP01"]["row"][i]["INFO_FAT"]
    FoodIDDF.ix[i, "INFO_NA"] = FoodIdData["COOKRCP01"]["row"][i]["INFO_NA"]
    FoodIDDF.ix[i, "RCP_PARTS_DTLS"] = FoodIdData["COOKRCP01"]["row"][i]["RCP_PARTS_DTLS"]

    dimage.append([])
    direction.append([])
    cnt = 0
    for j in range(20):
        cnt += 1
        FoodIDDF.ix[i, "MANUAL"+str(j+1).rjust(2, '0')] = \
        FoodIdData["COOKRCP01"]["row"][i]["MANUAL"+str(j+1).rjust(2, '0')]
        if FoodIDDF.ix[i, "MANUAL"+str(j+1).rjust(2, '0')] != '':
            if FoodIDDF.ix[i, "MANUAL"+str(j+1).rjust(2, '0')][-1] != '.':
                FoodIDDF.ix[i, "MANUAL"+str(j+1).rjust(2, '0')] = \
                FoodIDDF.ix[i, "MANUAL"+str(j+1).rjust(2, '0')][:-1]

            dir = FoodIDDF.ix[i, "MANUAL"+str(j+1).rjust(2, '0')]
            direction[i].append(dir)
            direction[i].append(cnt)

        FoodIDDF.ix[i, "MANUAL_IMG"+str(j+1).rjust(2, '0')] = \
        FoodIdData["COOKRCP01"]["row"][i]["MANUAL_IMG" + str(j+1).rjust(2, '0')]
        if FoodIDDF.ix[i, "MANUAL_IMG" + str(j + 1).rjust(2, '0')] != '':
            img = FoodIDDF.ix[i, "MANUAL_IMG" + str(j + 1).rjust(2, '0')]
            dimage[i].append(img)
            dimage[i].append(cnt)

dirkey = []
DIR = []
imgkey = []
DIMG = []
for i in range(num):
    dirkey.append([])
    DIR.append([])
    imgkey.append([])
    DIMG.append([])
    for j in range(len(direction[i])):
        if j % 2 == 1:
            dirkey[i].append(direction[i][j])
        else:
            DIR[i].append(direction[i][j])

    for j in range(len(dimage[i])):
        if j % 2 == 1:
            imgkey[i].append(dimage[i][j])
        else:
            DIMG[i].append(dimage[i][j])