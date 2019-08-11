import matplotlib.pyplot as plt
import numpy
import csv

datas = [1,4,9,16,25]
# print(datas)


print('Hello Test!')
normalTime = {}
overTime = {}
allTime = {}
filename = 'C:/Users/Administrator/PycharmProjects/dataanalysis/data/test.csv'
with open(filename,'r',encoding='UTF-8') as f:
    reader = csv.reader(f)
    head_row = next(reader)
    ivalue = {}
    for index,value in enumerate(head_row):
        ivalue[index] = value
    print(ivalue)
    # 正常工时
    for row in reader:
        if row[10] == '按员工汇总':
            # 获取员工编号
            userid = row[2]
            normalTime[userid] = float(row[13])
            overTime[userid] = float(row[14])
            allTime[userid] = float(row[13])+float(row[14])
    # print(normalTime)
# print(normalTime.keys())
x = list(range(len(normalTime.keys())))
print(x)
print(normalTime.values())

plt.plot(x,list(normalTime.values()))
plt.scatter(x,list(normalTime.values()),s=10)
plt.plot(x,list(overTime.values()))
plt.scatter(x,list(overTime.values()),s=10)
plt.plot(x,list(allTime.values()))
plt.scatter(x,list(allTime.values()),s=30)
plt.show()
