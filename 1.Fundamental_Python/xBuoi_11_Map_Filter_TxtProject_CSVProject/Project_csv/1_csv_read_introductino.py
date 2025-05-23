'''
csv là comma-separated values, là những file chứa dữ liệu được phân cắt từng cột bởi dấu phẩy

Rất tiện cho việc chuyển đổi qua lại với excel.
Thường khi muốn chuyển dữ liệu từ excel sang python để xử lý thì sẽ qua trung gian csv trước
ngượcc lại cũng tương tự
'''
print()
import csv #Phải import module csv để  thao tác với csv files
pathName = '/home/long/Documents/Data Science/1. Fundamental Python/File code python/Buoi 11: Map + Filter + Txt project/Project csv/DuLieu-csv'

with open(f'{pathName}/dshs.csv','r',encoding='utf-8-sig') as f:
    for row in csv.reader(f): #Đọc từng dòng, mỗi dòng là một list, elements của list con phân cắt bởi comma
        print(row)
print('--kết thúc demo 1--')
'''
['MS01', 'Trần Anh', 'Tuấn', '9.5']
['MS02', 'Lê Quốc', 'Anh', '9']
['MS03', 'Trần Anh', 'Bình', '6.5']
['MS04', 'Nguyễn Thúy', 'An', '7.5']
['MS05', 'Trần Anh', 'Thư', '5']
['MS06', 'Lý Thanh', 'Tâm', '3.5']
['MS07', 'Trần Lê Nhất', 'Hạnh', '9.5']
['MS08', 'Trần Bửu', 'Nguyên', '4']
['MS09', 'Lê Thanh', 'Tuấn', '8']
--kết thúc--
'''

with open(f'{pathName}/dshs.csv','r',encoding='utf-8-sig') as f:
    for row in csv.reader(f):
        ms = row[0]
        ho = row[1]
        ten = row[2]
        print(f'{ms}: {ho} {ten}')
print('--kết thúc demo 2--')
