from PIL import Image, ImageEnhance
from numpy import asarray
import numpy as np

name = input()
im = Image.open(str(name)).convert("L")

w, h = im.size
if(w>h):
    cut = (w-h)//2
    img = im.crop((cut,h,(w-cut),0))
elif(w<h):
    cut = (h-w)//2
    img = im.crop((0, cut ,w,(h-cut)))
else:
    img=im

img.save('crop.jpg')

Max = (28,28)
img.thumbnail(Max)
img.save('Small.jpg')

image = Image.open("Small.jpg")
data = asarray(image)
leng, bre = (data.shape)

arr =np.array([])

for x in range(leng):
    for y in range(bre):
        arr = np.append(arr,data[x][y])
print(len(arr))
print(arr)

np.savetxt('array.csv',[arr],delimiter=',', fmt='%d')