from FollowersSpider import *
from Sql import *
import schedule
import time
from sys import argv

uid = ""
# 初始化数据库
sql = Mysql()


def main():
    """主函数"""

    # 每小时执行任务
    schedule.every(10).seconds.do(update)
    while True:
        schedule.run_pending()
        time.sleep(1)


def update():
    """用于更新up主信息 并且写入数据库的函数"""
    num = get_followers_number(uid)
    sql.insert(uid, num)
    print(f"uid:{uid} followers:{num}")


if __name__ == "__main__":
    # 输入uid
    uid = argv[1]
    print(uid)
    main()
