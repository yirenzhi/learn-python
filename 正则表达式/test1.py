# -*- coding: utf-8 -*-
#http://www.cnblogs.com/chuxiuhong/p/5885073.html
import re
key = r"<html><body><h1>hello world<h1></body></html>"#这段是你要匹配的文本
p1 = r"(?<=<h1>).+?(?=<h1>)"#这是我们写的正则表达式规则，你现在可以不理解啥意思
pattern1 = re.compile(p1)#我们在编译这段正则表达式
matcher1 = re.search(pattern1,key)#在源文本中搜索符合正则表达式的部分
print matcher1.group(0)#打印出来
'''
key = r"javapythonhtmlvhdl"
p1=r"python"
pattern1 = re.compile(p1)
matcher1 = re.search(pattern1,key)
print matcher1.group(0)
'''
key = r"<h1>hello world<h1>"#源文本
p1 = r"<h1>.+<h1>"#我们写的正则表达式，下面会将为什么
pattern1 = re.compile(p1)
print pattern1.findall(key)#发没发现，我怎么写成findall了？咋变了呢？

key = r"alsdfkjoqwerfjljzhouda@163.comasdofkjladksjf"
p = r"zhouda@163\.com"   #\转义符
pattern = re.compile(p)
print pattern.findall(key)

#*跟在其他符号后面表达可以匹配到它0次或多次
key = r"http://www.alsdfjl.com and https://www.faosdfjlasd.com"
p = r"https*"
pattern = re.compile(p)
print pattern.findall(key)

#[]代表匹配里面的字符中的任意一个
key = r"ladflja<hTml>hello<Html>helkfj"
p = r"<[Hh][Tt][Mm][Ll]>.*<[Hh][Tt][Mm][Ll]>"
pattern = re.compile(p)
print pattern.findall(key)

#[^]代表除了内部包含的字符以外都能匹配
key = r"mat cat hat pat"
p = r"[^p]at"
pattern = re.compile(p)
print pattern.findall(key)

#加了一个“?”我们就将贪婪的“+”改成了懒惰的“+”。这对于[abc]+,\w*之类的同样适用。
key = r"yiren_zhi@163.com.cn"
p = r"@.+\."
pattern = re.compile(p)
p1 = r"@.+?\."
pattern1 = re.compile(p1)
print pattern.findall(key)
print pattern1.findall(key)

'''
正则表达式	代表的匹配字符
[0-9]	0123456789任意之一
[a-z]	小写字母任意之一
[A-Z]	大写字母任意之一
\d	等同于[0-9]
\D	等同于[^0-9]匹配非数字
\w	等同于[a-z0-9A-Z_]匹配大小写字母、数字和下划线
\W	等同于[^a-z0-9A-Z_]等同于上一条取非
'''

#为了能够准确的控制重复次数，正则表达式还提供
#{a,b}(代表a<=匹配次数<=b)
key = r"saas and sas and saaas"
p = r"sa{1,2}s"
pattern = re.compile(p)
print pattern.findall(key)

