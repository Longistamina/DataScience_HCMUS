'''
Cho nhập họ tên, xuất ra họ, tên và tên lót
'''
hoten = input('\nMời bạn nhập họ và tên: ')
i = hoten.find(' ')
j = hoten.rfind(' ')
ho = hoten[:i]
ten = hoten[j+1:]
tenlot = hoten[i+1:j]
print('\nHọ:',ho.rjust(20))
print('Tên lót:',tenlot.rjust(15))
print('Tên:',ten.rjust(19))
