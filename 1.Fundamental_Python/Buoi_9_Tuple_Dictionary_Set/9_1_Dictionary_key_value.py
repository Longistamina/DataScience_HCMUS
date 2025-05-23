''' 
Dictionary {key:value} là một tập hợp nhiều phần tử.
Mỗi phần tử là một bộ key:value
Key là duy nhất, không được trùng nhau. Key có thể  là string, number hoặc tuple
Còn value tương ứng với key thì có thể  trùng nhau giữa các key.
'''
print()

#Khởi tạo dictionary:
dicR1 = {}
dicR2 = dict()

dic_animals = {1:'chien', 2:'chat', 3:'lapin', 4:'ours', 5:'loup'}

print(dic_animals)     # {1: 'chien', 2: 'chat', 3: 'lapin', 4: 'ours', 5: 'loup'}
print(dic_animals[1])  # chien

dic_EngVn = {'one':'một', 'two':'hai', 'three':'ba'}
#print(dic_EngVn[1])     # Error
print(dic_EngVn['two']) # 'hai

dic_complicated = {
    'x':[2,3], #value của key 'x' là một list
    'y':(4,1), #value của key 'y' là một tuple
    'z': {'s':9, 'p':20} #value của key 'z' là một dictionary
}
print(dic_complicated['z']['p']) # 20

#dictionary.get()
cat = dic_animals.get(2) #Get value có key = 2 rồi gán cho biến cat

#Cập nhật dictionary
dic_numbers = {1:'một', 2:'hai', 3:'ba'}
dic_numbers[4] = 'bốn' #thêm key:value mới vào             {1:'một', 2:'hai', 3:'ba', 4:'bốn'}
dic_numbers[4] = 'tư'  #điều chỉnh value của key tương ứng {1:'một', 2:'hai', 3:'ba', 4:'tư'}

dic_numbers.update(dic_EngVn) # {{1: 'một', 2: 'hai', 3: 'ba', 4: 'tư', 'one': 'một', 'two': 'hai', 'three': 'ba'}
                              # .update() giống với extend() của list
3 in dic_numbers #True
30 in dic_numbers #False

len(dic_numbers) # 3
del(dic_numbers[3]) #xoá phần tử có key và value tương ứng ra khỏi dict
dic_numbers.clear() #xoá mọi phần tử, trả về  dict trống
del(dic_numbers)    #xoá hoàn toàn dic_numbers ra khỏi bộ nhớ

s = str(dic_animals) #CHuyển dict thành chuỗi "{1: 'chien', 2: 'chat', 3: 'lapin', 4: 'ours', 5: 'loup'}"
copy = dic_animals.copy() #tạo dict bản sao với id khác

print()

#Tạo lập key của dict từ list
listN = [1,2,3,4]
dict_stt = dict.fromkeys(listN) #Lấy các phần tử  trong listN để  làm key cho dict_stt, value tạm thời = None
                                # {1: None, 2: None, 3: None, 4: None}
lstHanghoa = ['H01','H02','H03']
dict_hanghoa = dict.fromkeys(lstHanghoa)    #{'H01': None, 'H02': None, 'H03': None}
dict_hanghoa0 = dict.fromkeys(lstHanghoa,0) #{'H01': 0, 'H02': 0, 'H03': 0}

#Trả về  danh sách keys:
dictKeys = dic_animals.keys()        #dict_keys([1, 2, 3, 4, 5])
lst_keys = list(dic_animals.keys())  #[1, 2, 3, 4, 5]

#Trả về  danh sách values:
dictValues = dic_animals.values()        #dict_values(['chien', 'chat', 'lapin', 'ours', 'loup'])
lst_values = list(dic_animals.values())  #['chien', 'chat', 'lapin', 'ours', 'loup']
print()