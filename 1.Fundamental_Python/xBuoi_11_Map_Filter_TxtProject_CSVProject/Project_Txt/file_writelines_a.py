'''
writelines: Ghi nội dung dưới dạng list vào file
nếu mode trong open() là 'a' tức append, thì nội dung mới được thêm vào sau nd cũ, không ghi đè lên
nếu tập tin chưa tồn tại thì cũng tạo tập tin mới, rồi ghi nội dung mới vào
'''
print()
txtName = '/home/long/Documents/Data Science/1. Fundamental Python/File code python/Buoi 11: Map + Filter + Txt project/Project Txt/DuLieu-txt'

tentaptin = input('Mời nhập tên tập tin muốn ghi: ') #DanhSachKhachHang
lstND =[
    'Bình: 20000\n',
    'Anh: 15000\n',
    'Minh: 9000\n'
]

#Mở tập tin để  viết 'a' để thêm nội dung mới vào nội dung cũ
with open(f'{txtName}/{tentaptin}.txt','a',encoding='utf-8') as f:

    f.writelines(lstND) #Nếu tên file có tồn tại, thì nội dung mới sẽ ghi đè lên nội dung cũ trong file đó
                   #Nếu tên file chưa tồn tại thì nó sẽ tạo file mới với tên đó, rồi ghi nội dung vào
f.close()

print('Ghi thành công')

'''
Tâm: 20000
Lý: 15000
Hoà: 9000
Bình: 20000  (do append vào)
Anh: 15000   (do append vào)
Minh: 9000   (do append vào)
'''