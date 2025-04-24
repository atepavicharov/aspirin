import numpy as np
from io import BytesIO
from zipfile import ZipFile
import PIL.Image
import matplotlib.pyplot as plt

archive_train = ZipFile("D:/Downloads/Classification Models/train.zip", 'r')

filename = BytesIO(archive_train.read(archive_train.namelist()[2]))  # 1st image

image = PIL.Image.open(filename)
image = image.resize((60, 60))

image = np.array(image)
image = np.clip(image / 255.0, 0.0, 1.0)  # 255 = max of the value of a pixel
plt.imshow(image)
plt.show()

# test how this works
x = np.array([1, 2, 3, 60, 5, 6])
y = np.array([10, 1, 30, 40, 5, 60])
print(np.where(x == y))

x = x.reshape(x.shape[0], 1)  # this makes it 2d array
print(np.where(x == y))
