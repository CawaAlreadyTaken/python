import cv2
import numpy as np
import os
from numba import njit
from numba.typed import List
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

@njit
def njitProcess(pairs, new_frames, rows, cols):
    for f in range(len(pairs)):
        for i in range(rows):
            for j in range(cols):
                R = (int(pairs[f][0][i][j][2]) + int(pairs[f][1][i][j][2]))//2
                G = (int(pairs[f][0][i][j][1]) + int(pairs[f][1][i][j][1]))//2
                B = (int(pairs[f][0][i][j][0]) + int(pairs[f][1][i][j][0]))//2
                new_frames[f][i, j] = (int(B), int(G), int(R))
    return new_frames

def main():
    path, vidcap = takeVideo()
    trash, image0 = vidcap.read()
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
    iterator = 1
    while (iterator < frames - 1):
        pairs = []
        new_frames = []
        u = 0 
        for k in range(50):
            success, image1 = vidcap.read()
            if (not success):
                break
            pairs.append((image0, image1))
            new_frames.append(image0)
            iterator+=1
            u+=1
            image0 = image1
        
        for k in range(u):
            bar.next()
    
        typed_pairs = List()
        typed_new_frames = List()
        [typed_pairs.append(x) for x in pairs]
        [typed_new_frames.append(x) for x in new_frames]
        new_frames = njitProcess(typed_pairs, typed_new_frames, rows, cols)
        for k in range(u):
            out.write(pairs[k][0])
            out.write(new_frames[k])

    bar.next()
    bar.finish()
    out.release()

if __name__ == "__main__":
    main()
