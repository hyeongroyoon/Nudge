import pymysql
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

mydb = pymysql.connect(
  host="localhost",
  user="root",
  passwd="vy107752!!",
  db="food",
  charset='utf8mb4',
)

cursor = mydb.cursor(pymysql.cursors.DictCursor)

sql1 = "select * from Menu where mname = %s"
sql2 = "select D.recipe_menu, D.direction, I.img_dir " \
       "from (select * from direction where recipe_menu = %s as D)"\
       "left outer join (select * from dir_image where recipe_menu = %s as I)" \
       "on D.dirkey = I.imgkey"
sql3 = "select * from Dir_Image where recipe_menu = %s"
cursor.execute(sql1, "세 가지 소스의 파스타")
rows = cursor.fetchall()
for row in rows:
    print(row)

print()
cursor.execute(sql2, ("세 가지 소스의 파스타", "세 가지 소스의 파스타"))
rows = cursor.fetchall()
for row in rows:
    print(row)

print()
cursor.execute(sql3, "세 가지 소스의 파스타")
rows = cursor.fetchall()
for row in rows:
    print(row)


# sql2 = "select A.recipe_menu, A.direction, B.imgkey, B.dir_image " \
#        "from (select * from direction where recipe_menu = %s) as A " \
#        "left outer join (select * from dir_image where recipe_menu = %s) as B" \
#        "on A.dirkey = B.imgkey"
#
# cursor.execute(sql2, ("고등어 찜", "고등어 찜"))
# rows = cursor.fetchall()
# for row in rows:
#     print(row)