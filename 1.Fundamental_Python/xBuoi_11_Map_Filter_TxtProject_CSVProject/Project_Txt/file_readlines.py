'''
Đọc rồi trả về dưới dạng list, mỗi dòng là một phần tử của list
'''
print()
txtName = '/home/long/Documents/Data Science/1. Fundamental Python/File code python/Buoi 11: Map + Filter + Txt project/Project Txt/DuLieu-txt/ConGapNhau.txt'

#Mở tập tin để đọc 'r'
f = open(txtName,'r',encoding='utf-8') #vì có tiếng Việt có dấu nên chọn utf-8

lstND = f.readlines() #Đọc nội dung trong file, trả về  dưới dạng list, mỗi dòng là một element của list

f.close() #Đóng tập tin lại

print(lstND)
#['CÒN GẶP NHAU\n', '\n', 'Còn gặp nhau thì hãy cứ vui\n', 'Chuyện đời như nước chảy hoa trôi\n', 
#'Lợi danh như bóng mây chìm nổi\n', 'Chỉ có tình thương để lại đời.\n', '\n', 
#'Còn gặp nhau thì hãy cứ thương\n', 'Tình người muôn thuở vẫn còn vương\n', 
#'Chắt chiu một chút tình thương ấy\n', 'Gửi khắp muôn phương vạn nẻo đường.\n', 
#'\n', 'Nhà thơ: Tôn Nữ Hỷ Khương']