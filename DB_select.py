# 사용자에게 재료를 받았다고 가정하고 추천 레시피를 뽑아내는 비교 알고리즘
# 사용자가 레시피 중 하나를 선택했다고 가정하고 해당 레시피의 모든 정보를 다시 사용자에게 전달

import pymysql.cursors
import time

start = time.time() # 시간 측정 시작

# 시나리오 1: 사용자 재료 수신, DB와 비교, 추천 레시피 전달
user_ingredient = ["우유", "달걀", "닭", "두부"] # 사용자로 부터 입력 받은 재료 예시

mydb = pymysql.connect(
    host='localhost',
    user='root',
    password='rladudwn01**',
    db='food',
    charset='utf8mb4'
)

try:
    with mydb.cursor() as cursor:
        sql = 'SELECT Recipe_name, Ingredients FROM myapp_food'
        cursor.execute(sql)
        recipe_DB = cursor.fetchall()
        # print(result)

finally:
    mydb.close()

cntnum = [0 for _ in range(1000)] # 사용자 재료와 DB재료의 매치 갯수

for i in range(0, 1000):
    cntnum[i] = 0
    for j in range(0,len(user_ingredient)):
        comparing = recipe_DB[i][1].find(user_ingredient[j])
        # find() 를 통해서 사용자의 재료가 DB 재료에 매칭 되는 지 확인(매칭되면 >=0, 매칭 되지 않으면 -1)
        if comparing >= 0:
            cntnum[i] += 1  # 매칭 되었을 때 갯수 ++

maxi = 0  # 최대 매칭 레시피를 찾기 위한 변수
reci_num = 1  # 결과 레시피 번호

for m in range(0, 1000):  # 최대 매칭 레시피의 매칭 재료 개수 설정(maxi의 최신화)
    if cntnum[m] > maxi:
        maxi = cntnum[m]
        # print(maxi)

print("사용자 재료: %s" % (user_ingredient), "\n")

for m in range(0, 1000):  # maxi에 해당하는 최대 매칭 레시피 모두 출력
    if cntnum[m] == maxi:
        print("추천 레시피%d: %s" % (reci_num, recipe_DB[m][0]))
        reci_num += 1


# 시나리오 2: 사용자가 추천 레시피 중 하나 선택, DB에서 해당 레시피 정보 출력, 선택 레시피 정보 다시 전달
user_choice = ["크림닭"] # 사용자가 닭고기김치찌개를 선택함

mydb = pymysql.connect(
    host='localhost',
    user='root',
    password='rladudwn01**',
    db='food',
    charset='utf8mb4'
)

try:
    with mydb.cursor() as cursor:
        sql = 'SELECT * FROM myapp_food WHERE Recipe_name = %s'
        cursor.execute(sql, user_choice)
        Rec_recipe = cursor.fetchone()

finally:
    mydb.close()

print("\n-----------------------------------------------")
print("\n선택 요리: %s" % Rec_recipe[1])
print("\n필요 재료:\n%s" % Rec_recipe[2])
print("\n조리 방법:\n%s" % Rec_recipe[3].strip())

print("\n소요 시간: %s 초" % (round((time.time() - start), 4))) # 시간 측정 끝