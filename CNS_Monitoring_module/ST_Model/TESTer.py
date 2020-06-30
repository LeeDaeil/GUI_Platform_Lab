import pickle

with open('YH_0_scaler.pkl', 'rb') as f:
    temp = pickle.load(f)
print(temp.min_)