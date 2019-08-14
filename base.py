import matplotlib.pyplot as plt
import numpy as np
import csv

datas = [1,4,9,16,25]
# print(datas)


print('Hello Test!')
normalTime = {}
overTime = {}
allTime = {}

# 列表生成式
# data_reader = csv.DictReader(open(filename,'r',encoding='UTF-8'))
# data_rows = [d for d in data_reader]
# print(data_rows[2].values())


filename = 'C:/Users/nuaas/Desktop/test.csv'

with open(filename,'r',encoding='UTF-8') as f:
    reader = csv.reader(f)
    head_row = next(reader)
    ivalue = {}
    for index,value in enumerate(head_row):
        ivalue[index] = value
    print(ivalue)
    # 正常工时
    workerId = -1
    writeDayNum = 0
    writeDaySum = {}
    peopleOrg = {}
    for row in reader:
        if row[10] == '按员工汇总':
            # 获取员工编号
            userid = row[2]
            normalTime[userid] = float(row[13])
            overTime[userid] = float(row[14])
            allTime[userid] = float(row[13])+float(row[14])
            # 获取各个部门人数
            peopleOrg[userid] = row[3]
            workerId += 1
            writeDaySum[workerId] = writeDayNum
            writeDayNum = 0
        else:
            writeDayNum += 1

    # print(writeDaySum)
    leaders = 0
    orgA = 0
    orgB = 0
    orgC = 0
    orgD = 0
    # print(peopleOrg.values())
    for org in peopleOrg.values():
        if org=='AAA':
            leaders += 1
        elif org =='AAA-01':
            orgA += 1
        elif org =='AAA-02':
            orgB += 1
        elif org =='AAA-03':
            orgC += 1
        else:
            orgD += 1
    # print(orgA)
    orgSum = [leaders-1,orgA+leaders-1,orgB+orgA+leaders-1,orgC+orgB+orgA+leaders-1,orgD+orgC+orgB+orgA+leaders-1]
    # print(orgSum[0])

    # print(normalTime)
# print(normalTime.keys())
x = list(range(len(normalTime.keys())))
# print(x)
# print(normalTime.values())

array = np.array(list(allTime.values()))
arrayMean = array.mean()
arrayMax = array.max()

avgData = []
# AAA部门
arrayAAA = array[:orgSum[0]+1]
meanA = arrayAAA.mean()
avgData.append(meanA)
# AAA-001部门
arrayAAA01 = array[orgSum[0]+1:orgSum[1]+1]
meanA1 = arrayAAA01.mean()
avgData.append(meanA1)
# AAA-002部门
arrayAAA02 = array[orgSum[1]+1:orgSum[2]+1]
meanA2 = arrayAAA02.mean()
avgData.append(meanA2)
# AAA-003部门
arrayAAA03 = array[orgSum[2]+1:orgSum[3]+1]
meanA3 = arrayAAA03.mean()
avgData.append(meanA3)
# AAA-004部门
arrayAAA04 = array[orgSum[3]+1:]
meanA4 = arrayAAA04.mean()
avgData.append(meanA4)
plt.plot(orgSum,avgData)


# plt.plot(x,list(normalTime.values()))
# plt.scatter(x,list(normalTime.values()),s=10)
# plt.plot(x,list(overTime.values()))
# plt.scatter(x,list(overTime.values()),s=10)
plt.plot(x,list(allTime.values()))
plt.scatter(x,list(allTime.values()),s=30)
plt.plot([0,len(x)],[arrayMean,arrayMean])
plt.plot([orgSum[0],orgSum[0]],[0,arrayMax])
plt.plot([orgSum[1],orgSum[1]],[0,arrayMax])
plt.plot([orgSum[2],orgSum[2]],[0,arrayMax])
plt.plot([orgSum[3],orgSum[3]],[0,arrayMax])
plt.plot([orgSum[4],orgSum[4]],[0,arrayMax])
plt.show()
