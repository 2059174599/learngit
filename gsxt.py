# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import traceback 
import pymysql
import random
import json
import time
import re

#一般请求
def getHtmlText(url):
    headers = {
    'Cookie': '__jsluid=ba0aad1bf14b8e19828fca412151ed81; UM_distinctid=1643b4b55e5b25-0e36229a6e53b-6373563-15f900-1643b4b55e6295; Hm_lvt_d7682ab43891c68a00de46e9ce5b76aa=1534334042; SECTOKEN=7082104079821572037; tlb_cookie=S172.16.12.69; __jsl_clearance=1534840055.225|0|fejO%2B0sV1W2RMmCAUjI72bDxZ4c%3D; CNZZDATA1261033118=1326626745-1529999540-http%253A%252F%252Fwww.gsxt.gov.cn%252F%7C1534836837; gsxtBrowseHistory1=%0FS%04%06%1D%04%1D%10SNS%24%26%3B%22%3D%3A71%3A%3B01%3A%219EEDDDD%12%12LDLDLEALM%15%11%12M%15DEAL%15L%10%11%11AM%40B%15%17%17SXS%11%1A%00%1A%15%19%11SNS%E5%8D%A3%E4%BB%98%E8%9F%B9%E6%94%84%E5%BF%B5%E4%BE%95%E6%9D%BD%E9%98%A4%E5%84%98%E5%8E%8CSXS%11%1A%00%00%0D%04%11SNEEAFXS%02%1D%07%1D%00%00%1D%19%11SNEAG%40LGBBMGGF%40%09; gsxtBrowseHistory2=%0FS%04%06%1D%04%1D%10SNS%24%26%3B%22%3D%3A71%3A%3B01%3A%219EEDDDD%12%12LDLDLEA%16EGEECLDEA%16E%10%40%12%17DB%40CFDGSXS%11%1A%00%1A%15%19%11SNS%E7%89%85%E7%A6%A5%E6%81%A9%E7%90%AA%E9%92%B6%E7%88%8D%EF%BD%BC%E5%8D%A3%E4%BB%98%EF%BD%BD%E6%98%8E%E8%82%89%E6%8B%B4%E6%9D%9B%E6%9D%BD%E9%98%A4%E5%84%98%E5%8E%8CSXS%11%1A%00%00%0D%04%11SNEEAEXS%02%1D%07%1D%00%00%1D%19%11SNEAG%40LELE%40FBBD%09; gsxtBrowseHistory3=%0FS%04%06%1D%04%1D%10SNS%24%26%3B%22%3D%3A71%3A%3B01%3A%219EEDDDDFD%11GL%16L%16%40%12L%16ML%10FDE%40%12%15ACC%12L%12%10BMD%17SXS%11%1A%00%1A%15%19%11SNS%E5%8D%A3%E4%BB%98%E4%BB%8E%E4%BB%8E%E7%A7%93%E6%8B%A1%E8%B4%B0%E7%AF%95%E7%91%B2%E8%83%95%E4%BA%89%E6%9D%BD%E9%98%A4%E5%84%98%E5%8E%8CSXS%11%1A%00%00%0D%04%11SNEFFFXS%02%1D%07%1D%00%00%1D%19%11SNEAG%40LEBCACF%40%40%09; gsxtBrowseHistory4=%0FS%04%06%1D%04%1D%10SNS%24%26%3B%22%3D%3A71%3A%3B01%3A%219%40FDDDDE%40FDDDDDCDDDBELDMCSXS%11%1A%00%1A%15%19%11SNS%E4%B9%8D%E6%B0%AB%E5%8E%97%E5%B9%B6%E9%86%A5%E6%9D%9C%E7%95%AB%E6%81%B5%E7%A6%B9%E5%84%8F%E6%AF%A2%E4%B9%A7%E4%B9%AE%E5%91%BC%E4%BC%A8%E7%A5%8ASXS%11%1A%00%00%0D%04%11SNMEDDXS%02%1D%07%1D%00%00%1D%19%11SNEAG%40CBC%40%40LDB%40%09; gsxtBrowseHistory5=%0FS%04%06%1D%04%1D%10SNS%24%26%3B%22%3D%3A71%3A%3B01%3A%219GFDDDDGFDADDDDDDDDDDFDGEEFCSXS%11%1A%00%1A%15%19%11SNS%E7%A7%BB%E5%84%80%E7%BA%B3%E9%81%94%EF%BD%BC%E8%8A%BB%E5%B6%AA%EF%BD%BD%E6%9D%BD%E9%98%A4%E5%84%98%E5%8E%8CSXS%11%1A%00%00%0D%04%11SNBEADXS%02%1D%07%1D%00%00%1D%19%11SNEAG%40L%40DMCFMED%09; JSESSIONID=21609D07D9DDC9DE78F60D42731C2557-n1:14',
    'Host': 'www.gsxt.gov.cn',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
    }
    try:
        r = requests.get(url,headers = headers,timeout=30) #cookie和User-Agent需统一，且cookie三小时后过期
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        traceback.print_exc()
        return "请求错误"
        
#列表页url
def getCompany_url(html):
    soup = BeautifulSoup(html, 'html.parser')
    #href = soup.find('data-value',class_='top4 fl lll')
    hrefs = re.findall('''</i><a href='(.*?)'>''',html,re.S)
    hrefs = set(hrefs) #url去重
    for href in hrefs:
        return href

#内容
def getContent(html,url):
    res_data={}
    soup = BeautifulSoup(html, 'html.parser')
    content = re.search('''添加业务逻辑 -->(.*?)</dd>.*?title="(.*?)">.*?法定代表人.*?class="result">(.*?)</dd>.*?成立日期.*?class="result">(.*?)</dd>.*?经营范围.*?<dd>(.*?)</dd>''',html,re.S)
    state = re.search('''class="jingying">(.*?)class=''',html,re.S).group(1).strip() if re.search('''class="jingying">(.*?)class=''',html,re.S) else '未进入异常名录'
    if content:
        company = content.group(2).strip() #公司名称
        # state = re.search('''class="jingying">(.*?)class=''',html,re.S).group(1) #状态
        state = re.sub(r'[<div> / <div]| ','',state) #过滤特殊字符
        cod = content.group(1).strip() #统一社会信用代码
        corporation = content.group(3).strip() #法人
        pub_date = content.group(4).strip() #成立日期
        reg_dep = content.group(5).strip() #经营范围
        company_url = url
        #print(company,state,cod,corporation,pub_date,reg_dep,company_url)
        sql = "INSERT INTO gsxt_heat (company, cod, state, corporation, pub_date, reg_dep, url) \
        values('%s', '%s', '%s', '%s', '%s', '%s', '%s')" %\
        (company, cod, state, corporation, pub_date, reg_dep, url)#sql    
        db_execute(sql) #入库
        
#链接数据库
def db_execute(sql):
    dbs = pymysql.connect(
                            host='localhost',
                            user='wxy', 
                            passwd='66357070', 
                            db='sys',
                            port=3306,
                            charset="utf8"
                        )
    cursor = dbs.cursor()
    #print('链接数据库')
    try:
        dbs.autocommit(True)
        cursor.execute(sql)
        dbs.commit()
    except:
        traceback.print_exc() #异常处理
        dbs.rollback() #回滚
    cursor.close()
    
#主函数
def main(keyword):
    url = 'http://www.gsxt.gov.cn/corp-query-entprise-info-hot-search-list.html?province=' + str(keyword) + '0000'
    html = getHtmlText(url) #起始页源码
    company_url = 'http://www.gsxt.gov.cn' + str(getCompany_url(html)) #列表页url
    company_content = getHtmlText(company_url) #内容页源码
    time.sleep(random.randint(2,5)) #暂缓
    getContent(company_content,company_url) #内容
    #content = getContent(html,keyword)
        
if __name__ == '__main__':
    #map(main,[unmber for unmber in range(0,2,10)])
    for number in range(10,38,1):
        main(number)
