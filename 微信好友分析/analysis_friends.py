'''
好友分析图
1.4 实验环境
python 3.5
itchat 1.3.10
pyecharts 0.5.11
pillow 5.3


2.1.1 自动登录,收发信息，并获取好友数据

整合成适当的数据结构，并用图片表示

微信好友性别比例图

好友省级分布（中国地图）
省份判断是否是空，是否有英文（都不计入统计）

好友城市分布Top10柱状图
'''

import itchat
from pyecharts.charts import Page,Pie,Map,Bar
from collections import Counter
from pyecharts import options as opts
import re
def countPro(pro_list):
    pro_dict={}
    for i in pro_list:
        if re.search('[a-zA-Z]',i):
            continue
        elif pro_dict.__contains__(i):
            pro_dict[i]+=1
        else:
            pro_dict[i]=1
    pro_dict.pop('')   # 去掉空的键
    return pro_dict

def annlysis(friends):
    friends_info = get_friends_info(friends)
    #男女性别比例
    sex_list = friends_info['sex']
    tag_list=['未知','男','女']
    c_sex = Counter(sex_list)
    sex_value=[c_sex[0],c_sex[1],c_sex[2]]

    page = Page()
    chart1 = (
        Pie()
        .add("", [list(z) for z in zip(tag_list, sex_value)])
        .set_global_opts(title_opts=opts.TitleOpts(title="性别比例"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}  占比:{d}%"))
    )
    page.add(chart1)   #把chart1添加到页面中


    #好友省级分布（中国地图）
    pro_list = friends_info['province']
    #处理省份数据，删除不需要的
    pro_dict = countPro(pro_list)
    #画图
    chart2 = (
        Map()
        .add("", [list(z) for z in zip(pro_dict.keys(), pro_dict.values())], "china")
        .set_global_opts(
            title_opts=opts.TitleOpts(title="好友省级分布（中国地图）"),
            visualmap_opts=opts.VisualMapOpts(),)
    )  
    page.add(chart2)   #把chart2添加到页面中  


    #好友城市分布Top10柱状图
    sort_pro = sorted(pro_dict.items(),key=lambda item:item[1],reverse=True)
    sort_pro=sort_pro[:10]
    chart3 = (
        Bar()
        .add_xaxis(list(map(lambda item:item[0],sort_pro)))
        .add_yaxis("", list(map(lambda item:item[1],sort_pro)))
        .set_global_opts(title_opts=opts.TitleOpts(title="好友城市分布Top10柱状图"))
    )
    page.add(chart3)   #把chart3添加到页面中  

    page.render()

def get_friends_info(friends):
    friends_info = dict(
        username=get_key_info(friends, 'UserName'),    # 用户名
        sex=get_key_info(friends, 'Sex'),              # 性别
        province=get_key_info(friends, 'Province'),    # 省份
        city=get_key_info(friends, 'City')             # 城市
    )
    return friends_info


def get_key_info(friends,key):
    return list(map(lambda friend:friend.get(key),friends))

def BinarySearch(  L,  X ):
    n=len(L)
    data=L
    pos=-1
    start =0
    fin = n-1
    while start<=fin:
        mid = (start+fin)//2
        print("start:%d,fin:%d,min:%d"%(start,fin,mid))
        if(X>data[mid]):
            start=mid+1
        elif(X<data[mid]):
            fin=mid-1
        else:
            pos=mid
            print("pos:"+str(pos))
            return pos
    
    print("pos:"+str(pos))
    return 0


if __name__ == '__main__':
    itchat.auto_login(enableCmdQR=-2,hotReload=True) 
    friends  = itchat.get_friends(update=True)
    annlysis(friends)
    print(type(friends))
    # #存储朋友数据
    # with open("friends.txt","w",encoding='utf-8') as f:
    #     f.write(str(friends))

    # list1=[]
    # with open("friends.txt","r",encoding='utf-8') as f:
    #     list1 = itchat.storage.templates.ContactList(f.read())
    # annlysis(list1)
    # list1=[12,31,55,89,101]
    # x=31
    # BinarySearch(list1,x)
   


