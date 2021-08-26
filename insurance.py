import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv('insurance.csv')
dataset=pd.get_dummies(dataset,drop_first=True)
dataset.head()
X = dataset.loc[:,['age','bmi','children','sex_male','smoker_yes','region_northwest','region_southeast','region_southwest']].values
y = dataset.loc[:,['expenses']].values
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
       X, y,test_size = 0.2, random_state=0)
from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators = 10, random_state = 0)
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
np.set_printoptions(precision=2)
print(np.concatenate((y_pred.reshape(len(y_pred),1), y_test.reshape(len(y_test),1)),1))
from sklearn.metrics import r2_score
r2_score(y_test, y_pred)
import pickle
file = open('insurance.pkl', 'wb')
pickle.dump(regressor, file)















