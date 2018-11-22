#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 17:08
# @Author  : Ryu
# @Site    : 
# @File    : aiohttp_headers.py
# @Software: PyCharm
import asyncio,aiohttp
async def f():
    async with aiohttp.ClientSession(cookies={'a':'b'}) as session:
        async with session.get('http://httpbin.org/ip',proxy='http://118.190.95.35:9001') as resp:
            print(await resp.text())

asyncio.get_event_loop().run_until_complete(f())















