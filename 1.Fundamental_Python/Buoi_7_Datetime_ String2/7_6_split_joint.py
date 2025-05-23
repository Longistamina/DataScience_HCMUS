#-------------_SPLIT------------------#
#%%
hoten = 'Arthur Conan Doyle'
str1 = hoten.split() # => ['Arthur', 'Conan', 'Doyle']

so = '12,13,14,15,16'
str2 = so.split(',') # => ['12', '13', '14', '15', '16']
str3 = so.split(',',maxsplit=2) # => ['12', '13', '14,15,16']
print()
#Kết quả split trả về ở dạng list, các phần tử  ở dạng string

#--------------JOIN-----------------#
#%%
lst = ['A','B','C','D','E']
str1 = ''.join(lst)   # 'ABCDE'
str2 = ' '.join(lst)  # 'A B C D E'
str3 = ','.join(lst)  # 'A,B,C,D,E'
print()