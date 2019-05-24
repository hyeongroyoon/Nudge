import pymysql.cursors
import urllib
import json
import pandas as pd
from . import api_parsing
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

mydb = pymysql.connect(
  host="localhost",
  user="root",
  passwd="vy107752!!",
  db="food",
  charset='utf8mb4',
)

try:
    with mydb.cursor() as cursor:
        sql1 = "INSERT INTO MENU (mname, ingredient, dimage) " \
              "VALUES (%s, %s, %s)"
        sql2 = "INSERT INTO menu_info (recipe_menu, how_make, sort, calorie, carbohydrate, protein, fat, salt) " \
               "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        sql3 =  "INSERT INTO DIRECTION (recipe_menu, dirkey, direction)" \
                "VALUES (%s, %s, %s)"
        sql4 = "INSERT INTO DIR_IMAGE (recipe_menu, imgkey, dir_image)" \
               "VALUES (%s, %s, %s)"

        for j in range(0, num):
            val1 = (FoodIDDF.ix[j, "RCP_NM"], FoodIDDF.ix[j, "RCP_PARTS_DTLS"], FoodIDDF.ix[j, "ATT_FILE_NO_MK"])
            val2 = (FoodIDDF.ix[j, "RCP_NM"], FoodIDDF.ix[j, "RCP_WAY2"], FoodIDDF.ix[j, "RCP_PAT2"],
                    FoodIDDF.ix[j, "INFO_ENG"],FoodIDDF.ix[j, "INFO_CAR"],FoodIDDF.ix[j, "INFO_PRO"],
                    FoodIDDF.ix[j, "INFO_FAT"],FoodIDDF.ix[j, "INFO_NA"])

            cursor.execute(sql1, val1)
            cursor.execute(sql2, val2)

        for i in range(len(dirkey)):
            for j in range(len(dirkey[i])):
                val3 = (FoodIDDF.ix[i, "RCP_NM"], dirkey[i][j], DIR[i][j])
                cursor.execute(sql3, val3)
            for j in range(len(imgkey[i])):
                val4 = (FoodIDDF.ix[i, "RCP_NM"], imgkey[i][j], DIMG[i][j])
                cursor.execute(sql4, val4)
    mydb.commit()
finally:
    mydb.close()