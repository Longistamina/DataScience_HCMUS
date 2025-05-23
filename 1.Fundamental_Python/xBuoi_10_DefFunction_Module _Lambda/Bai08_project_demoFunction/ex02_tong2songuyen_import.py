import ex01_func_arg as toan
print()
print("CHƯƠNG TRÌNH TÍNH TỔNG HAI SỐ  NGUYÊN".center(50))
print('-'*50)
A = int(input('Nhập số  nguyên A: '))
B = int(input('Nhập số  nguyên B: '))

if __name__ == '__main__':
    tongAB = toan.tinh_tong(a=A,b=B)
    print('Tổng hai số A và B =',tongAB)
    print()