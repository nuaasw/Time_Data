from csv import DictReader

data_rdr = DictReader(open('./test.csv','r'))
data_rows = [d for d in data_rdr]
print(data_rows[1])
print('Test')