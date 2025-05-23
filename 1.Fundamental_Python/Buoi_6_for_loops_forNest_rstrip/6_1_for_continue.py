'''
In số  lẻ từ 1 đến 100
'''

#----cách 1-------#
#%%
for i in range(1,101):
    if i%2 != 0: print(i)

#---cách 2: dùng continue-----#
# %%
for i in range (1,101):
    if i%2 == 0: continue #tiếp tục vòng lặp, không làm gì
    print(i)
# %%
