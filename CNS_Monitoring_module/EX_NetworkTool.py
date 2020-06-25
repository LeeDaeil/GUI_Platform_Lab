from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
import pickle


class NetTool:
    def __init__(self):
        # ==== 스케일러
        self.scaler = self.make_scaler()
        self.ParaList = self.make_paralist()
        self.NetBox = self.make_net()

    def make_paralist(self):
        # paralist = pd.read_csv('PARKJIHUN/MIN_MAX/Final_parameter.csv')['0'].tolist()
        paralist = ['UAVLEG1', 'UAVLEG2', 'UAVLEG3', 'ZINST58', 'ZINST75', 'ZINST30', 'ZINST78', 'ZINST74',
                    'WFWLN1', 'WFWLN2', 'WFWLN3', 'ZINST26', 'ZINST22', 'BFV122', 'URHXUT', 'ZINST56', 'KBCDO23']
        return paralist

    def make_scaler(self):
        """
        Make scaler
        :return: scaler
        """
        # scaler = MinMaxScaler()
        # min_value = pd.read_csv('PARKJIHUN/MIN_MAX/min_value_final.csv')
        # max_value = pd.read_csv('PARKJIHUN/MIN_MAX/max_value_final.csv')
        # scaler.fit([min_value['0'], max_value['0']])

        with open('scaler.pkl', 'rb') as f:
            scaler = pickle.load(f)

        return scaler

    def make_input_window(self, db):
        """

        :param db: Get from DATA
        :return: Return input data based on self.ParaList
        """

        # db['key']['V']
        one_input_window = np.array([db[key]['V'] for key in self.ParaList])
        one_input_window = self.scaler.transform(np.reshape(one_input_window, (1, len(one_input_window))))
        return one_input_window

    def make_input_window_ST(self, db):
        one_input_window = np.array([db[key]['V'] for key in self.ParaList])
        one_input_window = self.scaler.transform(np.reshape(one_input_window, (1, len(one_input_window))))
        return one_input_window

    def make_net(self):
        import tensorflow as tf
        # self.timesteps = 10
        # self.input_dim = 46
        # self.units = 64  # choosen unit number randomly
        #
        # inputs = tf.keras.Input(shape=(self.timesteps, self.input_dim))
        # encoded = tf.keras.layers.LSTM(self.input_dim, return_sequences=False, name="encoder")(inputs)
        # encoded = tf.keras.layers.Dropout(0.5)(encoded)
        # decoded = tf.keras.layers.RepeatVector(self.timesteps)(encoded)
        # decoded = tf.keras.layers.Dropout(0.5)(decoded)
        # decoded = tf.keras.layers.LSTM(self.input_dim, return_sequences=True, name='decoder')(decoded)
        # autoencoder = tf.keras.models.Model(inputs, decoded)

        inputs = tf.keras.Input(len(self.ParaList))
        hiden = tf.keras.layers.Dense(300, activation='relu')(inputs)
        hiden1 = tf.keras.layers.Dense(300)(hiden)
        hiden2 = tf.keras.layers.Dense(300)(hiden1)
        output = tf.keras.layers.Dense(5, activation='softmax')(hiden2)
        model = tf.keras.models.Model(inputs,output)

        # model.save_weights('TESTW.h5')

        model.load_weights('save_model.h5')


        return model