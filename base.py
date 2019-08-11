# import matplotlib.pyplot as plt
# import numpy
#
# datas = [1,4,9,16,25]
# print(datas)
# plt.plot(list(range(1,6)),datas)
# plt.show()
# print('End')

import numpy
import csv

print('Hello Test!')

filename = 'C:/Users/Administrator/PycharmProjects/dataanalysis/data/test.csv'
with open(filename,'r',encoding='UTF-8') as f:
    reader = csv.reader(f)
    head_row = next(reader)
    ivalue = {}
    for index,value in enumerate(head_row):
        ivalue[index] = value
    print(ivalue)