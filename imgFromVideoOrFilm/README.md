# imgFromVideoOrFilm

Not a good name for a python project, i know and i am sorry.

This script will take a video as an input and will produce an image. Every pixel of the output image will be the average of the values of the pixels during the whole video. 

Two modes are available: arithmetic mean and root mean square.

Mind that the video file **MUST** be inside the same folder as the script, and you will need to indicate the full name (with `."extension"` aswell).

An `images` folder for the output images will be created if not existant yet; the 'images' folder provided has some examples of output inside.

Run it with:

```
python imgFromVideoOrFilm.py
```
