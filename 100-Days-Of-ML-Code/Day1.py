import numpy as np
import pandas as pd
from sklearn.preprocessing import Imputer,LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split

dataset = pd.read_csv('Data.csv')
print(dataset)

X = dataset.iloc[:,:-1].values
Y= dataset.iloc[:,3].values

print('-'*50)
print(X)
print('-'*50)
print(Y)

imputer = Imputer(missing_values= "NaN", strategy="mean", axis=0)
imputer = imputer.fit(X[:,1:3])
X[:,1:3] = imputer.transform(X[:,1:3])

print(X)

labelencoder_X = LabelEncoder()
X[:,0]=labelencoder_X.fit_transform(X[:,0])
print(X)
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()
labelencoder_Y = LabelEncoder()
Y =  labelencoder_Y.fit_transform(Y)
print(X)


X_train, X_test, Y_train, Y_test = train_test_split( X , Y , test_size = 0.2, random_state = 0)


print(X_train)
print(X_test)
print(Y_train)
print(Y_test)
