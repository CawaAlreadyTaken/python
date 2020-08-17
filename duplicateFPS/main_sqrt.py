import cv2
import os
from math import sqrt
from pathlib import Path
from progress.bar import IncrementalBar

def takeVideo():
    Path("output_videos").mkdir(exist_ok=True)
    while True:
        try:
            path = input("# Insert file name (it has to be in this folder): \n- ")
            vidcap = cv2.VideoCapture(path)
            if not vidcap.isOpened():
                raise NameError('File not found')
            break
        except KeyboardInterrupt:
            exit()
    return path, vidcap

def main():
    path, vidcap = takeVideo()
    success, image0 = vidcap.read()
    rows, cols, nslice = image0.shape
    frames = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
    frameRate = (vidcap.get(cv2.CAP_PROP_FPS))
    print("# Original FrameRate: ", frameRate)
    print("# Aborting with ctrl-C may cause some issues. If it happens, just close the terminal. Btw, i suggest not to abort.")
    bar = IncrementalBar('Doing stuff...', max=frames)
    path = os.path.split(path)
    path = path[1].split('.')
    path_out = "output_videos/"
    for i in range(len(path)-1):
        path_out += path[i]
    path_out += "_out."
    path_out += path[len(path)-1]
    out = cv2.VideoWriter(path_out,cv2.VideoWriter_fourcc(*'DIVX'), frameRate*2, (cols, rows))
    for _ in range(frames - 1):
        success, image1 = vidcap.read()
        imageI = image0
        bar.next()
        for i in range(rows):
            for j in range(cols):
                R = sqrt((image0[i][j][2]**2 + image1[i][j][2]**2)/2)
                G = sqrt((image0[i][j][1]**2 + image1[i][j][1]**2)/2)
                B = sqrt((image0[i][j][0]**2 + image1[i][j][0]**2)/2)
                imageI[i, j] = (int(B), int(G), int(R))
        out.write(cv2.UMat(image0))
        out.write(cv2.UMat(imageI))
        image0 = image1
    bar.next()
    bar.finish()
    out.release()

if __name__ == "__main__":
    main()
