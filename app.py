#-*- coding = utf-8-*-
#@Time : 2020/6/26 14:49
#@Author :Ella
#@File :app.py
#@Software : PyCharm

from flask import Flask,render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/index')
def home():
    return index()

@app.route('/movie')
def movie():
    datalist = []
    con = sqlite3.connect("movie250.db")
    print("成功打开数据库")
    cur = con.cursor()
    sql = "select * from movie250"
    data = cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()
    return render_template("movie.html",movies = datalist)

@app.route('/score')
def score():
    scorelist = []#评分
    num = []#每个评分所统计的电影
    con = sqlite3.connect("movie250.db")
    print("成功打开数据库")
    cur = con.cursor()
    sql = "select score,count(score) from movie250 group by score"
    data = cur.execute(sql)
    for item in data:
        scorelist.append(item[0])
        num.append(item[1])
    cur.close()
    con.close()
    return render_template("score.html",scorelist = scorelist,num = num)

@app.route('/word')
def word():
    return render_template("word.html")

@app.route('/team')
def team():
    return render_template("team.html")

if __name__ == '__main__':
    app.run(debug=True)