"""操作MySql相关函数"""
"""
 desc followers;
+---------------+--------------+------+-----+---------+-------+
| Field         | Type         | Null | Key | Default | Extra |
+---------------+--------------+------+-----+---------+-------+
| uid           | varchar(255) | YES  |     | NULL    |       |
| followers_num | int          | YES  |     | NULL    |       |
| time          | timestamp    | YES  |     | NULL    |       |
+---------------+--------------+------+-----+---------+-------+
"""
import pymysql
from datetime import datetime


class Mysql:
    def __init__(self):
        self.db = pymysql.connect(host="localhost",
                                  user="root",
                                  password="white",
                                  database="UpSpider")

    def insert(self, uid, num):
        """向数据库中储存up的粉丝数"""
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        commond = f'insert into followers values ("{uid}",{num},"{time}")'
        cursor = self.db.cursor()
        cursor.execute(commond)
        self.db.commit()


def main():
    mysql = Mysql()
    mysql.insert("2333", 23333)


if __name__ == "__main__":
    print(argv)
    main()
