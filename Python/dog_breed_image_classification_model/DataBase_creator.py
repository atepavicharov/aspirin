import time
import pickle
from datetime import timedelta

import numpy as np

# Image manipulation
import PIL.Image

# Open a Zip File
from zipfile import ZipFile
from io import BytesIO

# We unzip the train and test zip file
archive_train = ZipFile("D:/Downloads/Classification Models/train.zip", 'r')
archive_test = ZipFile("D:/Downloads/Classification Models/test.zip", 'r')


# This function help to create  a pickle file gathering all the image from a zip folder
def DataBase_creator(archivezip, nwidth, nheight, save_name):
    # We choose the archive (zip file) + the new width and height for all the image which will be reshaped

    # Start-time used for printing time-usage below.
    start_time = time.time()

    # nwidth x nheight = number of features because images have nwidth x nheight pixels
    # Maybe 3 here is because the CNN will have 3 convolutional layers
    s = (len(archivezip.namelist()[:]) - 1, nwidth, nheight, 3)
    allImage = np.zeros(s)  # s matrix with zeros
    # for i in range(1, len(archivezip.namelist()[:])):
    for i in range(1, len(archivezip.namelist()[:])):  # for a memory est
        filename = BytesIO(archivezip.read(archivezip.namelist()[i]))
        image = PIL.Image.open(filename)  # open colour image
        image = image.resize((nwidth, nheight))
        image = np.array(image)
        image = np.clip(image / 255.0, 0.0, 1.0)  # 255 = max of the value of a pixel
        allImage[i - 1] = image

    # we save the newly created data base
    pickle.dump(allImage, open(save_name + '.p', "wb"))

    # Ending time.
    end_time = time.time()
    # Difference between start and end-times.
    time_dif = end_time - start_time
    # Print the time-usage.
    print("Time usage: " + str(timedelta(seconds=int(round(time_dif)))))


if __name__ == "__main__":
    image_resize = 60
    try:
        print("Creating Train pickle")
        DataBase_creator(archivezip=archive_train, nwidth=image_resize, nheight=image_resize, save_name="train")
    except Exception as e:
        print(e.message)

    try:
        print("Creating Test pickle")
        DataBase_creator(archivezip=archive_test, nwidth=image_resize, nheight=image_resize, save_name="test")
    except Exception as e:
        print(e.message)
