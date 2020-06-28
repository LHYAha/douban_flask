#-*- coding = utf-8-*-
#@Time : 2020/6/26 18:09
#@Author :Ella
#@File :testCloud.py
#@Software : PyCharm

import jieba                                #分词
from matplotlib import pyplot as plt        #绘图，数据可视化
from wordcloud import WordCloud             #词云
from PIL import  Image                      #图片处理
import numpy as np                          #矩阵运算
import sqlite3                              #数据库

con = sqlite3.connect("movie250.db")
cur = con.cursor()
sql = "select introduction from movie250"
data = con.execute(sql)
text = ""
for item in data:
    text = text + item[0]
cur.close()
con.close()

#分词
cut = jieba.cut(text)
string = ' '.join(cut)
print(len(string))

#取图
img = Image.open('tree.jpg')#.static\assets\img\tree.jpg
img_array = np.array(img) #将图片转换为数组
wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path="STXINGKA.TTF" #字体所在位置：C:\Windows\Fonts
)
wc.generate_from_text(string)

#绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')#是否显示坐标轴
# plt.show() #显示生成的词云图片

#输出梯云图片到文件
plt.savefig('word.jpg',dpi=500)