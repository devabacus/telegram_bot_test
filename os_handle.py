import os
import re
import pathlib

# p.parents[0].joinpath()
# print(p.joinpath('ivan.img'))

# lstDirs = os.listdir(base_path)
def get_listOfDirs(base_path):
    return os.listdir(base_path)

def get_img_path(teleg_path, img_name):
    return teleg_path.joinpath(img_name)

    
def get_brand_name(path):
    with open(path, encoding = 'utf8') as f:
        r = f.read().split('\n')[3]
        return r

def get_brand(teleg_path, img_name):
    _num = img_name.split('.')[0]
    txt_path = teleg_path.parents[0].\
                            joinpath(_num).\
                            joinpath(_num + '.txt') 
    brand = get_brand_name(txt_path).upper().replace(' ', '')
    return brand

base_path = "D:\Macys\\18-01-2022\\telegram\\"
teleg_path = pathlib.Path(base_path)

# for img in get_listOfDirs(base_path):
#     brand = get_brand(teleg_path, img)
    # print(brand)
        

# print(get_img_path('1.jpg'))
# print(get_listOfDirs(base_path))

# for img in lstDirs:
    

                            
                            
#     print(img_path, txt_path)



# print(lstDirs)






# imgs = [i for i in lstDirs if r'*.jpg' in i]
# lst = [i for i in lstDirs if re.search(r'.*.jpg',i)]


