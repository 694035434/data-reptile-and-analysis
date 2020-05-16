import re
import  urllib.parse
from fake_useragent import UserAgent
import json
import time
from  bs4 import  BeautifulSoup
from  urllib import request
import requests
def data_req(type,tag,page_limit):
    ua = UserAgent()
    header = {
        "User-Agent": str(ua.random)
    }
    myproxies = {
        "HTTP": "121.227.89.58:8118",
        "HTTP": "110.73.7.167:8123",
        "HTTPS": "218.76.253.201:61408"
        }
    v_resp=requests.get("https://movie.douban.com/j/search_subjects?type="+type+"&tag="+tag+"&page_limit="+page_limit+"&page_start=0",proxies=myproxies,headers=header)
    list = []
    for i in v_resp.json()["subjects"]:
        list1=[]
        list1.append(i["title"])
        list1.append(i["rate"])
        list1.append("/static/images/movie/"+i["title"]+".jpg")
        list.append(list1)
        v_cover = requests.get(i["cover"]).content
        # print(v_cover)
        with open("static/images/movie/"+i["title"]+".jpg","wb") as f1:
            f1.write(v_cover)
    return list
# data_req("tv","热门","5")