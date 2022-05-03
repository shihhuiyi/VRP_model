# %%
import tkinter as tk

win = tk.Tk()
win.title("Nihao")
win.geometry('800x600')
win.configure(background='white')

header_label = tk.Label(win, text='你好')
header_label.pack(side="top")

header_label = tk.Label(win, text='BMI 計算器')
header_label.pack(side="top")

height_frame = tk.Frame(win)
height_frame.pack(side=tk.TOP)
height_label = tk.Label(height_frame, text='身高（m）')

if __name__=="__main__":
    win.mainloop()

# %%
'''
import tkinter as tk
import math

window = tk.Tk()
window.title('BMI App')
window.geometry('800x600')
window.configure(background='white')

def calculate_bmi_number():
    height = float(height_entry.get())
    weight = float(weight_entry.get())
    bmi_value = round(weight / math.pow(height, 2), 2)
    result = '你的 BMI 指數為：{} {}'.format(bmi_value, get_bmi_status_description(bmi_value))
    result_label.configure(text=result)

def get_bmi_status_description(bmi_value):
    if bmi_value < 18.5:
        return '體重過輕囉，多吃點！'
    elif bmi_value >= 18.5 and bmi_value < 24:
        return '體重剛剛好，繼續保持！'
    elif bmi_value >= 24 :
        return '體重有點過重囉，少吃多運動！'

header_label = tk.Label(window, text='BMI 計算器')
header_label.pack()

height_frame = tk.Frame(window)
height_frame.pack(side=tk.TOP)
height_label = tk.Label(height_frame, text='身高（m）')
height_label.pack(side=tk.LEFT)
height_entry = tk.Entry(height_frame)
height_entry.pack(side=tk.LEFT)

weight_frame = tk.Frame(window)
weight_frame.pack(side=tk.TOP)
weight_label = tk.Label(weight_frame, text='體重（kg）')
weight_label.pack(side=tk.LEFT)
weight_entry = tk.Entry(weight_frame)
weight_entry.pack(side=tk.LEFT)

result_label = tk.Label(window)
result_label.pack()

calculate_btn = tk.Button(window, text='馬上計算', command=calculate_bmi_number)
calculate_btn.pack()

window.mainloop()
'''
# %%
a = input("Nihao")

print(a)
# %%
import folium

word_map =folium.Map()

folium.Marker(
    location=(35.69,139.69),
    popup="東京"
).add_to(word_map)

folium.Marker(
    location=(40.6643,-73.9385),
    popup="紐約"
).add_to(word_map)

folium.Marker(
    location=(48.51,2.2),
    popup="巴黎"
).add_to(word_map)

folium.Marker(
    location=(25.26,55.29),
    popup="杜拜"
).add_to(word_map)

route = folium.PolyLine(    #polyline方法爲將座標用線段形式連接起來
    [[35.69,139.69],[40.6642,-73.9385]],    #將座標點連接起來
    weight=3,  #線的大小爲3
    color='orange',  #線的顏色爲橙色
    opacity=0.8    #線的透明度
).add_to(word_map)
#word_map.save("word_map.html")
# %%
