class Financial():
    def url_join(self,pageindex,pagesize,producttype,status):
        # http://www.yanglee.com/Action/ProductAJAX.ashx?mode=statistics&pageSize=40&pageIndex=1&conditionStr=producttype%3A1%7Cstatus%3A%E5%9C%A8%E5%94%AE&start_released=&end_released=&orderStr=1&ascStr=ulup&_=1583631480607
        url="http://www.yanglee.com/Action/ProductAJAX.ashx?"
        arg={
            'mode':'statistics',
            'pageSize':pagesize,
            'pageIndex':pageindex,
            'conditionStr':"producttype:"+producttype+"|status"+status,
            'start_released':'',
            'end_released':'',
            'orderStr':'1',
            'ascStr':'ulup'
        }

        #参数解析
        new_url=url+urllib.parse.urlencode(arg)
        return new_url

    # 第一次爬取数据
    def data_req(self,nurl):
        ua = UserAgent()
        header = {
            "User-Agent": str(ua.random),
            "Referer": "http://www.yanglee.com/Product/Index.aspx"

        }
        myproxies = {
            "HTTP": "121.227.89.58:8118",
            "HTTP": "110.73.7.167:8123",
            "HTTPS": "218.76.253.201:61408"
            }
        v_resp=requests.get(nurl,proxies=myproxies,headers=header)
        return v_resp.json()
    # 第一层数据解析
    # return:第二层拼接后的地址
    def first_parse(self,url_id):
        id_list=url_id["result"]
        second_url_list=[]
        for i in id_list:
            id=i["ID"]
            url="http://www.yanglee.com/Product/Detail.aspx?id="+id
            second_url_list.append(url)
        return second_url_list

    # 第二层数据的爬取
    def second_req_parse(self,second_url_list):
        ua = UserAgent()
        header = {
            "User-Agent": str(ua.random),
            "Referer": "http://www.yanglee.com/Product/Index.aspx"

        }
        myproxies = {
            "HTTP": "121.227.89.58:8118",
            "HTTP": "110.73.7.167:8123",
            "HTTPS":"218.76.253.201:61408"
        }
        csv_content1 = []
        # csv_content.append()
        for i in second_url_list:
            v_resp=requests.get(i,proxies=myproxies,headers=header)
            v_content=v_resp.text
            bs=BeautifulSoup(v_content,"lxml")
            content=bs.select("#procon1 > table")
            second_content=content[0]
            r_name = re.findall("<td>(.*)</td>", str(second_content))
            r_content = re.findall(
                r'(<td class="pro-textcolor" colspan="3"><p>|<td class="pro-textcolor" colspan="3">|<td class="pro-textcolor">)([\s\S]*?)(</p></td>|<i class="a-icon"></i></td>|</td>)',
                str(second_content))
            r_content1 = []
            for i in r_content:
                r_content1.append(i[1])
            print(r_name)
            print(r_content1)
            num=0
            csv_content = ""
            csv_content=csv_content+r_content1[0]+","+r_content1[1]+","+r_content1[2]+","+r_content1[4][:-2]+","+r_content1[8][1:-2]
            csv_content1.append(csv_content.split(","))
        return csv_content1


import requests
import re
import urllib.parse
from fake_useragent import UserAgent
import json
import time
from  bs4 import BeautifulSoup
from  urllib import request