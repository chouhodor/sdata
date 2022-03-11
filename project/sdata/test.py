from os import listdir
from os.path import isfile, join
import os

#mypath = "C:\\stekapps\\project\\snake_data\\static\\snake_img\\1"

mypath = 'project/static/snake_img/1'

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

print(onlyfiles)

'''
cwd = os.getcwd()

print(cwd)
'''