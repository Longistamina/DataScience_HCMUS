dic_EngVn = {'one':'một', 'two':'hai', 'three':'ba'}
print()

k1 = dic_EngVn.items() #Trả về một tham chiếu đến danh sách các bộ tuple (key,value) của dictionary
                       #dict_items([('one', 'một'), ('two', 'hai'), ('three', 'ba')])

lstK1 = list(dic_EngVn.items()) #Như trên nhưng trả về dưới dạng list
                                #[('one', 'một'), ('two', 'hai'), ('three', 'ba')]
k2 = dic_EngVn.keys()
k3 = dic_EngVn.values()

#Không thể  duyệt trực tiếp trên dictionary như list và tuple được
#Thay vào đó phải dùng .items(), .keys() hoặc .values() để  trả về các tham chiếu rồi mới duyệt được
for key,value in dic_EngVn.items():
    print(f'{key} - {value}')

for key in dic_EngVn.keys():
    print(key)

for value in dic_EngVn.values():
    print(value)

