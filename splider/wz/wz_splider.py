import requests
import json
def photo_req(h_name):
    v_resp=requests.get("https://pvp.qq.com/web201605/js/herolist.json")
    v_json=json.loads(v_resp.text)
    for i in v_json:
        if i["cname"]==h_name:
            list=[]
            n=i["skin_name"].count("|")+1
            for j in range(n):
                j=j+1
                v_img=requests.get("http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/"+str(i["ename"])+"/"+str(i["ename"])+"-bigskin-"+str(j)+".jpg")
                with open("static/images/wz/" + str(i["cname"])+str(j)+ ".jpg", "wb") as f1:
                    f1.write(v_img.content)
                list.append("/static/images/wz/" + str(i["cname"])+str(j)+ ".jpg")
            return list