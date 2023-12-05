# import numpy as np
# import pandas as pd
# from sklearn import metrics 
# import warnings
# import joblib
# warnings.filterwarnings('ignore')
# from feature import FeatureExtraction

# file = open("pickle/rnn_model.pkl","rb")
# rnn = joblib.load(file)
# print(rnn)

# file.close()

# url = 'www.bookbitches.com'
# obj = FeatureExtraction(url)
# x = np.array(obj.getFeaturesList()).reshape(1,30) 
# print(x)
