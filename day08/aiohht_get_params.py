#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 12:58
# @Author  : Ryu
# @Site    : 
# @File    : aiohht_get_params.py
# @Software: PyCharm

import asyncio,aiohttp

def get_params(param):
    params={}
    for data in param.split('\n'):
        params.update({data.split(':')[0].strip(): data.split(':')[1].strip()})
    return params
param = '''pageSize: 60
    cityId: 763
    workExperience: -1
    education: -1
    companyType: -1
    employmentType: -1
    jobWelfareTag: -1
    kw: python
    kt: 3
    _v: 0.00752017
    x-zp-page-request-id: 2f3389d4b9164087b6cbca89a3f98e76-1542334620581-439137'''
params = get_params(param)
url = 'https://fe-api.zhaopin.com/c/i/sou'

def f2(datas):
    print(datas.result())

async def get_urls_from_zhilian(url,params):
    async with aiohttp.ClientSession() as session:
        async with session.get(url,data=params) as resp:   #发请求，得到的是一个响应流
            print(await resp.read())   #从流中获取响应，二进制流
            print(await resp.text())   #从流中获取响应，utf-8
            return await resp.text()
loop=asyncio.get_event_loop()     #创建事件循环
task=asyncio.ensure_future(get_urls_from_zhilian(url,params))   #手动转换成任务
task.add_done_callback(f2)         # 回调函数
loop.run_until_complete(task)
print(task.done())
print(task.result())