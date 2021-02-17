"""爬虫相关函数"""
import json
import requests


def get_followers_number(uid):
    """用于获得up主粉丝数的函数"""
    uid = uid
    url = f"https://api.bilibili.com/x/relation/followers?vmid={uid}&pn=1&ps=1&order=desc&jsonp=jsonp"
    headers = {
        "User-Agent": r"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      r"Chrome/88.0.4324.150 Safari/537.36A",
        "referer": r"https://space.bilibili.com/"}
    res = requests.get(url, headers)
    data = json.loads(res.text)
    followers_num = data["data"]["total"]
    return followers_num


def main():
    # soup = bs4.BeautifulSoup(res, "html.parser")
    # fansnum = soup.find("<a>", class_="n-data n-fs")
    followers_num = get_followers_number("777536")
    print(followers_num)


if __name__ == "__main__":
    main()
