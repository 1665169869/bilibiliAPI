# -*- coding: utf-8 -*-
# @file main.py
#

from bilibiliAPI.login_info import login_info
from bilibiliAPI.QR import QR

table='fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
tr={}
for i in range(58):
    tr[table[i]]=i
s=[11,10,3,8,4,6]
xor=177451812
add=8728348608
def bvInav(bvid):
    r = 0
    for i in range(6):
        r+=tr[bvid[s[i]]]*58**i
    return (r-add)^xor

def avInbv(avid):
	x=(avid^xor)+add
	r=list('BV1  4 1 7  ')
	for i in range(6):
		r[s[i]]=table[x//58**i%58]
	return ''.join(r)

# bv转av代码:
# 作者：mcfx
# 链接：https://www.zhihu.com/question/381784377/answer/1099438784
# 来源：知乎