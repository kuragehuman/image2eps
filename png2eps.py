# -*- coding: utf-8
import glob
import cv2
import os
from PIL import Image

for inputfile in glob.glob("./input/*.png"):
    im = Image.open(inputfile)
#    im = cv2.imread(inputfile)
    name,ext = os.path.splitext(os.path.basename(inputfile))
    outputfile = "./output/" + name + ".eps"
    im.save(outputfile)
#    cv2.imwrite(outputfile, im)
    print(outputfile)
