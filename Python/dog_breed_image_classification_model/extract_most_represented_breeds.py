import numpy as np
import pickle
import pandas as pd
import matplotlib.pyplot as plt

Nber_of_breeds = 8
train = pickle.load(open("train.p", "rb"))  # 10,222 dogs
labels_raw = pd.read_csv("D:/Downloads/Classification Models/labels.csv", header=0, sep=',', quotechar='"')


def main_breeds(labels_raw, Nber_breeds, all_breeds='TRUE'):
    # labels_freq_pd = itemfreq(labels_raw["breed"]) # itemfreq is deprecated https://stackoverflow.com/questions/75910116/attributeerror-module-scipy-stats-has-no-attribute-itemfreq
    values, counts = np.unique(labels_raw['breed'], return_counts=True)  # get unuque counts per label
    labels_freq_pd = np.column_stack((values, counts))  # combine values and counts into a df
    labels_freq_pd = labels_freq_pd[labels_freq_pd[:, 1].argsort()[::-1]]  # sort df desc by count

    if all_breeds == 'FALSE':
        main_labels = labels_freq_pd[:, 0][0:Nber_breeds]
    else:
        main_labels = labels_freq_pd[:, 0][:]

    labels_raw_np = labels_raw['breed'].to_numpy()  # all labels to an array
    # transpose from a single row array to a single column 2d array
    labels_raw_np = labels_raw_np.reshape(labels_raw_np.shape[0], 1)
    # indexes in labels_raw_np of only those labels that appear in main_labels
    labels_filtered_index = np.where(labels_raw_np == main_labels)
    return labels_filtered_index


labels_filtered_index = main_breeds(labels_raw=labels_raw, Nber_breeds=Nber_of_breeds, all_breeds='FALSE')
labels_filtered = labels_raw.iloc[labels_filtered_index[0], :]  # iloc[i,j] means i is the row, j the column of the df
train_filtered = train[labels_filtered_index[0], :, :, :]
print('- Number of images remaining after selecting the {0} main breeds : {1}'.format(Nber_of_breeds,
                                                                                      labels_filtered_index[0].shape))
print('- The shape of train_filtered dataset is : {0}'.format(train_filtered.shape))

lum_img = train_filtered[1, :, :, :]
plt.imshow(np.zeros(lum_img.shape) + lum_img)  # workaround, otherwise it doesnt work
plt.show()

# One-Hot Labels
# We select the labels from the N main breeds
labels = labels_filtered["breed"].to_numpy()
labels = labels.reshape(labels.shape[0], 1)  # labels.shape[0] looks faster than using len(labels)
print("labels.shape:", labels.shape)


# Function to create one-hot labels
def matrix_Bin(labels):
    labels_bin = np.array([])

    labels_name, labels0 = np.unique(labels,
                                     return_inverse=True)  # Reconstruct the labels array from the unique values and inverse:
    labels0
    # workaround for itemfreq(labels0)
    for _, i in enumerate(np.unique(labels0).astype(int)):  # for each of the 8 unique values
        labels_bin0 = np.where(labels0 == np.unique(labels0)[i], 1.,
                               0.)  # replace in the 922 array with 0 and 1 for those for which the value equals the current one [i]
        labels_bin0 = labels_bin0.reshape(1, labels_bin0.shape[0])  # make it a row instead of a column

        if labels_bin.shape[0] == 0:  # check if it's the first iteration
            labels_bin = labels_bin0  # then first row in the labels_bin will be the row from above (labels_bin0)
        else:
            labels_bin = np.concatenate((labels_bin, labels_bin0), axis=0)  # append the row from above (labels_bin0)

    print("Nber SubVariables {0}".format(np.unique(labels0).shape[0]))
    labels_bin = labels_bin.transpose()
    print("Shape : {0}".format(labels_bin.shape))

    return labels_name, labels_bin


labels_name, labels_bin = matrix_Bin(labels=labels)

print(labels_bin[0:9])
print(labels_name)
