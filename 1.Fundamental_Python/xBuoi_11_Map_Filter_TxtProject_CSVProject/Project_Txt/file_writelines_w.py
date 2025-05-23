'''
writelines: Ghi nội dung dưới dạng list vào file
nếu mode open() là 'w' thì nội dung mới sẽ ghi đè lên nội dung cũ (overwrite)
'''
print()
txtName = '/home/long/Documents/Data Science/1. Fundamental Python/File code python/Buoi 11: Map + Filter + Txt project/Project Txt/DuLieu-txt'

tentaptin = input('Mời nhập tên tập tin muốn ghi: ') #DanhSachKhachHang
lstND =[
    'Tâm: 20000\n',
    'Lý: 15000\n',
    'Hoà: 9000\n'
]

#Mở tập tin để  viết 'w'
with open(f'{txtName}/{tentaptin}.txt','w',encoding='utf-8') as f:

    f.writelines(lstND) #Nếu tên file có tồn tại, thì nội dung mới sẽ ghi đè lên nội dung cũ trong file đó
                   #Nếu tên file chưa tồn tại thì nó sẽ tạo file mới với tên đó, rồi ghi nội dung vào
f.close()

print('Ghi thành công')
'''
Tâm: 20000
Lý: 15000
Hoà: 9000
'''