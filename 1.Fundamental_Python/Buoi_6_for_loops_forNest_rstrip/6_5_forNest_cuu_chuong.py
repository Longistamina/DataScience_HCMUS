print('-'*116)
print('BANG CUU CHUONG'.center(116)) #Căn giữa trong khoảng 116 ký tự
print('-'*116)

#%%
bcc = ''
for n in range(1,11,1):
    for i in range (2,10,1):
        bcc += f'{i:2} x {n:2} = {i*n:2}   '
    bcc +='\n'
print(bcc)

#%%
for n in range(1,11,1):
    for i in range (2,10,1):
        print(f'{i:2} x {n:2} = {i*n:2}',end='   ')
    print()
# %%
