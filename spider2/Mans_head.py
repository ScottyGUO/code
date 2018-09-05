from bs4 import BeautifulSoup
import requests

url="https://www.woyaogexing.com/touxiang/nan/2018/663561.html"

r=requests.get(url) #请求该网页，得到网页源代码
soup=BeautifulSoup(r.content.decode('utf-8'),"html.parser") #把网页源代码解析为beautifulsoup节点形式

#得到所有的图片
# all_img=soup.find_all('img',attrs={"class":"lazy"}) #查找代码里，属性class值为lazy的img标签，返回列表
# num=0
# for once_img in all_img: #遍历列表，每次得到的是一个img标签
#     once_img_src="https:"+once_img.attrs['src'] #取到img标签里的src属性，并且拼接上https，得到图片链接
#     img_resource=requests.get(once_img_src,stream=True) #请求图片链接，得到图像资源
#     with open("./HeadImg/%d.jpg"%(num),'wb') as file: #创建文件，准备保存资源
#         for j in img_resource.iter_content(1024): #每次从得到的资源里读取一部分，遇到大文件不会卡顿
#             file.write(j) #把读取到的这一部分写入到文件里
#     num+=1

#得到热门标签
# all_a=soup.find_all('a',attrs={}) #直接取a标签的时候，因为网页中有很多的a标签，而且没有属性可以区分
# print(all_a)
#通过找到a标签的父级，发现是div 这个div有个class属性，可以用来区分，
#先找到 div，再去找div下面的a标签
this_div=soup.find('div',attrs={"class":"hot-tags"}) #返回的是列表
all_a=this_div.find_all('a')
for once_a in all_a:
    print(once_a.string)