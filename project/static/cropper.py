from PIL import Image, ImageDraw, ImageFont
from os import listdir
from os.path import isfile, join

mypath = 'project/static/thumbnails/'

img_files = [f for f in listdir(mypath) if isfile(join(mypath, f))]

print(img_files)


for i in img_files:
    image = Image.open(mypath + i)
    cropper = image.crop((1200, 935, 1575, 1090))
    width, height = cropper.size
    cropper = cropper.resize(((width*3), (height)*3), Image.ANTIALIAS)
    imageName = "project/static/geo/"+i
    cropper.save(imageName)
