from PIL import Image
import numpy as np
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import requests
import re
import time
import pandas as pd
import imageio
from imageio.core.functions import imread


def getHTMLText(url):  # 获得页面
    try:
        kv = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
              'cookie': 'cna=0spiGXvFDwUCAXL/2gtMWRxv; _samesite_flag_=true; cookie2=14a19824091c47480692b8601ec39fae; t=a4096c35d3c48c21921f02dbddf53a90; _tb_token_=e13e3be78bf37; xlly_s=1; sgcookie=E100PV%2FHGPnlh%2FTeTsW52XFTAV%2FIIMfYgXMD8oUB5WrCL5NwvZYFDdgzLe%2BUCqsIM4VWiCEF8uIhUM8zX3UAOCJBZB02DEFmQkbj8ZZsoLAQb9o%3D; unb=3987897451; uc3=lg2=W5iHLLyFOGW7aA%3D%3D&id2=UNk%2FT%2BT9u9SGrw%3D%3D&vt3=F8dCujpQtYzEsLyew6Y%3D&nk2=AH%2Bqtx1ImQ%3D%3D; csg=68331fda; lgc=cegreat; cancelledSubSites=empty; cookie17=UNk%2FT%2BT9u9SGrw%3D%3D; dnk=cegreat; skt=fc20fedd3429a925; existShop=MTYzNjQ0NjUwNQ%3D%3D; uc4=nk4=0%40AhEn8NIs32YlctpxZRa3qMZB&id4=0%40Ug41TjANg2FZXh0PQeNg49B%2BUCDt; tracknick=cegreat; _cc_=Vq8l%2BKCLiw%3D%3D; _l_g_=Ug%3D%3D; sg=t18; _nk_=cegreat; cookie1=AHhVFLT%2BLhE5IttMkWEdzDfbxChFg%2BXJTRGv%2F1FreYk%3D; enc=PJOMn3o9zagG0KCvQce0oIBIFz2nLumEq5s3KibiZa5fD4GSS6Su2QvOJFvz7Wly5%2BYuD7ubvdbreZPue%2BhfLw%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; thw=cn; mt=ci=120_1; uc1=existShop=false&cookie14=Uoe3ccrcMfieng%3D%3D&pas=0&cookie16=Vq8l%2BKCLySLZMFWHxqs8fwqnEw%3D%3D&cookie15=W5iHLLyFOGW7aA%3D%3D&cookie21=VFC%2FuZ9ainBZ; tfstk=cpsAB7xKV7VcpPvRLZUlfIu1Li6Aa7kvsxOtX8soi_xEUPnjDs0GxMHR4r9wLLwR.; l=eBT6gp9IjV0JaRlBBO5aFurza77O0QAbzsPzaNbMiInca1-1wBBgtNCd_NH6kdtj_tfxbetrwmwghRFHJ7z38x90MWpDRs5mpxv9-; isg=BIWF-bFqSI7BMm2DK3K2lMbqlMG_QjnU-tMlFofoXryzHqeQT5L5pTO8KEroXlGM; JSESSIONID=F02ACED973E8DDD2C3459F18F02D86C0'
              }
        r = requests.get(url, headers=kv, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print(2)
        return r.text
    except:
        print("获取页面失败")


def parsePage(ilt, html):  # 对每一个获得的页面进行解析
    # 两个变量分别是结果的列表类型和相关的HTML页面的信息
    try:
        time.sleep(5)
        re1 = re.compile(r'\"view_price\"\:\"[\d\.]*\"')
        # re1 = re.compile(r'\"view_price\"\:\".*?\"')  # 编译商品名称正则表达式
        tlt = re1.findall(html)
        #plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        #tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(tlt)):
            title = eval(tlt[i].split(':')[1])  # 去掉raw_title字段，只要名称部分
            title.replace("'", "")
            ilt.append(title)
            
        df = pd.DataFrame(ilt)
        # df["price"] = ilt
        df.to_csv("priceDB.csv", mode='a', encoding='utf-8', index=False)
        print(1)
    except:
        print("网页解析失败")


def main():
    depth = 5
    start_url = 'https://s.taobao.com/search?spm=a230r.1.1998181369.d4919860.299bb78aHpSTCP&q=%E6%95%99%E8%82%B2%E6%9C%BA%E5%99%A8%E4%BA%BA&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&ie=utf8&initiative_id=tbindexz_20170306&tab=mall&sort=sale-desc&bcoffset=0&p4ppushleft=%2C44&s='
    infoList = []  # 定义整个的输出结果变量
    for i in range(depth):  # 对每次翻页后的URL链接进行设计
        try:
            url = start_url + str(44*i)
            html = getHTMLText(url)
            parsePage(infoList, html)
        except:
            continue
    
    # ConvertStr = ''
    # for i, item in enumerate(infoList):
    #     ConvertStr += item[0].strip()

    # with open('static/content.txt', mode='w', encoding='utf-8') as f:
    #     f.write(ConvertStr)
# 调用主函数
main()
