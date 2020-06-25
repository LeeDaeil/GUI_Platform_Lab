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

print(np.shape(train_x), np.shape(train_y), np.shape(test_x), np.shape(test_y))

timesteps=10
input_dim=46
units=50 #choosen unit number randomly

def get_model(n_dimensions):
    inputs = Input(shape=(timesteps, input_dim))
    encoded = LSTM(n_dimensions, return_sequences=False, name="encoder")(inputs)
    decoded = RepeatVector(timesteps)(encoded)
    decoded = LSTM(input_dim, return_sequences=True, name='decoder')(decoded)

    autoencoder = Model(inputs, decoded)
    encoder = Model(inputs, encoded)
    return autoencoder, encoder

autoencoder, encoder = get_model(input_dim)
autoencoder.compile(optimizer='adam', loss='mse',
                    metrics=['acc', 'cosine_proximity'])

history = autoencoder.fit([train_x], [train_x], batch_size=16, epochs=150)
# encoded = encoder.predict([train_x])
autoencoder.save('LSTM_autoencoder.h5')