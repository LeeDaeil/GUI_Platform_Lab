import tensorflow as tf
import numpy as np

inputs = tf.keras.Input(23)
hiden = tf.keras.layers.Dense(300, activation='relu')(inputs)
hiden1 = tf.keras.layers.Dense(300)(hiden)
hiden2 = tf.keras.layers.Dense(300)(hiden1)
output = tf.keras.layers.Dense(5, activation='softmax')(hiden2)
model = tf.keras.models.Model(inputs, output)

model.load_weights('ST_Model/YH_1_save_model.h5')

print(model.layers[0].output)

temp = []
for _ in range(1, len(model.layers)):
    temp.append(tf.keras.backend.function([model.layers[0].input], [model.layers[_].output]))


test_val = np.array([[9.81446748e-01, 9.82974666e-01, 9.83826801e-01, 9.95316382e-01,
  8.08407948e-01, 7.31126685e-02, 8.49825839e-01, 8.10492424e-01,
  5.53565882e-01, 5.71993489e-01, 5.51499926e-01, 3.92397872e-04,
  0.00000000e+00, 7.95771673e-01, 5.59074868e-01, 1.08622432e-01,
  9.90000000e-01, 9.95316382e-01, 0.00000000e+00, 0.00000000e+00,
  6.07502288e-01, 6.10586576e-01, 6.11992596e-01]])

print(model.predict(test_val))

print([temp[_](test_val) for _ in range(len(temp))])