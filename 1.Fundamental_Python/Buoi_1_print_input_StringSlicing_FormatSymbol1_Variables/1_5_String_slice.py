name="Lê Anh Thư"
l=len(name)
ktdau=name[0] #---> L
kt4=name[3] #---> A

ktcuoi=name[-1] #---> ư
name[l-1] #--->ư
#Python đặt 0 là index cho vị trí đầu tiên

ho=name[0:2] #index kết thúc là 2, chỉ kết thúc chứ không bao gồm
ho2=name[:2]
tenlot=name[3:6]
ten=name[7:]

strSo="123456789"
strLe=strSo[0::2] #Từ đầu đến cuối, bước nhảy là 2
strChan=strSo[1::2]

print("-"*50) #print dấu - 50 lần
print()
