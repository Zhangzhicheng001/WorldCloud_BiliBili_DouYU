import  requests
from lxml import etree
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
}

#抓取函数
def yitianSpiderf(url):
    res=requests.get(url,headers=headers)
    tree=etree.HTML(res.content)
    comment_list=tree.xpath('//d/text()')
    with open('rng_fnc.txt','a+',encoding='utf-8') as f:
        for comment in comment_list:
            f.write(comment+'\n')

#主函数,其实所有是视频找到其id就能抓到所有的弹幕

def main():
    cid='80266814'                    #输入您的cid与url
    url='https://api.bilibili.com/x/v1/dm/list.so?oid=124438763'.format(cid)
    yitianSpiderf(url)

if __name__ == '__main__':
     main()


import re
import jieba
import os
from collections import Counter

os.getcwd()
#使用结巴分词
with open('rng_fnc.txt','r',encoding='utf-8') as f:
    txt=f.read()
jbwords=jieba.cut(txt)

#遇到这种非常规词不使用
with open('stopwords.txt' ,'r',encoding='utf-8') as f1:
    stopwords=f1.read()
result=[]
for word in jbwords:
    word=re.sub(r'[A-Za-z0-9\!?\%\[\]\,\.~]','',word) #去除英文符号
    if word:
        if word not in stopwords:
            result.append(word)
'+++++++++++++++统计'
print('=====',result,len(result))
print(Counter(result))
text='/'.join(result)

#词云处理
import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator
from PIL import Image
import numpy as np

myfon=r'C:\Windows\Fonts\msyh.ttc'  #选择你所需要的字体
img2=Image.open('jiangbei2.png')    #选择你所需要云图的形状
graph2=np.array(img2)

wc=WordCloud( scale=4,font_path=myfon,background_color='white',max_font_size=50,max_words=500,mask=graph2)
wc.generate(text)

plt.imshow(wc)
plt.axis("off")
plt.show()

wc.to_file("text.png")