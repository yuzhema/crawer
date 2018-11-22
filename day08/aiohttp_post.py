#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 17:00
# @Author  : Ryu
# @Site    : 
# @File    : aiohttp_post.py
# @Software: PyCharm

import asyncio,aiohttp
async def ai133_post(url,data):
    async with aiohttp.ClientSession() as session:
        async with session.post(url,data=data) as resp:
            await resp.text()
            async with session.get('http://www.honestcareer.com/hr/index') as r:
                print(await r.text())

url='http://www.honestcareer.com/hr/dologin'
formdata={
'type': '1',
'username': '18501279410',
'password': 'hbw123'
}

loop=asyncio.get_event_loop()
loop.run_until_complete(ai133_post(url,formdata))












