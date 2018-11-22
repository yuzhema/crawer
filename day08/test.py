#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/22 16:13
# @Author  : Ryu
# @Site    : 
# @File    : test.py
# @Software: PyCharm

# def A(fun):
#     print('aaaaa')
#     return fun
# @A
# def B():
#     print('bbbbb')
# B()


# def funA(fun):
#     def funB():
#         print('inner function funB')
#     funB()
#     return fun
#
# @funA
# def funC():
#     print('C')
#
# funC()


# def funA(f):
#     def funB():
#         print('inner function B')
#         return f()
#     return funB()
#
# @funA
# def funC():
#     print('C')
# funC()
import happybase

connection = happybase.Connection(host="192.168.245.36", port=9090)
# connection = happybase.Connection(host="hadoop6.baizhiedu.com", port=9090)

connection.open()
families = {
    "base":dict(),
    "address":dict()
}
connection.create_table('baizhi125:user',families)















