'''
用上一个文件的方法获取好友数据，通过用户名调用img = itchat.get_head_img(uname)
            f.write(img)
将头像保存到本地

使用Image 拼接图片
输入手机分辨率的长宽

img = img.resize((width, width), Image.ANTIALIAS)   # 缩小图片
new_img.paste(img, (x * width, y * width))   # 拼接图片，一行排满，换行拼接
'''

import itchat
from PIL import Image
import os, random, math
def down_Img(friends):
    friends_info=get_friends_info(friends)
    name_list = friends_info['username']
    nick_list = friends_info['nickname']
    for i in range(len(name_list)):
        with open("headImgs/"+str(i)+".png","wb") as f:
            img_dir = itchat.get_head_img(name_list[i])
            f.write(img_dir)


def get_friends_info(friends):
    friends_info = dict(
        username=get_key_info(friends, 'UserName'),    # 用户名
        nickname=get_key_info(friends, 'NickName'),    # 用户名
    )
    return friends_info


def get_key_info(friends,key):
    return list(map(lambda friend:friend.get(key),friends))

def create_img():
    x=0
    y=0
    imgs = os.listdir("headImgs")
    random.shuffle(imgs)  # 将文件列表随机排序

    input_length = int(input("请输入手机屏保长的像素值(一般是两个值中较大的值):"))
    input_width = int(input("请输入手机屏保宽的像素值(一般是两个值中较小的值):"))

    new_img = Image.new('RGBA', (input_width, input_length))   # 创建 长*宽 的图片用于填充各小图片
    width = int(math.sqrt(input_length * input_width / len(imgs)))   # 以 长*宽 来拼接图片，math.sqrt()开平方根计算每张小图片的宽高
    num_line = int(input_width / width)   # 每行图片数

    for i in imgs:  #对每一张图片逐个进行处理
        try:
            img = Image.open("headImgs/" + i)
        except IOError:
            print("第{}张图片为空".format(i))  #可能会出现某张图片为空的情况
        else:
            img = img.resize((width, width), Image.ANTIALIAS)   # 缩小图片
            new_img.paste(img, (x * width, y * width))   # 拼接图片，一行排满，换行拼接
            x += 1
            if x >= num_line:
                x = 0
                y += 1

    new_img.save("mixedImg.png")
    itchat.send_image('mixedImg.png', toUserName='filehelper')   #通过文件传输助手发送到自己微信中
    new_img.show()
if __name__ == '__main__':
    itchat.auto_login(hotReload=True)
    friends  = itchat.get_friends(update=True)
    
    #down_Img(friends)

    #拼接图片
    create_img()
