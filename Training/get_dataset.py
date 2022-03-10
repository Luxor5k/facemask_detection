from ast import Try

from sympy import interpolate
import cv2
import os

def load(images_path):
    images=[]
    for img in os.listdir(images_path):
        img_path = os.path.join(images_path,img)
        try:
            img = cv2.imread(img_path)
            img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img= cv2.resize(img, (50,50), interpolation=cv2.INTER_CUBIC)
            images.append(img)
        except Exception as e:
            print(f"Cannot load image {img_path}")
    print(f"Loaded {len(images)} images from path {images_path}")
    return images
