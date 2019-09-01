import matplotlib.pyplot as plt
import numpy as np
import csv


print('TimeData Project!')
filename = './test.csv'

normalTime = {}
overTime = {}
allTime = {}

with open(filename,'r') as f:
    reader = csv.reader(f)
    head_row = next(reader)
    ivalue = {}
    for index,value in enumerate(head_row):
        ivalue[index] = value
    workerId = -1
    writeDayNum = 0
    outDays = 0
    writeDaySum = {}
    peopleOrg = {}
    outTime = []
    for row in reader:
        if row[10] == '按员工汇总':
            # 获取员工编号
            userid = row[2]
            normalTime[userid] = float(row[13])
            overTime[userid] = float(row[14])
            allTime[userid] = float(row[13])+float(row[14])
            outTime.append(outDays)
            outDays = 0
            # 获取各个部门人数
            peopleOrg[userid] = row[3]
            # 计算每个人填报的工时数据
            workerId += 1
            writeDaySum[workerId] = writeDayNum
            writeDayNum = 0
        else:
            if row[12] == '出差工时':
                outday = float(row[13])
                outDays  += outday
            writeDayNum += 1
    outTime.append(outDays)
    outTime.pop(0)

    # 个人数据可视化
    x = list(range(len(normalTime.keys())))
    arrayall = np.array(list(allTime.values()))
    arraynormal = np.array(list(normalTime.values()))
    arrayover = np.array(list(overTime.values()))
    arrayout = np.array(list(outTime))
    # 计算个人100小时KPI
    array100h = arrayover + arrayout
    # 计算平均出差工时数据
    arrayMean = array100h.mean()
    arrayMax = array100h.max()
    print(arrayMean)
    print(arrayMax)

    plt.bar(x, arrayall)
    # plt.scatter(x, array100h, s=10)
    plt.bar(x,array100h)
    # plt.scatter(x,array100h,s=10)
    plt.plot([0,len(x)],[300,300])
    plt.show()
    # plt.plot(x,list(overTime.values()))
    # plt.scatter(x,list(overTime.values()),s=10)

    # plt.plot(x,list(allTime.values()))
    # plt.scatter(x,list(allTime.values()),s=10)
    # print(writeDaySum)



    # 计算各部门工时数据
    leaders = 0
    orgoffice = 0
    orgA = 0
    orgB = 0
    orgC = 0
    orgD = 0
    # print(peopleOrg.values())
    for org in peopleOrg.values():
        if org=='AAA':
            leaders += 1
        elif org=='AAA-00':
            orgoffice += 1
        elif org =='AAA-01':
            orgA += 1
        elif org =='AAA-02':
            orgB += 1
        elif org =='AAA-03':
            orgC += 1
        else:
            orgD += 1

    orgPeople = {}
    orgPeople['AAA-A'] = leaders
    orgPeople['AAA-O'] = orgoffice
    orgPeople['AAA-1'] = orgA
    orgPeople['AAA-2'] = orgB
    orgPeople['AAA-3'] = orgC
    orgPeople['AAA-4'] = orgD

    # plt.bar(orgPeople.keys(),orgPeople.values())
    # plt.bar(list(orgPeople.keys()),list(orgPeople.values()))
    # plt.show()

    orgSum = [leaders-1,orgoffice+leaders-1,orgA+orgoffice+leaders-1,orgB+orgA+leaders-1,orgC+orgB+orgA+leaders-1,orgD+orgC+orgB+orgA+leaders-1]
    print(orgPeople)

    # 绘制各部门总工时/加班工时/出差工时
    arrays = [arrayall, array100h]
    for array in arrays:
        avgData = []
        # AAA部门
        arrayAAA = array[:orgSum[0] + 1]
        meanA = arrayAAA.mean()
        avgData.append(meanA)
        # AAA OFFICE
        arrayAAA00 = array[orgSum[0]+1:orgSum[1] + 1]
        print(len(arrayAAA00))
        meanA0 = arrayAAA00.mean()
        avgData.append(meanA0)
        # AAA-001部门
        arrayAAA01 = array[orgSum[1] + 1:orgSum[2] + 1]
        meanA1 = arrayAAA01.mean()
        avgData.append(meanA1)
        # AAA-002部门
        arrayAAA02 = array[orgSum[2] + 1:orgSum[3] + 1]
        meanA2 = arrayAAA02.mean()
        avgData.append(meanA2)
        # AAA-003部门
        arrayAAA03 = array[orgSum[3] + 1:orgSum[4] + 1]
        meanA3 = arrayAAA03.mean()
        avgData.append(meanA3)
        # AAA-004部门
        arrayAAA04 = array[orgSum[4] + 1:]
        meanA4 = arrayAAA04.mean()
        avgData.append(meanA4)
        # plt.plot(orgSum,avgData)
        plt.bar(list(orgPeople.keys()), avgData)
        # plt.bar(list(range(len(avgData))), avgData, tick_label=list(range(len(avgData))))

    plt.show()






