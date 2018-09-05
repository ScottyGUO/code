from bs4 import BeautifulSoup
import requests
import json
page=1
while page<5:
    url="http://pic.gamersky.com/home/getimagesindex?sort=time_desc&pageIndex=%d&pageSize=50&nodeId=21089"%(page)
    # http://pic.gamersky.com/home/getimagesindex?sort=time_desc&pageIndex=1&pageSize=50&nodeId=21089
    # http://pic.gamersky.com/home/getimagesindex?sort=time_desc&pageIndex=2&pageSize=50&nodeId=21089
    # http://pic.gamersky.com/home/getimagesindex?sort=time_desc&pageIndex=3&pageSize=50&nodeId=21089
    r=requests.get(url)
    #返回回来的是一个json格式的字符串，我们先把数据转换为字典，然后可以直接使用
    json_str=r.json() #把json格式字符串解析，发现解析出来不是字典，还是字符串，需要再次解析
    img_dict=json.loads(json_str) #再次解析
    # print(img_dict['body'])
    for i in img_dict['body']:
        print(i['originImg'])
    print('第%d页图片获取完毕'%(page))
    page+=1
