'''
Ghi nội dung lên một tập tin có tên tương ứng.
Nếu tên tập tin chưa tồn tại thì tạo mới rồi ghi
'''
print()
txtName = '/home/long/Documents/Data Science/1. Fundamental Python/File code python/Buoi 11: Map + Filter + Txt project/Project Txt/DuLieu-txt'

tentaptin = input('Mời nhập tên tập tin muốn ghi: ') #VB01
strND = input('Mời nhập nội dung muốn ghi: ')

#Mở tập tin để  viết 'w'
with open(f'{txtName}/{tentaptin}.txt','w',encoding='utf-8') as f:

    f.write(strND) #Nếu tên file có tồn tại, thì nội dung mới sẽ ghi đè lên nội dung cũ trong file đó
                   #Nếu tên file chưa tồn tại thì nó sẽ tạo file mới với tên đó, rồi ghi nội dung vào
f.close()

print('Ghi thành công')