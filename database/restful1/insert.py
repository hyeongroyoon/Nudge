from mysql.connector import MySQLConnection, Error
from configparser import ConfigParser
import mysql.connector
from mysql.connector import Error
from python_mysql_dbconfig import read_db_config


def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='python_mysql',
                                       user='root',
                                       password='secret')
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        conn.close()


if __name__ == '__main__':
    connect()


def read_db_config(filename='config.ini', section='mysql'):
    """ Read database configuration file and return a dictionary object
    :param filename: name of the configuration file
    :param section: section of database configuration
    :return: a dictionary of database parameters
    """
    # create parser and read ini configuration file
    parser = ConfigParser()
    parser.read(filename)

    # get section, default to mysql
    db = {}
    if parser.has_section(section):
        items = parser.items(section)
        for item in items:
            db[item[0]] = item[1]
    else:
        raise Exception('{0} not found in the {1} file'.format(section, filename))

    return db


def insert_book(title, isbn):
    query = "INSERT INTO books(title,isbn) " \
            "VALUES(%s,%s)"
    args = (title, isbn)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()


def main():

    import urllib
    import json
    import pandas as pd


    FoodIdListURL = "http://openapi.foodsafetykorea.go.kr/api/6d82f3c09e2f4568b124/COOKRCP01/json/1/5"

    FoodIdPage = urllib.request.urlopen(FoodIdListURL)
    FoodIdData = json.loads(FoodIdPage.read())
    FoodIdData

    FoodIDDF = pd.DataFrame()
    FoodIDDF = FoodIDDF.append(
        {"RCP_NM": "", "RCP_PARTS_DTLS": "", "MANUAL01": "", "MANUAL02": "", "MANUAL03": "", "MANUAL04": ""
         },
        ignore_index=True)
    FoodIDDF

    num = len((FoodIdData["COOKRCP01"]["row"]))
    print(num)
    for i in range(0, num):
        FoodIDDF.ix[i, "RCP_NM"] = FoodIdData["COOKRCP01"]["row"][i]["RCP_NM"]
        FoodIDDF.ix[i, "RCP_PARTS_DTLS"] = FoodIdData["COOKRCP01"]["row"][i]["RCP_PARTS_DTLS"]
        FoodIDDF.ix[i, "MANUAL01"] = FoodIdData["COOKRCP01"]["row"][i]["MANUAL01"]
        FoodIDDF.ix[i, "MANUAL02"] = FoodIdData["COOKRCP01"]["row"][i]["MANUAL02"]
        FoodIDDF.ix[i, "MANUAL03"] = FoodIdData["COOKRCP01"]["row"][i]["MANUAL03"]
        FoodIDDF.ix[i, "MANUAL04"] = FoodIdData["COOKRCP01"]["row"][i]["MANUAL04"]
        print(FoodIDDF.ix[i, "RCP_NM"])
        print(FoodIDDF.ix[i, "RCP_PARTS_DTLS"])
        print(FoodIDDF.ix[i, "MANUAL01"])
        print(FoodIDDF.ix[i, "MANUAL02"])
        print(FoodIDDF.ix[i, "MANUAL03"])
        print(FoodIDDF.ix[i, "MANUAL04"])
        print("\n")

        insert_book('A Sudden Light', '9781439187036')

if __name__ == '__main__':
    main()