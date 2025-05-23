'''
read to list
'''
print()
import csv #Phải import module csv để  thao tác với csv files
pathName = '/home/long/Documents/Data Science/1. Fundamental Python/File code python/Buoi 11: Map + Filter + Txt project/Project csv/DuLieu-csv'

lstDSHS = []
with open(f'{pathName}/dshs.csv','r',encoding='utf-8-sig') as f:
    for row in csv.reader(f):
        row[3] = float(row[3]) #Chuyển điểm từ str sang float rồi mới append sau vào list DSHS sau
        lstDSHS.append(row)
print(lstDSHS)
print('--kết thúc demo--')
