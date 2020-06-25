import pandas as pd
import os
import glob
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
from scipy import stats
import tensorflow as tf
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from pylab import rcParams
from sklearn.model_selection import train_test_split
from keras.models import Model, load_model
from keras.layers import Input, Dense,LSTM,RepeatVector
from keras.callbacks import ModelCheckpoint, TensorBoard
from keras import regularizers
rcParams['figure.figsize'] = 14, 8

RANDOM_SEED = 42
LABELS = ["Abnormal", "Normal"]

with open('DataBase/CNS_predict_abnormal_accident_train_db_3D_scaler.bin', 'rb') as f:
    db = pickle.load(f)

train_x_db = [db[_]['train_x_db'] for _ in db.keys() if _[:6] == 'normal']
train_y_db = [db[_]['train_y_db'] for _ in db.keys() if _[:6] == 'normal']
test_x_db = [db[_]['train_x_db'] for _ in db.keys() if not _[:6] == 'normal']
test_y_db = [db[_]['train_y_db'] for _ in db.keys() if not _[:6] == 'normal']

train_x = np.concatenate(train_x_db)
train_y = np.argmax(np.concatenate(train_y_db), axis=1)
test_x = np.concatenate(test_x_db)
test_y = np.argmax(np.concatenate(test_y_db), axis=1)

autoencoder = load_model('LSTM_autoencoder.h5')


def flatten(X):
    '''
    Flatten a 3D array.

    Input
    X            A 3D array for lstm, where the array is sample x timesteps x features.

    Output
    flattened_X  A 2D array, sample x features.
    '''
    flattened_X = np.empty((X.shape[0], X.shape[2]))  # sample x features array.
    for i in range(X.shape[0]):
        flattened_X[i] = X[i, (X.shape[1] - 1), :]
    return (flattened_X)

# valid_x_pre


threshold = 0.000064+3*0.001036 # mean*3*std

valid_x_predictions = autoencoder.predict([test_x])
mse = np.mean(np.power(flatten(np.array(test_x)) - flatten(valid_x_predictions), 2), axis=1)

error_df = pd.DataFrame({'reconstruction_error': mse,
                        'true_class': np.array(test_y).reshape(-1)})
error_df.describe()

groups = error_df.groupby('true_class')
fig, ax = plt.subplots()
for name, group in groups:
    ax.plot(group.reconstruction_error[0:100], marker='o', ms=3.5, linestyle='',
            label= "Abnormal" if name == 1 else "Normal")

ax.hlines(threshold, ax.get_xlim()[0], ax.get_xlim()[1], colors="r", zorder=100, label='Threshold')
ax.legend()
# ax.plot(c,color='black',ms = 00000.1)
# ax.plot(d,color='black',ms = 00000.1)
# ax.fill_between(c,d,where=c>=d,facecolor='yellow', alpha=0.5)
ax.set_title('Fill Between')
plt.title("Reconstruction error for the normal and abnormal data")
plt.ylabel("Reconstruction error")
plt.xlabel("Data point index")
plt.show();
