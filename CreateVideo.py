import os
import cv2


path = "C:/Users/Lenovo/Desktop/Python Whitehat/Project-105/Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in [ '.gif','.png','.jpg','.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)

img = cv2.imread(images[0])
print(img.shape)
outputVid = cv2.VideoWriter('photos.mp4',cv2.VideoWriter_fourcc(*'DIVX'),0.8,(300,500))

for i in range(0,count-1):
    print(i)
    frame = cv2.imread(images[i])
    #print(frame)
    outputVid.write(frame)
    print("done")
