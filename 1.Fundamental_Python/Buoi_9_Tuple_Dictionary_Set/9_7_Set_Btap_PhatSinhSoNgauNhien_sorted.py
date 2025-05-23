'''
Cho phát sinh một danh sách set chứa 20 số  ngẫu nhiên từ 1 đến 100
(không lấy trùng lặp)
print ra màn hình
xếp tăng dần và print
'''
print()
import random

#Theo kiểu set:
setSN = set()
while len(setSN) < 20:
    valueAdd = random.randint(1,100) #Không cần kiểm tra element có trùng hay không vì set{} sẽ tự làm
    setSN.add(valueAdd)

print(setSN)
print('Tăng dần:',sorted(setSN))
print()

#Theo kiểu list
listSN = []
i = 1

while len(listSN) < 20:
    valueAdd = random.randint(1,100)
    if (valueAdd in listSN) == False: #Với list thì phải kiểm tra element có trùng hay không
        listSN.append(valueAdd)
    else: continue

print(listSN)
listSN.sort()
print(f'Tăng dần: {listSN}')
print()