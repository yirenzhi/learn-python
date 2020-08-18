import json
from collections import defaultdict
path='chapter2/usagov_bitly_data2012-03-16-1331923249.txt'
#open(path).readline()

records = [json.loads(line) for line in open(path)]     #json.loads把字符转化成json格式

def get_counts(sequence):
    counts={}
    for x in sequence:
        if x in counts:
            counts[x]+=1
        else:
            counts[x]=1
    return counts

#这个函数处理更优雅
def get_counts2(sequence):
    counts=defaultdict(int)
    for x in sequence:
        counts[x]+=1
    return counts

#处理字典，将key和value对调并排序,取前n名
def chuliDict(dict1,n=10):
    dict2 = [(count,tz) for tz, count in dict1.items()]
    dict2.sort()
    return dict2[-10:]

time_zones = [record['tz'] for record in records if 'tz' in record]
counts = get_counts2(time_zones)
#print(counts['America/Chicago'])
#print(len(time_zones))
counts2= chuliDict(counts)
#print(counts2)


#方法2，极大的简化
from collections import Counter 
counts3 = Counter(time_zones)
#print(counts3.most_common(10))

from pandas import DataFrame, Series
import pandas as pd; import numpy as np 
frame = DataFrame(records)
#print(frame['tz'][:10])
#print(frame['tz'].value_counts()[:10])

clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz=='']='Unknown'
tz_counts = clean_tz.value_counts()
print(tz_counts[:10])

tz_counts[:10].plot(kind='barh', rot=0)

results = Series([x.split()[0] for x in frame.a.dropna()])

print(results[:5])

print(results.value_counts()[:8])

#剔除缺失的部分
cframe = frame[frame.a.notnull()]

#操作系统分类
operating_system = np.where(cframe['a'].str.contains('Windows'),'Windows','Not Windows')
print(operating_system[:5])

by_tz_os = cframe.groupby(['tz', operating_system])

agg_counts = by_tz_os.size().unstack().fillna(0)

print(agg_counts[:10])