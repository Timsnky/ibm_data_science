import matplotlib.pyplot as plt
import pandas as pd
import pylab as pl
import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score

df = pd.read_csv("FuelConsumption.csv")
# print(df.head())
# print(df.describe())

cdf = df[['ENGINESIZE','CYLINDERS','FUELCONSUMPTION_COMB','CO2EMISSIONS']]
# print(cdf.head(9))
# cdf.hist()
# plt.show()

# # Plot fuel consumption vs co2emissions
# plt.scatter(cdf.FUELCONSUMPTION_COMB, cdf.CO2EMISSIONS,  color='blue')
# plt.xlabel("Fuel Consumption")
# plt.ylabel("Emission")
# plt.show()
#
# # Plot engine size vs co2emissions
# plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS,  color='blue')
# plt.xlabel("Engine size")
# plt.ylabel("Emission")
# plt.show()
#
# # Plot Cylinders vs co2emissions
# plt.scatter(cdf.CYLINDERS, cdf.CO2EMISSIONS,  color='blue')
# plt.xlabel("Cylinders")
# plt.ylabel("Emission")
# plt.show()

#Split Training and Test Set Data
msk = np.random.rand(len(df)) < 0.8
train = cdf[msk]
test = cdf[~msk]

# # Plot engine size vs co2emissions for training data
# plt.scatter(train.ENGINESIZE, train.CO2EMISSIONS,  color='blue')
# plt.xlabel("Engine size")
# plt.ylabel("Emission")
# plt.show()

# Liner Regression Modelling
regr = linear_model.LinearRegression()
train_x = np.asanyarray(train[['ENGINESIZE']])
train_y = np.asanyarray(train[['CO2EMISSIONS']])
regr.fit (train_x, train_y)
# The coefficients
print ('Coefficients: ', regr.coef_)
print ('Intercept: ',regr.intercept_)

#Error Evaluation
test_x = np.asanyarray(test[['ENGINESIZE']])
test_y = np.asanyarray(test[['CO2EMISSIONS']])
test_y_hat = regr.predict(test_x)

print("Mean absolute error: %.2f" % np.mean(np.absolute(test_y_hat - test_y)))
print("Residual sum of squares (MSE): %.2f" % np.mean((test_y_hat - test_y) ** 2))
print("R2-score: %.2f" % r2_score(test_y_hat , test_y) )


