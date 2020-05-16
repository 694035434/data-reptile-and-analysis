import requests
import re
def video_req(reqType,categoryId,start):
    # categoryId  菜单栏类别

    url="https://www.pearvideo.com/category_loading.jsp?reqType="+reqType+"&categoryId="+categoryId+"&start="+start
    v_resp=requests.get(url).text
    url=re.findall('<a href="(.*?)" class="vervideo-lilink actplay"',v_resp)
    v_title=re.findall('vervideo-title">(.*?)</div>',v_resp)
    # print(v_title)
    # print(url)
    re_list01=[]
    num=0
    for i in url:
        video_page_url="https://www.pearvideo.com/"+i
        v_resp=requests.get(video_page_url).text
        video_url=re.findall('srcUrl="(.*?)",vdoUrl=srcUrl',v_resp)
        print(video_url)
        id=video_url[0][54:61]
        videourl="static/livideo/"+id+".mp4"
        video=requests.get(video_url[0]).content
        # print(video)
        if video_url[0].endswith("mp4"):
            with open(videourl,"wb") as f1:
                f1.write(video)
            re_list02=[]
            re_list02.append(v_title[num])
            num+=1
            re_list02.append("/static/livideo/"+id+".mp4")
            re_list01.append(re_list02)
    return re_list01

def main(categoryId):
    reqType="5"
    start=0
    # for i in range(2):
    return video_req(reqType,str(categoryId),str(start))
        # start = start + 12
