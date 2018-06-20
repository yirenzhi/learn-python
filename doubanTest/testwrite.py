str1='1'
for i in range(10):
    with open('douban_1.txt', 'a+') as f:
        f.write(str1+'\n')
