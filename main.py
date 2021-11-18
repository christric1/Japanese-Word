import pymysql


if __name__ == '__main__':

    # 資料庫參數設定
    db_settings = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",
        "password": "akb033658",
        "db": "japanese_words",
        "charset": "utf8"
    }

    try:
        # 建立Connection物件
        conn = pymysql.connect(**db_settings)

        with conn.cursor() as cursor:
            # 新增資料SQL語法
            command = "INSERT INTO words(id, word, chinese)VALUES(%s, %s, %s)"

            cursor.execute(command, ("1", "わたし", "我"))

            # 儲存變更
            conn.commit()

    except Exception as ex:
        print(ex)
