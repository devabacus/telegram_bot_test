from datetime import date
import os
import re
import pathlib


def get_imgs_path(base_path):
    today = date.today().strftime("%d-%m-%Y")
    teleg_path = pathlib.Path(base_path).joinpath(today).joinpath('telegram')
    return teleg_path


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

# for img in get_listOfDirs(teleg_path):
#     brand = get_brand(teleg_path, img)
#     print(brand)


