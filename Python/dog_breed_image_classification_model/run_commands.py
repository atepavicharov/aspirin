# %matplotlib inline
import matplotlib.pyplot as plt
import pickle
import numpy as np
from numpy import float64
import PIL.Image
import pandas as pd

# load TRAIN
train = pickle.load(open("train.p", "rb"))


# image_resize = 60
# nwidth = image_resize
# nheight = image_resize
#
# df_train = pd.read_csv('D:/Downloads/Classification Models/labels.csv')
#
# # nwidth x nheight = number of features because images are nwidth x nheight pixels
# s = (len(df_train['breed']), nwidth, nheight, 3)
# allImage = np.zeros(s)
#
# i = 0
# for f, breed in df_train.values:
#     image = PIL.Image.open('D:/Downloads/Classification Models/train/{}.jpg'.format(f))
#     image = image.resize((nwidth, nheight))
#     image = np.array(image)
#     image = np.clip(image / 255.0, 0.0, 1.0)  # 255 = max of the value of a pixel
#     i += 1
#     allImage[i - 1] = image
#     print(f)
#     train = allImage
#     # if i == 3:
#     #     break

lum_img = train[100, :, :, :]
lum_img = np.array(lum_img)

print(lum_img.shape)

allImage = np.zeros(lum_img.shape) # workaround, otherwise there is a weird bug happening ValueError: arrays must be of dtype byte, short, float32 or float64

lum_img_final = allImage + lum_img
print(lum_img_final.shape)

plt.imshow(lum_img_final)
plt.show()
