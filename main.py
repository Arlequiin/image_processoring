from PIL import Image
import os
os.chdir("img")
images=os.listdir()
images.remove("duck.jpg")
images.remove("tirex.jpg")
images_data=[]
output=[]
for image in images:
    images_data.append(Image.open(image).convert('RGB').load())
os.chdir("..")
width,height=Image.open('img/'+images[0]).size
out=Image.new("RGB", (width,height),'red')
pixels=out.load()
print("Processoring in progress, please wait...")
for y in range(height):
    for x in range(width):
        l1=[images_data[i][x,y][0] for i in range(len(images_data))]
        l1.sort()
        l1=l1[len(l1)//2]
        l2=[images_data[i][x,y][1] for i in range(len(images_data))]
        l2.sort()
        l2=l2[len(l2)//2]
        l3=[images_data[i][x,y][2] for i in range(len(images_data))]
        l3.sort()
        l3=l3[len(l3)//2]
        pixels[x,y]=(l1,l2,l3)
print("Execution done!")
out.save("output.jpg")
out.show()