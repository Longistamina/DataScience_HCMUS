#-------------------------#
#%%
for char in 'LONG':
    print('Character: '+char)

#--------range([start=0],stop,[step=1])----------#
#%%
for i in range(10):
    print(i) #Dừng lại tại 9 chứ không đến 10

#%%
for i in range(1,11): #in từ 1 -> 10
    print(i)
# %%
d = 0
for i in range(1,101,2): #in số lẻ
    print(i,end=', ')
    d +=1
print(f'\nSố số lẻ là: {d}')
# %%
for i in range (10,0,-1):
    print(i) #in từ 10 9 8 7... 1