import pandas as pd
import os
import glob
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import shap
import IPython
import time
from scipy import stats
import tensorflow as tf
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from pylab import rcParams
from sklearn.model_selection import train_test_split
from keras.models import Model, load_model
from keras.layers import Input, Dense,LSTM,RepeatVector
from keras.callbacks import ModelCheckpoint, TensorBoard
from collections import deque
from sklearn.preprocessing import MinMaxScaler
from xgboost import plot_tree, plot_importance

type = 1


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

file_list = os.listdir('DataBase/CNS_db/pkl')
selected_para = pd.read_csv('DataBase/Final_parameter.csv')
untrain_data = []
for _ in file_list:
    if _[:7] == 'ab20-01':
        untrain_data.append(_)
    elif _[:7] == 'ab59-01':
        untrain_data.append(_)
    elif _[:7] == 'ab80-02':
        untrain_data.append(_)
    elif _[:7] == 'ab64-03':
        untrain_data.append(_)
    else:
        pass
test_db = ['ab15-07_1016.pkl', 'ab21-12_16.pkl', 'ab19-02_01 (04;42트립).pkl', 'ab15-07_1016.pkl', 'ab15-07_1035.pkl', 'ab15-08_1063.pkl', 'ab15-08_1089.pkl', 'ab19-02_01 (04;42트립).pkl', 'ab19-02_44(2;57trip).pkl', 'ab19-02-6(트립x).pkl', 'ab20-01_99(auto까지).pkl', 'ab20-04_8.pkl', 'ab20-04_13.pkl', 'ab21-01_158.pkl', 'ab21-01_168.pkl', 'ab21-02_132(Trip).pkl', 'ab21-02_150.pkl', 'ab21-11_24(27;32트립).pkl', 'ab21-11_88(4;08트립).pkl', 'ab21-12_16.pkl', 'ab21-12_38 (05;28트립).pkl', 'ab23-01_10024(01;02trip).pkl', 'ab23-01_30024(1;00_trip).pkl', 'ab23-03-16.pkl', 'ab23-03-95.pkl', 'ab23-06_10004(03;17_trip).pkl', 'ab23-06_30032(52s trip).pkl', 'ab59-02-1013.pkl', 'ab59-02-1073.pkl', 'ab60-02_57.pkl', 'ab60-02_210.pkl', 'ab63-02_3.pkl', 'ab63-03-1.pkl', 'ab63-04_124.pkl', 'ab63-04_335.pkl', 'ab64-03-02(트립).pkl', 'ab80-02_23.pkl', 'normal0.pkl']
scaler = MinMaxScaler()
min_value = pd.read_csv('DataBase/min_value_final.csv')
max_value = pd.read_csv('DataBase/max_value_final.csv')
scaler.fit([min_value['0'], max_value['0']])
autoencoder = load_model('train_untrain/Train_Untrain_epoch27_[0.00225299]_acc_[0.9724685967462512].h5')
# autoencoder = load_model('nor_ab/Nor_Ab_epoch1_[0.00358652]_acc_[0.2587023813180802].h5')
XGB = pickle.load(open("XGB_max_depth/XGB_max_depth_46.h5", "rb"))

explainer = shap.TreeExplainer(XGB)
# for test in untrain_data:
for test in test_db:
    with open(f'DataBase/CNS_db/pkl/{test}', 'rb') as f:
        db = pickle.load(f)
    selected_db = db[selected_para['0'].tolist()]
    scaled_db = scaler.transform(selected_db)
    scaled_db = np.array(scaled_db)
    # scaled_db = selected_db
    real_2D_data = deque(maxlen=1)
    real_time_db = deque(maxlen=10)
    error, time, prediction = [], [], []
    plt.close()
    for line in range(len(scaled_db)):
        real_time_db.append(scaled_db[line,:])
        data = np.array([real_time_db])
        print(np.shape(data))
        real_2D_data.append(scaled_db[line, :])
        dim2 = np.array(real_2D_data)
        if type == 1: # 3차원 데이터
            if np.shape(data)[1] < 10:
                print('시계열 데이터 구성을 위해서 시간이 필요합니다.')
            else:
                valid_x_predictions = autoencoder.predict(data)
                mse = np.mean(np.power(flatten(np.array(data)) - flatten(valid_x_predictions), 2), axis=1)
                print(mse)
                error.append(mse)
                time.append(line)
                if error[-1] > 0.00225299: # 비정상 or Untrain
                    plt.plot(time[-1], error[-1], 'rx', ms=4.5)
                    plt.title('Abnormal')
                else:
                    plt.plot(time[-1], error[-1], 'go', ms=4.5)
                    plt.title('Normal')
                plt.hlines(0.00225299, time[0], time[-1], 'b')

                plt.pause(0.1)
        elif type == 2: #2차원 데이터
            # time.append(line)
            y_pred = XGB.predict(dim2)
            print(y_pred)
            # prediction.append(y_pred)
            # plt.plot(time[:line], prediction[:line], 'r.', ms=2)
            # plt.pause(0.01)
            # plot_tree(XGB)
            # plot_importance(XGB)
            # plt.show()
            shap_values = explainer.shap_values(dim2)
            # print(np.shape(shap_values))
            # shap.initjs()
            print(shap_values)
            # plt.figure(1)
            # print(np.shape(shap_values))
            # print(explainer.expected_value)
            shap.force_plot(explainer.expected_value[int(y_pred)], shap_values[int(y_pred)], pd.DataFrame(dim2, columns=selected_para['0'].tolist()), matplotlib=True, figsize=(10,5), show=False)
            # plt.draw()
            plt.pause(1)
            # plt.close()

            # dp = shap.multioutput_decision_plot(explainer.expected_value, shap_values, pd.DataFrame(dim2, columns=selected_para['0'].tolist()))
            # plt.show(dp)

            # plt.draw(shap_dp)
            # plt.draw()
            # print(explainer.expected_value)
            # plt.plot(time[-1],explainer.expected_value, 'r.')



            # plt.pause(1)
            # plt.cla()
            # plt.show()
            # plt.close(dp)
            # plt.show(block=False)
            # plt.show(shap_dp)
            # print(explainer.expected_value)
            # print(np.shape(dim2))
            # print(pd.DataFrame(dim2, columns=selected_para['0'].tolist()))
            # plt.figure(1)
            # shap.summary_plot(shap_values, pd.DataFrame(dim2, columns=selected_para['0'].tolist()))
            # plt.clf()
            # plt.show(dp)
            # plt.pause(0.01)
            # plt.close()


            # plt.close()















# type = 2
#
# if type == 1:
#     RANDOM_SEED = 42
#     LABELS = ["Abnormal", "Normal"]
#     with open('DataBase/CNS_LSTM_autoencoder_Nor_Ab.bin', 'rb') as f:
#         db = pickle.load(f)
#     train_x, train_y, test_x, test_y = [], [], [], []
#     for _ in db.keys():
#         for temp in range(len(db[_]['train_x_db'])):
#             if np.argmax(db[_]['train_y_db'], axis=1)[temp] == 0:  # 정상데이터
#                 train_x.append(db[_]['train_x_db'][temp])
#                 train_y.append(np.argmax(db[_]['train_y_db'], axis=1)[temp])
#             elif np.argmax(db[_]['train_y_db'], axis=1)[temp] == 1:  # 비정상데이터
#                 test_x.append(db[_]['train_x_db'][temp])
#                 test_y.append(np.argmax(db[_]['train_y_db'], axis=1)[temp])
#
#     train_x = np.array(train_x)
#     train_y = np.array(train_y)
#     test_x = np.array(test_x)
#     test_y = np.array(test_y)
#
#
#     def flatten(X):
#         '''
#         Flatten a 3D array.
#
#         Input
#         X            A 3D array for lstm, where the array is sample x timesteps x features.
#
#         Output
#         flattened_X  A 2D array, sample x features.
#         '''
#         flattened_X = np.empty((X.shape[0], X.shape[2]))  # sample x features array.
#         for i in range(X.shape[0]):
#             flattened_X[i] = X[i, (X.shape[1] - 1), :]
#         return (flattened_X)
#
#     autoencoder = load_model('LSTM_autoencoder.h5')
#
#     valid_x_predictions = autoencoder.predict(np.array(train_x))
#     mse = np.mean(np.power(flatten(np.array(train_x)) - flatten(valid_x_predictions), 2), axis=1)
#
#     error_ = pd.DataFrame({'reconstruction_error': mse, })
#     # error_ = pd.DataFrame(mse)
#
#     temp = error_.describe()
#
#     threshold = (temp.iloc[1].values) * 3 * (temp.iloc[2].values)
#     print(threshold)
#
#     valid_x_predictions = autoencoder.predict([test_x])
#     mse = np.mean(np.power(flatten(np.array(test_x)) - flatten(valid_x_predictions), 2), axis=1)
#
#     error_df = pd.DataFrame({'reconstruction_error': mse,
#                              'true_class': np.array(test_y).reshape(-1)})
#
#     error_df.describe()
#
#     groups = error_df.groupby('true_class')
#     fig, ax = plt.subplots()
#     for name, group in groups:
#         ax.plot(group.reconstruction_error, marker='o', ms=1, linestyle='',
#                 label="Abnormal" if name == 1 else "Normal")
#
#     ax.hlines(threshold, ax.get_xlim()[0], ax.get_xlim()[1], colors="r", zorder=100, label='Threshold')
#     ax.legend()
#     # ax.plot(c,color='black',ms = 00000.1)
#     # ax.plot(d,color='black',ms = 00000.1)
#     # ax.fill_between(c,d,where=c>=d,facecolor='yellow', alpha=0.5)
#     ax.set_title('Fill Between')
#
#     plt.title("Reconstruction error for the normal and abnormal data")
#     plt.ylabel("Reconstruction error")
#     plt.xlabel("Data point index")
#     plt.show();
#
# elif type == 2:
#     with open('DataBase/CNS_LSTM_autoencoder_Nor_Ab.bin', 'rb') as f:
#         db = pickle.load(f)
#
#     untrain_data = []
#     for _ in db.keys():
#         if _[:7] == 'ab20-01':
#             untrain_data.append(_)
#         elif _[:7] == 'ab59-01':
#             untrain_data.append(_)
#         elif _[:7] == 'ab80-02':
#             untrain_data.append(_)
#         elif _[:7] == 'ab64-03':
#             untrain_data.append(_)
#         else:
#             pass
#
#     train_x = [db[_]['train_x_db'] for _ in db.keys() if not _ in untrain_data]
#     train_y = [db[_]['train_y_db'] for _ in db.keys() if not _ in untrain_data]
#     test_x = [db[_]['train_x_db'] for _ in db.keys() if _ in untrain_data]
#     test_y = [db[_]['train_y_db'] for _ in db.keys() if _ in untrain_data]
#     train_x = np.concatenate(train_x)
#     train_y = np.concatenate(train_y)
#     test_x = np.concatenate(test_x)
#     test_y = np.concatenate(test_y)
#
#     def flatten(X):
#         '''
#         Flatten a 3D array.
#
#         Input
#         X            A 3D array for lstm, where the array is sample x timesteps x features.
#
#         Output
#         flattened_X  A 2D array, sample x features.
#         '''
#         flattened_X = np.empty((X.shape[0], X.shape[2]))  # sample x features array.
#         for i in range(X.shape[0]):
#             flattened_X[i] = X[i, (X.shape[1] - 1), :]
#         return (flattened_X)
#
#     autoencoder = load_model('Train_Untrain_epoch_50.h5')
#
#     valid_x_predictions = autoencoder.predict(np.array(train_x))
#     mse = np.mean(np.power(flatten(np.array(train_x)) - flatten(valid_x_predictions), 2), axis=1)
#
#     error_ = pd.DataFrame({'reconstruction_error': mse, })
#     # error_ = pd.DataFrame(mse)
#
#     temp = error_.describe()
#
#     threshold = (temp.iloc[1].values) * 3 * (temp.iloc[2].values)
#     print(threshold)
#
#     valid_x_predictions = autoencoder.predict([train_x])
#     mse = np.mean(np.power(flatten(np.array(train_x)) - flatten(valid_x_predictions), 2), axis=1)
#
#     error_df = pd.DataFrame({'reconstruction_error': mse,
#                              'true_class': np.array(np.argmax(train_y, axis=1)).reshape(-1)})
#
#     error_df.describe()
#
#     groups = error_df.groupby('true_class')
#     fig, ax = plt.subplots()
#     for name, group in groups:
#         ax.plot(group.reconstruction_error, marker='o', ms=3.5, linestyle='',
#                 label="Abnormal" if name == 1 else "Normal")
#
#     ax.hlines(threshold, ax.get_xlim()[0], ax.get_xlim()[1], colors="r", zorder=100, label='Threshold')
#     ax.legend()
#     # ax.plot(c,color='black',ms = 00000.1)
#     # ax.plot(d,color='black',ms = 00000.1)
#     # ax.fill_between(c,d,where=c>=d,facecolor='yellow', alpha=0.5)
#     ax.set_title('Fill Between')
#
#     plt.title("Reconstruction error for the normal and abnormal data")
#     plt.ylabel("Reconstruction error")
#     plt.xlabel("Data point index")
#     plt.show();
#
# #
# #
