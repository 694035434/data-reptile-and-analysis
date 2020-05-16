from flask import Flask,render_template,request
app=Flask(__name__)
# 首页
@app.route("/")
def xxx():
    return render_template("index.html")

@app.route("/financial")
def financial():
    return render_template("financial.html")

from splider.financial.financial_data import  Financial
@app.route("/data_Crawl",methods=["GET","POST"])
def data_Crawl():
    if request.method=="GET":
        page_num=request.args.get("page_num")
        page_size=request.args.get("page_size")
        pro_type = request.args.get("pro_type")
        pro_status= request.args.get("pro_status")
        # print(str(page_num),str(page_size),str(pro_type),str(pro_status))
        dt=Financial()
        # nurl = dt.url_join('1', '20', '1', '在售')
        nurl = dt.url_join(str(page_num),str(page_size),str(pro_type),str(pro_status))
        url_id = dt.data_req(nurl)
        second_url_list = dt.first_parse(url_id)
        result = dt.second_req_parse(second_url_list)
        # print(result)
        # result_list=result[1],result[3],result[5],result[7],result[9]
        return render_template("financial.html",u_result=result)

@app.route("/movie")
def movie():
    return render_template("movie.html")

from splider.movie import movie_splider
@app.route("/movie_Crawl",methods=["GET","POST"])
def movie_Crawl():
    if request.method=="GET":
        movie_type=request.args.get("movie_type")
        Classification=request.args.get("Classification")
        page_num = request.args.get("page_num")
        result=movie_splider.data_req(movie_type,Classification,str(page_num))
        return render_template("movie.html",u_result=result)


@app.route("/wz")
def wz():
    return render_template("wz.html")

from splider.wz import wz_splider
@app.route("/wz_Crawl",methods=["GET","POST"])
def wz_Crawl():
    if request.method=="GET":
        hero_name=request.args.get("hero_name")
        result=wz_splider.photo_req(hero_name)
        return render_template("wz.html",u_result=result)
@app.route("/li_video")
def li_video():
    return render_template("li_video.html")

from splider.li_video import lishipin
@app.route("/li_Crawl",methods=["GET","POST"])
def li_Crawl():
    if request.method=="GET":
        video_class=request.args.get("pro_type")
        result=lishipin.main(video_class)
        # print(result)
        return render_template("li_video.html",u_result=result)
@app.route("/it_home")
def it_home():
    with open("splider/work3/IT.csv","r") as f1:
        result=f1.readlines()
        result_list=[]
        for i in result:
            result_list.append(i.replace("\n","").split(","))


    return render_template("it_home.html",u_result=result_list)


if __name__ == '__main__':
    app.run()

