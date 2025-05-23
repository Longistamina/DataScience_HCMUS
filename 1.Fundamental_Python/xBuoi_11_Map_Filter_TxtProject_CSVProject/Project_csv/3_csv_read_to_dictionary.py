'''
read to dictionary
'''
print()
import csv #Phải import module csv để  thao tác với csv files
pathName = '/home/long/Documents/Data Science/1. Fundamental Python/File code python/Buoi 11: Map + Filter + Txt project/Project csv/DuLieu-csv'

dictNV = {}
with open(f'{pathName}/dsnv.csv','r',encoding='utf-8-sig') as f:
    for row in csv.reader(f):
        ms = row[0]
        thongtin = row[1:]
        dictNV[ms] = thongtin
print(dictNV)
print('--kết thúc demo--')