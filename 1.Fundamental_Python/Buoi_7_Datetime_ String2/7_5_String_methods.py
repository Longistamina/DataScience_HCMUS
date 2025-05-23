#%%
s1 = '  Trung tÂm tiN học   '
k1 = s1.capitalize() #=> '  Trung tâm tin học   ' viết hoa chữ cái đầu của từ đầu tiên
k2 = s1.upper() #=> '  TRUNG TÂM TIN HỌC   '      viết hoa toàn bộ
k3 = s1.lower() #=> '  trung tâm tin học   '      viết thường toàn bộ
k4 = s1.title() #=> '  Trung Tâm Tin Học   '      viết hoa chữ cái đầu mỗi từ
k6 = s1.strip() #=> 'Trung tÂm tiN học'           cắt bỏ khoảng trắng ở hai đầu chuỗi
print()

s2 = ',20 30,'
k7 = s2.strip(',') #=> '20 30' loại bỏ dấu phẩy ở hai đầu chuỗi
#------------------------------------------------------------------------------------------------#
#%%
baitho = '''
Thân em vừa trắng lại vừa tròn
Bảy nổi ba chìm với nước non
Rắn nát mặc dầu tay kẻ nặn
Mà em vẫn giữ tấm lòng son
'''
print(baitho)
print(baitho.count('m'))
print(baitho.lower().count('m'))
#method count() có phân biệt chữ hoa với chữ thường, nên hai kết quả .count('m') và .lower().count('m') khác nhau

tieude = 'BÁNH TRÔI NƯỚC'
print(tieude.count('N',2,10)) #Đếm xem có bao nhiêu chữ N từ vị trí số  3 đến 9 của chuỗi

#---------------FIND AND REPLACE--------------#
#%%
str = 'Hoa Chanh nở giữa vườn Chanh'
strTim = 'Chanh'
strThaythe = 'Cam'
strNew = str.replace(strTim,strThaythe)
strNew2 = str.replace(strTim,strThaythe,1) #Chỉ thay thế  một lần ở strTim đầu tiên bắt gặp
print()

#------------------------------------------------#
#%%
hoten = 'Trần Thị Anh Thư'
i = hoten.find(' ') #Tìm ký tự ' ' đầu tiên từ trái qua rồi trả về index của nó
j = hoten.find(' ',i+1) #Tìm ký tự ' ' bắt đầu từ vị trí i+1 trở đi
k = hoten.rfind(' ') #Tìm ký tự ' ' theo hướng từ phải sang
print()

# %%
sdt = '0903123456'
k1 = sdt.isdigit() #=> True / Nếu có dính một ký tự alphabetic vào thì sẽ thành False
k2 = sdt.isnumeric() #=> True / Nếu có dính một ký tự alphabetic vào thì sẽ thành False

tien = '1500VND'
id = 'ASDK'
k3 = tien.isalpha() #=> F
k4 = id.isalpha() #=> T / Nếu có dính một ký tự numeric vào thì sẽ thành False
k5 = tien.isalnum() #=> F
k6 = id.isupper() #=> T
k7 = id.islower()#=> F

#%%
#------------_format()---------------#
soTien = 1200000000.453
str_tien1 = '{:,} VND'.format(soTien) # '1,200,000,000.453 VND'
str_tien2 = '{:,.2f} VND'.format(soTien) # '1,200,000,000.45 VND'
# .format() giúp chuyển dữ liệu từ số sang chuỗi 
print()

#%%
#----------------Căn lề --------------------#
strD = 'Abc'
str1 = strD.center(20)     #'        Abc         '
str2 = strD.center(20,'*') #'********Abc*********'
str3 = strD.rjust(20) #Căn lề  phải với khoảng cách 20 ký tự
str4 = strD.ljust(20) #Căn lề  trái với khoảng cách 20 ký tự