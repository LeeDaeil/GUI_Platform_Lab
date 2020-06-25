import pandas as pd
import os
import glob
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from xgboost import XGBClassifier
from sklearn.metrics import confusion_matrix, plot_confusion_matrix, ConfusionMatrixDisplay
from sklearn.metrics import classification_report
from keras.layers import Dense, Input, Conv1D, MaxPooling1D, LSTM, Flatten, SimpleRNN, GRU, Dropout
from keras.models import Model, Sequential
import lightgbm as lgb
import seaborn as sn
import keras
from keras import backend as K
from keras.models import Sequential, Model
from keras.layers import Input, LSTM, RepeatVector
from keras.layers.core import Flatten, Dense, Dropout, Lambda
from keras.optimizers import SGD, RMSprop, Adam
from keras import objectives
import matplotlib.pyplot as plt


type = 1 # 1: LSTM_AutoEncoder(AB/Nor), 2: LSTM_AutoEncoder(Trained/Untrained), 3: Xgboost(procedure classification)

if type == 1:
    scaler = MinMaxScaler()
    LABELS = ["Abnormal", "Normal"]
    file_name = os.listdir('DataBase/CNS_db/pkl')
    selected_para = pd.read_csv('DataBase/Final_parameter.csv')
    selected_para = selected_para['0'].tolist()
    min_value = pd.read_csv('DataBase/min_value_final.csv')
    max_value = pd.read_csv('DataBase/max_value_final.csv')
    scaler.fit([min_value['0'], max_value['0']])
    train = []
    train_db = []
    for _ in file_name:
        if _[:6] == 'normal':
            train.append(_)
    for temp in train:
        with open(f'DataBase/CNS_db/pkl/{temp}', 'rb') as f:
            db = pickle.load(f)
        train_x = db[selected_para]
        train_x = scaler.transform(train_x)
        train_db.append([train_x[line:line+10] for line in range(len(train_x)-10)])
    data = np.concatenate(train_db)

    print(np.shape(data))

    timesteps = 10
    input_dim = 46
    units = 64  # choosen unit number randomly
    epoch = 200


    def get_model(n_dimensions):
        inputs = Input(shape=(timesteps, input_dim))
        encoded = LSTM(n_dimensions, return_sequences=False, name="encoder")(inputs)
        encoded = Dropout(0.5)(encoded)
        decoded = RepeatVector(timesteps)(encoded)
        decoded = Dropout(0.5)(decoded)
        decoded = LSTM(input_dim, return_sequences=True, name='decoder')(decoded)

        autoencoder = Model(inputs, decoded)
        encoder = Model(inputs, encoded)
        return autoencoder, encoder


    autoencoder, encoder = get_model(input_dim)
    autoencoder.compile(optimizer='adam', loss='mse',
                        metrics=['acc', 'cosine_proximity'])

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

    # def create_lstm_vae(input_dim,
    #                     timesteps,
    #                     batch_size,
    #                     intermediate_dim,
    #                     latent_dim,
    #                     epsilon_std=1.):
    #
    #     """
    #     Creates an LSTM Variational Autoencoder (VAE). Returns VAE, Encoder, Generator.
    #     # Arguments
    #         input_dim: int.
    #         timesteps: int, input timestep dimension.
    #         batch_size: int.
    #         intermediate_dim: int, output shape of LSTM.
    #         latent_dim: int, latent z-layer shape.
    #         epsilon_std: float, z-layer sigma.
    #     # References
    #         - [Building Autoencoders in Keras](https://blog.keras.io/building-autoencoders-in-keras.html)
    #         - [Generating sentences from a continuous space](https://arxiv.org/abs/1511.06349)
    #     """
    #     x = Input(shape=(timesteps, input_dim,))
    #
    #     # LSTM encoding
    #     h = LSTM(intermediate_dim)(x)
    #
    #     # VAE Z layer
    #     z_mean = Dense(latent_dim)(h)
    #     z_log_sigma = Dense(latent_dim)(h)
    #
    #     def sampling(args):
    #         z_mean, z_log_sigma = args
    #         epsilon = K.random_normal(shape=(batch_size, latent_dim),
    #                                   mean=0., stddev=epsilon_std)
    #         return z_mean + z_log_sigma * epsilon
    #
    #     # note that "output_shape" isn't necessary with the TensorFlow backend
    #     # so you could write `Lambda(sampling)([z_mean, z_log_sigma])`
    #     z = Lambda(sampling, output_shape=(latent_dim,))([z_mean, z_log_sigma])
    #
    #     # decoded LSTM layer
    #     decoder_h = LSTM(intermediate_dim, return_sequences=True)
    #     decoder_mean = LSTM(input_dim, return_sequences=True)
    #
    #     h_decoded = RepeatVector(timesteps)(z)
    #     h_decoded = decoder_h(h_decoded)
    #
    #     # decoded layer
    #     x_decoded_mean = decoder_mean(h_decoded)
    #
    #     # end-to-end autoencoder
    #     vae = Model(x, x_decoded_mean)
    #
    #     # encoder, from inputs to latent space
    #     encoder = Model(x, z_mean)
    #
    #     # generator, from latent space to reconstructed inputs
    #     decoder_input = Input(shape=(latent_dim,))
    #
    #     _h_decoded = RepeatVector(timesteps)(decoder_input)
    #     _h_decoded = decoder_h(_h_decoded)
    #
    #     _x_decoded_mean = decoder_mean(_h_decoded)
    #     generator = Model(decoder_input, _x_decoded_mean)
    #
    #     def vae_loss(x, x_decoded_mean):
    #         xent_loss = objectives.mse(x, x_decoded_mean)
    #         kl_loss = - 0.5 * K.mean(1 + z_log_sigma - K.square(z_mean) - K.exp(z_log_sigma))
    #         loss = xent_loss + kl_loss
    #         return loss
    #
    #     vae.compile(optimizer='rmsprop', loss=vae_loss, metrics=['acc', 'cosine_proximity'])
    #     # vae.compile(optimizer='adam', loss=vae_loss)
    #
    #     return vae, encoder, generator


    # input_dim = data.shape[-1]  # 46
    # timesteps = data.shape[1]  # 10
    # batch_size = 1
    #
    # vae, enc, gen = create_lstm_vae(input_dim,
    #                                 timesteps=timesteps,
    #                                 batch_size=batch_size,
    #                                 intermediate_dim=64,
    #                                 latent_dim=100,
    #                                 epsilon_std=1.)

    for _ in range(1000):
        history = autoencoder.fit(data, data, batch_size=32, epochs=1)
        valid_x_predictions = autoencoder.predict(data)
        mse = np.mean(np.power(flatten(data) - flatten(valid_x_predictions), 2), axis=1)
        error_ = pd.DataFrame({'reconstruction_error': mse, })
        # error_ = pd.DataFrame(mse)
        temp = error_.describe()
        print(temp)
        print(temp.iloc[1].values)
        print(temp.iloc[2].values)
        threshold = (temp.iloc[1].values) + (3 * (temp.iloc[2].values))
        print(threshold)
        autoencoder.save(f'nor_ab/node64_Nor_Ab_epoch{_+1}_{threshold}_acc_{history.history["acc"]}.h5')

        # history = vae.fit(data, data, epochs=1)
        # print('훈련 완료')
        # valid_x_predictions = vae.predict(data, batch_size=batch_size)
        # print('예측 완료')
        # mse = np.mean(np.power(flatten(data) - flatten(valid_x_predictions), 2), axis=1)
        # error_ = pd.DataFrame({'reconstruction_error': mse, })
        # temp = error_.describe()
        # threshold = (temp.iloc[1].values) + (3 * (temp.iloc[2].values))
        # print('Threshold 계산 완료')
        # vae.save_weights(f'nor_ab/LSTM-VAE_Nor_Ab_epoch{_ + 1}_{threshold}_acc_{history.history["acc"]}_rev1.h5')
        # # pickle.dump(vae, open(f'nor_ab/LSTM-VAE_Nor_Ab_epoch{_ + 1}_{threshold}_acc_{history.history["acc"]}.h5', 'wb'))
        # print('파일 저장 완료')

        # # pick a column to plot.
        # print("[plotting...]")
        # print("x: %s, preds: %s" % (data.shape, valid_x_predictions.shape))
        # plt.plot(data[:, 0, 3], label='data')
        # plt.plot(valid_x_predictions[:, 0, 3], label='predict')
        # plt.legend()
        # plt.show()

elif type == 2: # Trained_Untrained
    with open('DataBase/CNS_autoencdoer.bin', 'rb') as f:
        db = pickle.load(f)

    print(db.keys())

    untrain_data = []
    for _ in db.keys():
        if _[:7] == 'ab20-01':
            untrain_data.append(_)
        elif _[:7] == 'ab59-01':
            untrain_data.append(_)
        elif _[:7] == 'ab80-02':
            untrain_data.append(_)
        elif _[:7] == 'ab64-03':
            untrain_data.append(_)
        elif _[:7] == 'ab63-03':
            untrain_data.append(_)
        else:
            pass

        print(untrain_data)

    train_x = [db[_]['train_x_db'] for _ in db.keys() if not _ in untrain_data]
    test_x = [db[_]['train_x_db'] for _ in db.keys() if _ in untrain_data]

    print(train_x)

    # train_x = np.concatenate(train_x)
    # test_x = np.concatenate(test_x)
    #
    # timesteps = 10
    # input_dim = 46
    # units = 64  # choosen unit number randomly
    # epoch = 150
    #
    # def get_model(n_dimensions):
    #     inputs = Input(shape=(timesteps, input_dim))
    #     encoded = LSTM(n_dimensions, return_sequences=False, name="encoder")(inputs)
    #     decoded = RepeatVector(timesteps)(encoded)
    #     decoded = LSTM(input_dim, return_sequences=True, name='decoder')(decoded)
    #
    #     autoencoder = Model(inputs, decoded)
    #     encoder = Model(inputs, encoded)
    #     return autoencoder, encoder
    #
    #
    # autoencoder, encoder = get_model(input_dim)
    # autoencoder.compile(optimizer='adam', loss='mse',
    #                     metrics=['acc', 'cosine_proximity'])
    #
    #
    #
    # def flatten(X):
    #     '''
    #     Flatten a 3D array.
    #
    #     Input
    #     X            A 3D array for lstm, where the array is sample x timesteps x features.
    #
    #     Output
    #     flattened_X  A 2D array, sample x features.
    #     '''
    #     flattened_X = np.empty((X.shape[0], X.shape[2]))  # sample x features array.
    #     for i in range(X.shape[0]):
    #         flattened_X[i] = X[i, (X.shape[1] - 1), :]
    #     return (flattened_X)
    #
    # for _ in range(epoch):
    #     history = autoencoder.fit(train_x, train_x, batch_size=64, epochs=1)
    #     valid_x_predictions = autoencoder.predict(train_x)
    #     mse = np.mean(np.power(flatten(train_x) - flatten(valid_x_predictions), 2), axis=1)
    #
    #     error_ = pd.DataFrame({'reconstruction_error': mse, })
    #     # error_ = pd.DataFrame(mse)
    #
    #     temp = error_.describe()
    #     print(temp)
    #     print(temp.iloc[1].values)
    #     print(temp.iloc[2].values)
    #
    #     threshold = (temp.iloc[1].values) + (3 * (temp.iloc[2].values))
    #     print(threshold)
    #
    #
    #
    #
    #     autoencoder.save(f'train_untrain/Train_Untrain_epoch{_+1}_{threshold}_acc_{history.history["acc"]}.h5')

elif type == 3:
    with open('DataBase/CNS_Xgboost_Nor_Ab.bin', 'rb') as f:
        db = pickle.load(f)
    test_db = ['ab15-07_1016.pkl', 'ab15-07_1035.pkl', 'ab15-08_1063.pkl', 'ab15-08_1089.pkl', 'ab19-02_01 (04;42트립).pkl', 'ab19-02_44(2;57trip).pkl', 'ab19-02-6(트립x).pkl', 'ab20-01_99(auto까지).pkl', 'ab20-04_8.pkl', 'ab20-04_13.pkl', 'ab21-01_158.pkl', 'ab21-01_168.pkl', 'ab21-02_132(Trip).pkl', 'ab21-02_150.pkl', 'ab21-11_24(27;32트립).pkl', 'ab21-11_88(4;08트립).pkl', 'ab21-12_16.pkl', 'ab21-12_38 (05;28트립).pkl', 'ab23-01_10024(01;02trip).pkl', 'ab23-01_30024(1;00_trip).pkl', 'ab23-03-16.pkl', 'ab23-03-95.pkl', 'ab23-06_10004(03;17_trip).pkl', 'ab23-06_30032(52s trip).pkl', 'ab59-02-1013.pkl', 'ab59-02-1073.pkl', 'ab60-02_57.pkl', 'ab60-02_210.pkl', 'ab63-02_3.pkl', 'ab63-03-1.pkl', 'ab63-04_124.pkl', 'ab63-04_335.pkl', 'ab64-03-02(트립).pkl', 'ab80-02_23.pkl', 'normal0.pkl']

    train_x = np.concatenate([db[_]['train_x_db'] for _ in db.keys() if not _ in test_db])
    train_y = np.concatenate([db[_]['train_y_db'] for _ in db.keys() if not _ in test_db])
    test_x = np.concatenate([db[_]['train_x_db'] for _ in db.keys() if _ in test_db])
    test_y = np.concatenate([db[_]['train_y_db'] for _ in db.keys() if _ in test_db])
    print(f'Train_x = {np.shape(train_x)}, Train_y = {np.shape(train_y)}, Test_x = {np.shape(test_x)}, Test_y = {np.shape(test_y)}')
    print('데이터 라벨 불균형 확인')
    imbalance_num = {'normal': [], 'abnormal': []}
    num1 = np.argmax(train_y, axis=1)
    for _ in range(len(num1)):
        if num1[_] == 0:
            imbalance_num['normal'].append(num1[_])
        elif num1[_] == 1:
            imbalance_num['abnormal'].append(num1[_])

    print('정상데이터 :', len(imbalance_num['normal']), '비정상데이터 : ', len(imbalance_num['abnormal']))

    weight_para = (len(imbalance_num['normal'])/len(imbalance_num['abnormal']))*0.12

    depth = 46
    model = XGBClassifier(scale_pos_weight=weight_para, max_depth=depth, eta=0.001, objective='binary:logistic', num_rounds=100)
    model.fit(train_x, np.argmax(train_y, axis=1))
    pickle.dump(model, open(f'XGB_max_depth/XGBClassification_Nor_Ab_{weight_para}_max_depth_{depth}.h5', 'wb'))
    y_pred = model.predict(test_x)
    # confusion_matrix(np.argmax(test_y, axis=1), y_pred)
    disp = plot_confusion_matrix(model, test_x, np.argmax(test_y, axis=1))
    print(disp.confusion_matrix)
    print(classification_report(np.argmax(test_y, axis=1), y_pred, target_names=['Normal', 'Abnormal']))


elif type == 4:

    with open('DataBase/CNS_Xgboost_16Procedure_rev1.bin', 'rb') as f:
        db = pickle.load(f)
    test_db = ['ab15-07_1016.pkl', 'ab15-07_1035.pkl', 'ab15-08_1063.pkl', 'ab15-08_1089.pkl', 'ab19-02_01 (04;42트립).pkl', 'ab19-02_44(2;57trip).pkl', 'ab19-02-6(트립x).pkl', 'ab20-04_8.pkl', 'ab20-04_13.pkl', 'ab21-01_158.pkl', 'ab21-01_168.pkl', 'ab21-02_132(Trip).pkl', 'ab21-02_150.pkl', 'ab21-11_24(27;32트립).pkl', 'ab21-11_88(4;08트립).pkl', 'ab21-12_16.pkl', 'ab21-12_38 (05;28트립).pkl', 'ab23-01_10024(01;02trip).pkl', 'ab23-01_30024(1;00_trip).pkl', 'ab23-03-16.pkl', 'ab23-03-95.pkl', 'ab23-06_10004(03;17_trip).pkl', 'ab23-06_30032(52s trip).pkl', 'ab59-02-1013.pkl', 'ab59-02-1073.pkl', 'ab60-02_57.pkl', 'ab60-02_210.pkl', 'ab63-02_3.pkl', 'ab63-04_124.pkl', 'ab63-04_335.pkl']

    train_x = np.concatenate([db[_]['train_x_db'] for _ in db.keys() if not _ in test_db])
    train_y = np.concatenate([db[_]['train_y_db'] for _ in db.keys() if not _ in test_db])
    test_x = np.concatenate([db[_]['train_x_db'] for _ in db.keys() if _ in test_db])
    test_y = np.concatenate([db[_]['train_y_db'] for _ in db.keys() if _ in test_db])
    print('데이터 구축 완료')
    print(np.shape(train_x))
    depth = 15
    # model = XGBClassifier(objective='multi:softmax', eta=0.1, max_depth=depth, num_rounds=100, eval_metrics='auc')
    # model = lightgbm.LGBMClassifier(learning_rate=0.001,objective='multiclassova', num_leaves=depth**2, max_depth=depth, n_estimators=100, boosting_type='dart', class_weight='balanced', subsample=0.8)
    params = {}
    params['learning_rate'] = 0.01
    params['boosting_type'] = 'goss'  # GradientBoostingDecisionTree
    params['objective'] = 'multiclassova'  # Multi-class target feature
    params['metric'] = 'multi_logloss'  # metric for multi-class
    params['max_depth'] = depth
    params['num_leaves'] = 2**depth
    params['num_class'] = 16
    params['min_data_in_leaf'] = 128
    # params['bagging_fraction'] = 0.8
    # params['bagging_freq'] = 10
    params['feature_fraction'] = 1
    params['max_bin'] = 256
    # params['reg_sqrt'] = True
    d_train = lgb.Dataset(train_x, label=np.argmax(train_y, axis=1))
    model = lgb.train(params, d_train, 500)
    print('모델 훈련 시작')
    # model.fit(train_x, np.argmax(train_y, axis=1))
    print('모델 훈련 완료')
    pickle.dump(model, open(f'XGB_max_depth/Lightgbm_max_depth_{depth}.h5', 'wb'))
    y_pred = model.predict(test_x)
    result = confusion_matrix(np.argmax(test_y, axis=1), np.argmax(y_pred, axis=1))
    print(result)
    # d_test = lgb.Dataset(test_x, label=np.argmax(test_y, axis=1))
    # disp = plot_confusion_matrix(model, test_x, np.argmax(test_y, axis=1))
    # disp = ConfusionMatrixDisplay(confusion_matrix=result,display_labels=np.argmax(train_y, axis=1))
    # disp = disp.plot(include_values=include_values, cmap=cmap, ax=ax, xticks_rotation=xticks_rotation)
    # plt.plot(y_pred)
    # plt.plot(np.argmax(test_y,axis=1))
    # print(disp.confusion_matrix)
    # plt.figure(figsize=(10,7))
    # sn.heatmap(disp.confusion_matrix, annot=True, fmt='d', annot_kws={"size": 10})
    # lightgbm.plot_importance(model)
    # lightgbm.plot_tree(model)
    # plt.show(disp)

elif type==5:
    with open('DataBase/CNS_LSTM_16Procedure.bin', 'rb') as f:
        db = pickle.load(f)
    test_db = ['ab15-07_1016.pkl', 'ab15-07_1035.pkl', 'ab15-08_1063.pkl', 'ab15-08_1089.pkl', 'ab19-02_01 (04;42트립).pkl', 'ab19-02_44(2;57trip).pkl', 'ab19-02-6(트립x).pkl', 'ab20-04_8.pkl', 'ab20-04_13.pkl', 'ab21-01_158.pkl', 'ab21-01_168.pkl', 'ab21-02_132(Trip).pkl', 'ab21-02_150.pkl', 'ab21-11_24(27;32트립).pkl', 'ab21-11_88(4;08트립).pkl', 'ab21-12_16.pkl', 'ab21-12_38 (05;28트립).pkl', 'ab23-01_10024(01;02trip).pkl', 'ab23-01_30024(1;00_trip).pkl', 'ab23-03-16.pkl', 'ab23-03-95.pkl', 'ab23-06_10004(03;17_trip).pkl', 'ab23-06_30032(52s trip).pkl', 'ab59-02-1013.pkl', 'ab59-02-1073.pkl', 'ab60-02_57.pkl', 'ab60-02_210.pkl', 'ab63-02_3.pkl', 'ab63-04_124.pkl', 'ab63-04_335.pkl']
    train_x = np.concatenate([db[_]['train_x_db'] for _ in db.keys() if not _ in test_db])
    train_y = np.concatenate([db[_]['train_y_db'] for _ in db.keys() if not _ in test_db])
    test_x = np.concatenate([db[_]['train_x_db'] for _ in db.keys() if _ in test_db])
    test_y = np.concatenate([db[_]['train_y_db'] for _ in db.keys() if _ in test_db])
    print('데이터 구축 완료')

    in_pa = np.shape(train_x)[-1] #46
    ou_pa = np.shape(train_y)[-1]  # 21
    time_leg = np.shape(train_x)[1] #10
    print(in_pa, time_leg, ou_pa)


    from sklearn.utils import class_weight

    class_weights = class_weight.compute_class_weight('balanced', np.unique(np.argmax(train_y, axis=1)), np.argmax(train_y, axis=1))
    print(class_weights)



    state = Input(batch_shape=(None, time_leg, in_pa))
    shared = LSTM(256, activation='relu')(state)
    shared = Dropout(0.5)(shared)
    # shared = LSTM(256, activation='relu', return_sequences=False)(shared)
    # shared = Dense(64)(shared)
    # shared = Dense(128, activation='relu', kernel_initializer='glorot_uniform')(shared)
    # shared = Dropout(0.5)(shared)
    fin_out = Dense(ou_pa, activation='softmax', kernel_initializer='glorot_uniform')(shared)
    network = Model(inputs=state, outputs=fin_out)
    network.summary()
    network.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    epoch = 100
    for _ in range(epoch):
        history = network.fit(train_x, train_y, batch_size=64, epochs=1, verbose=1, shuffle=True, class_weight=class_weights)
        pickle.dump(network, open(f'LSTM_network/LSTM_AB_procedure_epoch_{_+1}_{history.history["acc"]}.h5', 'wb'))
        predict = network.predict(test_x)
        matrix = confusion_matrix(test_y.argmax(axis=1), predict.argmax(axis=1))
        # disp = confusion_matrix(network, test_x, np.argmax(test_y, axis=1))
        # plt.plot(y_pred)
        # plt.plot(np.argmax(test_y, axis=1))
        # print(disp.confusion_matrix)
        # plt.figure(figsize=(10, 7))
        # print([matrix])
        sn.heatmap(matrix, annot=True, fmt='d', annot_kws={"size": 3})
        plt.tight_layout()
        plt.savefig(f'heatmap_{_+1}epoch_128__LSTM_128_Dense_Dropout_o_classweight_o.png', format='png', dpi=300)
        plt.close()


