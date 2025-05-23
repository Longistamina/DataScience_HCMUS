from PIL import Image
from rembg import remove
import os

#-------------------------------------------#
def remove_background(file_name,in_dir,out_dir):
    
    file_path = in_dir+file_name #return the path leading to file
                                               #Disk:\...path...\file.extension
                                         
    
    file_head = os.path.splitext(file_name)[0] #get the head of the image file name
    file_tail = os.path.splitext(file_name)[-1] #get the extension of image files
    
    
    #Construct output path for file file
    nobg_file_name = file_head+'_nobg'+'.png'
    outpath = out_dir+nobg_file_name
    
    input = Image.open(file_path) #Must be this Disk:\...path...\file.extension
    
    if file_tail == '.png':
        output = remove(input)
        output.save(outpath)
        print(f'Background of image {file_name} has been removed into {nobg_file_name} !!')
    
    elif (file_tail == '.jpg' or '.jpeg'):   
        rgb_input = input.convert("RGB")
        output = remove(rgb_input)
        output.save(outpath)
        print(f'Background of image {file_name} has been removed into {nobg_file_name} !!')
    
    else: print('No image files found!!!')

#------------------------------------#
have_bg_path = "C:/Users/Admin/Pictures/have_bg/" 
no_bg_path = "C:/Users/Admin/Pictures/no_bg/"
image_name = 'dog.jpg'

remove_background(image_name, have_bg_path, no_bg_path)