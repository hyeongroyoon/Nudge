import pymysql.cursors
import json

with open("C:\\Users\\김영주\\Desktop\\Django RESTful API 2.0\\ex_project\\Etc_tools\\기본.json", "r",
          encoding='UTF8') as json_file1:
    with open("C:\\Users\\김영주\\Desktop\\Django RESTful API 2.0\\ex_project\\Etc_tools\\과정.json", "r",
              encoding='UTF8') as json_file2:
        with open("C:\\Users\\김영주\\Desktop\\Django RESTful API 2.0\\ex_project\\Etc_tools\\재료.json", "r",
                  encoding='UTF8') as json_file3:

            json_data1 = json.load(json_file1)
            json_data2 = json.load(json_file2)
            json_data3 = json.load(json_file3)


            main_info = json_data1["data"]
            dir_info = json_data2["data"]
            ing_info = json_data3["data"]

            # 1.menu 테이블 insert
            m_id = [None] * len(main_info)
            m_name = [None] * len(main_info)
            ingredients = [""] * len(main_info)
            m_main = [""] * len(main_info)
            m_sub = [""] * len(main_info)
            m_season = [""] * len(main_info)
            m_image = [None] * len(main_info)

            number = 0
            for i in range(0, len(main_info)):
                m_id[i] = main_info[i]["RECIPE_ID"]
                m_name[i] = main_info[i]["RECIPE_NM_KO"]
                m_image[i] = main_info[i]["IMG_URL"]

                for j in range(0, len(ing_info)):
                    if m_id[i] == ing_info[j]["RECIPE_ID"]:
                        ingredients[i] += ing_info[j]["IRDNT_NM"] + " "
                        if ing_info[j]["IRDNT_TY_NM"] == "주재료":
                            m_main[i] += ing_info[j]["IRDNT_NM"] + " "
                        elif ing_info[j]["IRDNT_TY_NM"] == "부재료":
                            m_sub[i] += ing_info[j]["IRDNT_NM"] + " "
                        else:
                            m_season[i] += ing_info[j]["IRDNT_NM"] + " "



            mydb = pymysql.connect(
              host="localhost",
              user="root",
              passwd="rladudwn01**",
              db="new_food",
              charset='utf8mb4',
            )

            try:
                with mydb.cursor() as cursor:
                    sql = "INSERT INTO menu (id, mname, ingredient, main_ing, sub_ing, seasoning, dimage) " \
                          "VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    for j in range(0, len(main_info)):
                        val = (m_id[j], m_name[j], ingredients[j], m_main[j], m_sub[j], m_season[j], m_image[j])
                        cursor.execute(sql, val)
                mydb.commit()

            finally:
                mydb.close()


            # 2.direction 테이블 insert
            # mydb = pymysql.connect(
            #     host="localhost",
            #     user="root",
            #     passwd="rladudwn01**",
            #     db="new_food",
            #     charset='utf8mb4',
            # )
            #
            # try:
            #     with mydb.cursor() as cursor:
            #         sql = "INSERT INTO direction (id, recipe_menu, dirkey, direction, dir_image) " \
            #               "VALUES (%s, %s, %s, %s, %s)"
            #         for j in range(0, len(dir_info)):
            #             p_id = dir_info[j]["RECIPE_ID"]
            #             p_key = dir_info[j]["COOKING_NO"]
            #             p_dir = dir_info[j]["COOKING_DC"]
            #             p_image = dir_info[j]["STRE_STEP_IMAGE_URL"]
            #
            #             for k in range(0, len(main_info)):
            #                 if dir_info[j]["RECIPE_ID"] == main_info[k]["RECIPE_ID"]:
            #                     p_name = main_info[k]["RECIPE_NM_KO"]
            #                     break
            #
            #             val = (p_id, p_name, p_key, p_dir, p_image)
            #             cursor.execute(sql, val)
            #     mydb.commit()
            #
            # finally:
            #     mydb.close()


