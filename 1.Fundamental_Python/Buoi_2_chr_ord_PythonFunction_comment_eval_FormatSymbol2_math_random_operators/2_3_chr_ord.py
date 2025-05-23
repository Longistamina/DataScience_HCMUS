#chr() trả về ký tự với số thứ tự tương đương trong bộ mã ASCII
#ord() trả về số thứ tự của ký tự tương đương trong bộ mã ASCCI
#Vào mục "Tài liệu tham khảo" để dò bảng ASCII code

chr(97) #---> 'a'
chr(65) #---> 'A'
ord('A') #---> 65
ord('a') #----> 97

chr(178) #----> ký hiệu bình phương: ²

print('X'+chr(178)) #----> X²
print(f'X{chr(178)}') #----> X²

# ptb2=f'aX{chr(178)}+bX+c=0'
# print(ptb2)

a=eval(input('Nhập hệ số  A: '))
b=eval(input('Nhập hệ số  B: '))
c=eval(input('Nhập hệ số  C: '))
ptb2=f'{a}X{chr(178)} + {b}X +{c} = 0'
print(ptb2)