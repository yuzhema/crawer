#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 17:19
# @Author  : Ryu
# @Site    : 
# @File    : yibuzhilian.py
# @Software: PyCharm
import MySQLdb
from lxml import etree

import aiohttp,asyncio

async def mylist(index):
    params={}
    param = '''pageSize: 60
                  workExperience: -1
                  education: -1
                  companyType: -1
                  employmentType: -1
                  jobWelfareTag: -1
                  kt: 3
                  _v: 0.00752017
                  x-zp-page-request-id: 2f3389d4b9164087b6cbca89a3f98e76-1542334620581-439137'''
    for data in param.split('\n'):
        params.update({data.split(':')[0].strip(): data.split(':')[1].strip()})
    # params.update({'kw': title})
    # params.update({'cityId': cityid})
    params.update({'start': index})
    urls = []

    async with aiohttp.ClientSession() as session:
        async with session.get(url='https://fe-api.zhaopin.com/c/i/sou', params=params) as resp:
            datas=await resp.json()
            datas=datas['data']
            for data in datas['results']:
                urls.append(data['numFound'])
            return urls,datas['numFound']


async def detail(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            text=await resp.text()
            html=etree.HTML(text)
            title=html.xpath('//h1/text()')[0]
            money=html.xpath('//li[@class="info-money"]/strong/text()')[0]
            return [title,money]

conn=MySQLdb.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    db='db133',
    password='111111',
    charset='utf8'
)
cursor=conn.cursor()

def myMysql(task):
    sql='insert into t_zhilian(title,salary) values(%s,%s)'
    cursor.execute(sql,task.result())
    conn.commit()

if __name__ == '__main__':
    city_ids = ['530', '538', '765', '763']
    kws = ['AI', '爬虫', '大数据', 'python web']
    loop=asyncio.get_event_loop()
    for city in city_ids:
        for kw in kws:
            index=0
            while 1:
                task_list=asyncio.ensure_future(mylist(index,kw,city))
                loop.run_until_complete(task_list)
                if task_list.done():
                    urls,num=task_list.result()
                    tasks=[]
                    for url in urls:
                        task=asyncio.ensure_future(detail(url))
                        task.add_done_callback(myMysql)
                        tasks.append(task)
                    loop.run_until_complete(asyncio.wait(tasks))
                    if index>=num:
                        break
                    index+=60

