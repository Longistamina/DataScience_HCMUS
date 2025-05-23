print()
print('-'*131)
print(' '*50,'BẢNG CỬU CHƯƠNG',' '*60)
print('-'*131)
i = 1
bcc = ''
while i <= 10:
    n = 1
    while n <= 9:
        bcc += f'{n:2}x {i:2} = {n*i:2}   ' #Độ rộng của chữ là 2
        n += 1
    i += 1
    bcc +='\n'
print(bcc)