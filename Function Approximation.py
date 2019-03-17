import tensorflow as tf
import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras.callbacks import EarlyStopping

rng = np.random.RandomState(1)
x = np.sort((360 * rng.rand(100, 1)), axis=0)
y = np.array([np.sin(x*(np.pi/180.0)).ravel(),np.cos(x*(np.pi/180.0)).ravel()]).T

model = Sequential()
model.add(Dense(300, input_dim=x.shape[1], activation='relu'))
model.add(Dense(100, activation='relu'))
model.add(Dense(25, activation='relu'))
model.add(Dense(2))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(x,y,verbose=0,batch_size=len(x),epochs=25000)

pred = model.predict(x)

print("Actual")
print(y[20:25])

print("Pred")
print(pred[20:25])

chart_regression(pred.flatten(),y,sort=False)