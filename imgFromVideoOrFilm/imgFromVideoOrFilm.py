import cv2
import os
from PIL import Image
from math import sqrt
from pathlib import Path
from progress.bar import IncrementalBar

def takeRate():
    Rate = int(input("# I will take a frame every X frames. Choose X: \n- "))
    if ((frameTot/Rate)*cols*rows > 160000000):
        confirm = input("# With this rate, you may experience some laggy behaviour (suggested rate for this video: " + str(int((frameTot*cols*rows)/160000000)+1) + "). Are you sure? [y/n]: ")
        if (confirm=="n" or confirm=="N"):
            return takeRate()
        elif (confirm=="y" or confirm=="Y"):
            return Rate
        else:
            exit()
    else:
        return Rate

def average(new):
    for i in range(rows):
        for j in range(cols):
            mediaR = 0
            mediaG = 0
            mediaB = 0
            for k in range(len(cache[i][j])):
                mediaR+=cache[i][j][k][2]
                mediaG+=cache[i][j][k][1]
                mediaB+=cache[i][j][k][0]
            mediaR/=len(cache[i][j])
            mediaG/=len(cache[i][j])
            mediaB/=len(cache[i][j])
            new[j, i] = (int(mediaR), int(mediaG), int(mediaB), 1)

def sqrt_average(new):
    for i in range(rows):
        for j in range(cols):
            mediaR = 0
            mediaG = 0
            mediaB = 0
            for k in range(len(cache[i][j])):
                mediaR+=cache[i][j][k][2]**2
                mediaG+=cache[i][j][k][1]**2
                mediaB+=cache[i][j][k][0]**2
            mediaR=sqrt(mediaR/len(cache[i][j]))
            mediaG=sqrt(mediaG/len(cache[i][j]))
            mediaB=sqrt(mediaB/len(cache[i][j]))
            new[j, i] = (int(mediaR), int(mediaG), int(mediaB), 1)

def mode():
    root = input("# Normal mode / Root Mean Square mode ? [n/r]: ")
    if ((root != 'n') and (root != 'N') and (root != 'r') and (root != 'R')):
        print("# Answer just n or r.")
        root = mode()
    return (root == 'r' or root == 'R')


Path("images").mkdir(exist_ok=True)
path = input("# Insert file name (it has to be in this folder): \n- ")
vidcap = cv2.VideoCapture(path)

success,image = vidcap.read()
rows, cols, nslice = image.shape

root = mode()

cache = []
for i in range(rows):
    cache.append([])

    for j in range(cols):
        cache[i].append([])

count = 0
frameTot = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
print("# Width: "+str(cols)+", Height: "+str(rows))
rate = int(takeRate())

#print("# Collecting all the pixels value..")
bar = IncrementalBar('# Collecting pixels values..', max = frameTot/rate+1)

while success:
    if (count%rate==0):
        for i in range(rows):
            for j in range(cols):
                cache[i][j].append(image[i,j])
        bar.next()
    success,image = vidcap.read()
    count += 1 

bar.finish()

frames = int(count/rate)
print("# Frames taken:"+str(frames+1))
print("# Creating the image..")
print("# This may take some time.")

new = Image.new('RGB', (cols, rows), color = 'white')
nuova = new.load()

if (root):
    nuova = sqrt_average(nuova)
else:
    nuova = average(nuova)

path = os.path.split(path)
path = path[1].split('.')
path_out = "images/"
for i in range(len(path)-1):
    path_out += path[i]
path_out += ".png"

new.save(path_out)

