# %%
from get_coordinate import get_coordinate
import pandas as pd

df = pd.read_csv("分行特性表.csv")
addressList = df["分行地址"].to_list()

ad_list = []
for address in addressList:
    res = get_coordinate(address)
    ad_list.append(res)
    print(res)

# %%
import pandas as pd

df = pd.read_csv("分行特性表.csv")
# %%
df["x"]=a[:,0]
df["y"]=a[:,1]
# %%
