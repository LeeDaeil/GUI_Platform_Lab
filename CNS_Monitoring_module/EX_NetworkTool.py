from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np
import pickle


class NetTool:
    def __init__(self):
        # ==== 스케일러
        self.scaler = self.make_scaler()
        self.ParaList = self.make_paralist()
        self.NetBox = [self.make_net(nub=0, path='ST_Model/HJ_0_save_model.h5'),
                       self.make_net(nub=1, path='ST_Model/YH_1_save_model.h5'),
                       self.make_net(nub=2, path='ST_Model/YC_2_save_model.h5'),
                       self.make_net(nub=3, path='ST_Model/SH_3_save_model.h5'),
                       self.make_net(nub=4, path='ST_Model/MH_4_save_model.h5'),
                       self.make_net(nub=5, path='ST_Model/JSH_5_save_model.h5'),
                       self.make_net(nub=6, path='ST_Model/SJ_6_save_model.h5'),
                       self.make_net(nub=7, path='ST_Model/EJ_7_save_model.h5'),
                       self.make_net(nub=8, path='ST_Model/SG_8_save_model.h5'),
                       ]

    def make_paralist(self):
        # paralist = pd.read_csv('PARKJIHUN/MIN_MAX/Final_parameter.csv')['0'].tolist()
        paralist = []
        # Model 0
        # paralist.append(['UAVLEG1', 'UAVLEG2', 'UAVLEG3', 'ZINST58', 'ZINST75', 'ZINST73', 'ZINST74','ZINST30', 'ZINST78',
        #                  'WFWLN1', 'WFWLN2', 'WFWLN3', 'ZINST26', 'ZINST22', 'BFV122','URHXUT','ZINST56','KBCDO23',
        #                  'ZINST65', 'ZINST22', 'DSECON', 'WSTM1', 'WSTM2', 'WSTM3', 'KFAST', 'KSLOW','BPORV',
        #                  'UNRHXUT'])
        paralist.append(['ZINST101', 'ZINST102', 'WSTM1', 'WSTM2', 'WSTM3', 'ZINST78',
        'ZINST77', 'ZINST76', 'ZINST72', 'ZINST71', 'ZINST70', 'ZINST75',
        'ZINST74', 'ZINST73', 'ZINST58', 'ZINST56', 'UPRT', 'ZINST63', 'KBCDO15',
        'ZINST26', 'ZINST22', 'UCTMT', 'WFWLN1', 'WFWLN2', 'WFWLN3', 'BPORV','ZINST22',
        'KLAMPO147', 'KLAMPO148', 'KLAMPO149', 'ZINST36', 'KLAMPO9', 'KFAST', 'KLAMPO70','DSECON'])

        # Model 1
        paralist.append(['UAVLEG1', 'UAVLEG2', 'UAVLEG3', 'ZINST58', 'ZINST75', 'ZINST73', 'ZINST74','ZINST30', 'ZINST78',
        'WFWLN1', 'WFWLN2', 'WFWLN3', 'ZINST26', 'ZINST22', 'BFV122','URHXUT','ZINST56','KBCDO23',
        'ZINST65', 'ZINST22', 'DSECON', 'WSTM1', 'WSTM2', 'WSTM3', 'KFAST', 'KSLOW','BPORV',
        'UNRHXUT','WFPLN1','WFPLN2','WFPLN3','WTIN','BFV499', 'BFV489', 'BFV479'])

        # Model 2
        paralist.append(
            ['ZINST101', 'ZINST102', 'WSTM1', 'WSTM2', 'WSTM3', 'ZINST78',
             'ZINST77', 'ZINST76', 'ZINST72', 'ZINST71', 'ZINST70', 'ZINST75',
             'ZINST74', 'ZINST73', 'ZINST58', 'ZINST56', 'UPRT', 'ZINST63', 'KBCDO15',
             'ZINST26', 'ZINST22', 'UCTMT', 'WFWLN1', 'WFWLN2', 'WFWLN3', 'BPORV',
             'KLAMPO147', 'KLAMPO148', 'KLAMPO149', 'ZINST36', 'KLAMPO9', 'KFAST', 'KLAMPO70'
             ])

        # Model 3
        paralist.append(['ZINST69', 'ZINST58', 'KLAMPO118', 'KLAMPO143', 'BHV302', 'Normal_0', 'KLAMPO337', 'KLAMPO312', 'KBCDO15', 'KFAST',
        'ZINST81', 'ZINST80', 'WSTM1', 'WSTM2', 'WSTM3', 'WFWLN1', 'WFWLN2', 'WFWLN3', 'ZINST22', 'DSECON', 'UCTMT',
        'KLAMPO312', 'ZINST101', 'ZINST102', 'ZINST78', 'ZINST77', 'ZINST76', 'ZINST72', 'ZINST71', 'ZINST70', 'BPORV',
        'ZINST75', 'KLAMPO57', 'KLAMPO64', 'KLAMPO241', 'KLAMPO230', 'KLAMPO152', 'KLAMPO22', 'KLAMPO9', 'KLAMPO6', 'KLAMPO21'])

        # Model 4
        paralist.append(['BPSV10','KLAMPO118','BTV418','BPORV','KLAMPO143',
        'BHV108','BHV308','UFUEL10','CAUTRDC','ZSGLS','WMLOCA',
        'QPRZB','PPRZLP','VSUMP','DCTMT','QPRZP','QPRZB','QPRZ',
        'XSMINJ','WRHSTM','WRHDT','WLPTC','WHPRH','WHPT','VNET',
        'YNET', 'ZINST22', 'DSECON','WFWLN1', 'WFWLN2', 'WFWLN3'])

        # Model 5
        paralist.append(['BPSV10','KLAMPO118','BTV418','BPORV','KLAMPO143',
        'BHV108','BHV308','UFUEL10','CAUTRDC','ZSGLS','WMLOCA',
        'QPRZB','PPRZLP','VSUMP','DCTMT','QPRZP','QPRZB','QPRZ',
        'XSMINJ','WRHSTM','WRHDT','WLPTC','WHPRH','WHPT','VNET',
        'YNET', 'ZINST22', 'DSECON','WFWLN1', 'WFWLN2', 'WFWLN3', 'KLAMPO57', ])

        # Model 6
        paralist.append(['ZINST101', 'ZINST102', 'WSTM1', 'WSTM2', 'WSTM3', 'ZINST78',
        'ZINST77', 'ZINST76', 'ZINST72', 'ZINST71', 'ZINST70', 'ZINST75',
        'ZINST74', 'ZINST73', 'ZINST58', 'ZINST56', 'UPRT', 'ZINST63', 'KBCDO15',
        'ZINST26', 'ZINST22', 'UCTMT', 'WFWLN1', 'WFWLN2', 'WFWLN3', 'BPORV',
        'KLAMPO147', 'KLAMPO148', 'KLAMPO149', 'ZINST36', 'KLAMPO9', 'KFAST', 'KLAMPO70'])

        # Model 7
        paralist.append(['ZINST101', 'ZINST102', 'WSTM1', 'WSTM2', 'WSTM3', 'ZINST78',
        'ZINST77', 'ZINST76', 'ZINST72', 'ZINST71', 'ZINST70', 'ZINST75',
        'ZINST74', 'ZINST73', 'ZINST58', 'ZINST56', 'UPRT', 'ZINST63', 'KBCDO15',
        'ZINST26', 'ZINST22', 'UCTMT', 'WFWLN1', 'WFWLN2', 'WFWLN3', 'BPORV',
        'KLAMPO147', 'KLAMPO148', 'KLAMPO149', 'ZINST36', 'KLAMPO9', 'KFAST', 'KLAMPO70'])

        # Model 8
        paralist.append(['ZINST101', 'ZINST102', 'WSTM1', 'WSTM2', 'WSTM3', 'ZINST78',
        'ZINST77', 'ZINST76', 'ZINST72', 'ZINST71', 'ZINST70', 'ZINST75',
        'ZINST74', 'ZINST73', 'ZINST58', 'ZINST56', 'UPRT', 'ZINST63', 'KBCDO15',
        'ZINST26', 'ZINST22', 'UCTMT', 'WFWLN1', 'WFWLN2', 'WFWLN3', 'BPORV',
        'KLAMPO147', 'KLAMPO148', 'KLAMPO149', 'ZINST36', 'KLAMPO9', 'KFAST', 'KLAMPO70'])

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
        scaler = []
        with open('ST_Model/HJ_0_scaler.pkl', 'rb') as f:
            scaler.append(pickle.load(f))
        with open('ST_Model/YH_1_scaler.pkl', 'rb') as f:
            scaler.append(pickle.load(f))
        with open('ST_Model/YC_2_scaler.pkl', 'rb') as f:
            scaler.append(pickle.load(f))
        with open('ST_Model/YC_2_scaler.pkl', 'rb') as f:
            scaler.append(pickle.load(f))
        with open('ST_Model/YC_2_scaler.pkl', 'rb') as f:
            scaler.append(pickle.load(f))
        with open('ST_Model/YC_2_scaler.pkl', 'rb') as f:
            scaler.append(pickle.load(f))
        with open('ST_Model/SJ_6_scaler.pkl', 'rb') as f:
            scaler.append(pickle.load(f))
        with open('ST_Model/EJ_7_scaler.pkl', 'rb') as f:
            scaler.append(pickle.load(f))
        with open('ST_Model/SG_8_scaler.pkl', 'rb') as f:
            scaler.append(pickle.load(f))
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

    def make_input_window_ST(self, nub, db):
        one_input_window = np.array([db[key]['V'] for key in self.ParaList[nub]])
        if nub == 3 or nub == 4 or nub == 5:
            one_input_window = np.reshape(one_input_window, (1, len(one_input_window)))
        else:
            one_input_window = self.scaler[nub].transform(np.reshape(one_input_window, (1, len(one_input_window))))
        return one_input_window

    def make_net(self, nub, path):
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

        inputs = tf.keras.Input(len(self.ParaList[nub]))
        if nub == 0:
            hiden = tf.keras.layers.Dense(500)(inputs)
            hiden = tf.keras.layers.Dense(150)(hiden)
            # hiden = tf.keras.layers.Dense(150, activation='relu')(inputs)
            # hiden1 = tf.keras.layers.Dense(150)(hiden)
            # hiden = tf.keras.layers.Dense(150)(hiden1)
        elif nub == 1:
            hiden = tf.keras.layers.Dense(150, activation='relu')(inputs)
            hiden = tf.keras.layers.Dense(150, activation='relu')(hiden)
            hiden = tf.keras.layers.Dense(150)(hiden)
            hiden = tf.keras.layers.Dense(100)(hiden)
        elif nub == 2:
            hiden = tf.keras.layers.Dense(200, activation='relu')(inputs)
            hiden1 = tf.keras.layers.Dense(100)(hiden)
            hiden = tf.keras.layers.Dense(50)(hiden1)
        elif nub == 3:
            hiden = tf.keras.layers.Dense(100)(inputs)
            hiden = tf.keras.layers.Dense(100)(hiden)
        elif nub == 4:
            hiden = tf.keras.layers.Dense(200)(inputs)
            hiden = tf.keras.layers.Dense(200)(hiden)
            hiden = tf.keras.layers.Dense(200)(hiden)
        elif nub == 5:
            hiden = tf.keras.layers.Dense(200)(inputs)
            hiden = tf.keras.layers.Dense(200)(hiden)
            hiden = tf.keras.layers.Dense(200)(hiden)
        elif nub == 6:
            hiden = tf.keras.layers.Dense(300, activation='relu')(inputs)
            hiden = tf.keras.layers.Dense(150, activation='relu')(hiden)
        elif nub == 7:
            hiden = tf.keras.layers.Dense(300, activation='relu')(inputs)
            hiden = tf.keras.layers.Dense(200, activation='relu')(hiden)
        elif nub == 8:
            hidden = tf.keras.layers.Dense(300, activation='relu')(inputs)
            hiden = tf.keras.layers.Dense(200, activation='relu')(hidden)

        output = tf.keras.layers.Dense(5, activation='softmax')(hiden)
        model = tf.keras.models.Model(inputs, output)

        model.load_weights(filepath=path)

        return model