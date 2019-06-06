import itchat
from pyecharts.charts import Page,Pie
from collections import Counter
def annlysis(friends):
    friends_info = get_friends_info(friends)
    #男女性别比例
    sex_list = friends_info['sex']

    page = Page()
    chart1 = (
        Pie()
        .set_global_opts(
            title_opts=opts.TitleOpts(title="性别")
        )
        .add("",)
    )
    chart1 = Pie("微信好友性别比例图",title_pos='center')   #标题放在中间
    chart1.add("", attr, value, is_label_show=True, legend_orient="vertical", legend_pos="left")   #显示标签，图例组件垂直分布，图例位于左侧
    page.add(chart1)   #把chart1添加到页面中
    page.render()

c = (
        Pie()
        .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
        .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
https://pyecharts.org/#/zh-cn/basic_charts?id=pie%EF%BC%9A%E9%A5%BC%E5%9B%BE
https://www.shiyanlou.com/courses/1197/labs/8920/document/
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


if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    friends  = itchat.get_friends(update=True)