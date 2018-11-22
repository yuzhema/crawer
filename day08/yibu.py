#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 12:54
# @Author  : Ryu
# @Site    : 
# @File    : yibu.py
# @Software: PyCharm

import asyncio,aiohttp
import time
import requests

async def f1(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(await resp.text())


def timecount(fun):
    def a(url):
        start=time.clock()
        fun(url)
        end=time.clock()
        print(end-start)
    return a

@timecount
def f2(url):
    for i in range(5):
        print(requests.get(url).text)

url='http://httpbin.org/ip'

# f2(url)
# time1=time.clock()
# loop=asyncio.get_event_loop()
# task=[f1(url) for i in range(600)]
# loop.run_until_complete(asyncio.wait(task))
# print(time.clock()-time1)
















