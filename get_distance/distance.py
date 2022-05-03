# %%
#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Seven'


import math
import pandas as pd


# 計算距離
def getDistance(latA, lonA, latB, lonB):
    ra = 6378140  # 赤道半徑
    rb = 6356755  # 極半徑
    flatten = (ra - rb) / ra  # Partial rate of the earth
    # change angle to radians
    radLatA = math.radians(latA)
    radLonA = math.radians(lonA)
    radLatB = math.radians(latB)
    radLonB = math.radians(lonB)

    pA = math.atan(rb / ra * math.tan(radLatA))
    pB = math.atan(rb / ra * math.tan(radLatB))
    x = math.acos(math.sin(pA) * math.sin(pB) + math.cos(pA) * math.cos(pB) * math.cos(radLonA - radLonB))
    c1 = (math.sin(x) - x) * (math.sin(pA) + math.sin(pB)) ** 2 / math.cos(x / 2) ** 2
    c2 = (math.sin(x) + x) * (math.sin(pA) - math.sin(pB)) ** 2 / math.sin(x / 2) ** 2
    dr = flatten / 8 * (c1 - c2)
    distance = ra * (x + dr)
    distance = round(distance / 1000, 4)
    # f'{distance}km'
    return distance

if __name__=="__main__":
    #banklist = [1,2,3]
    distance = pd.DataFrame()
    for b1 in banklist:
        dd = []
        for b2 in banklist:
            if b1==b2:
                dd.append(0)
            else:
                d = getDistance(x["{}".format(b1)], y["{}".format(b1)], x["{}".format(b2)], y["{}".format(b2)])
                dd.append(d)
        distance["{}".format(b1)]=dd
# %%
import pandas as pd

df = pd.read_csv("分行特性表1.csv")
# %%
x = {}
y = {}
for i,j,k in zip(df["分行代碼"],df["x"],df["y"]):
    x["{}".format(i)]=j
    y["{}".format(i)]=k
# %%
banklist = [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 101, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 115, 116, 117, 118, 119, 120, 121, 122, 123, 125, 126,
            127, 128, 129, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 143, 144, 145, 146, 147, 148, 149, 150, 153, 154, 155, 156, 157, 158, 159, 160, 162, 164, 165, 166, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 185, 186, 187, 188, 189, 190, 192, 193, 196]
# %%
for banknum in df["分行代碼"]:
    if banknum in banklist:
        print(banknum,"true")
    else:
        print(banknum,"false")
# %%
df.to_csv("分行特性表1.csv", encoding = "utf_8_sig")
# %%
