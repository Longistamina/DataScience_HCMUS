print()
lstN = [25,428,33,121,63]

#Duyệt qua các phần tử  trong list:
tich = 1
for item in lstN:
    tich *= item
print('lstN =',lstN)
print('Tích các phần tử  trong lstN =',tich)

#Nếu quan tâm đến index của list
print()
i = 0
for item in lstN:
    print(i,':'.lstrip(),item)
    i+=1

print()
i = 0
for i in range(len(lstN)):       #len(lstN) = 5, nên câu lệnh sẽ duyệt i đi từ 0 đến 4 
    print(i,':'.lstrip(),lstN[i])