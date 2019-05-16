import numpy as np
import pandas as pd

from spiders import GUI


def run(list1):

    p = list1[0]
    print(p)
    s= list1[1]
    print(s)
    g = list1[2]
    print(g)
    r = list1[3]
    print(r)
    h = list1[4]
    print(h)

    data = pd.read_csv("Dell.csv")
    dataset = data.dropna()
    X = dataset.iloc[:, 1:6].values
    y = dataset.iloc[:,6].values

 #   Encode Categorical data
 #    from sklearn.preprocessing import LabelEncoder
 #    labelencoder_X = LabelEncoder()
 #    X[:, 1] = labelencoder_X.fit_transform(X[:,1])
 #    onehotencoder = OneHotEncoder(categorical_features=[1])
 #    X = onehotencoder.fit_transform(X).toarray()


    from sklearn.linear_model import LinearRegression
    regressor1 = LinearRegression()
    regressor1.fit(X,y)

    from sklearn.ensemble import RandomForestClassifier
    regressor = RandomForestClassifier(n_estimators=100, criterion='entropy', random_state= 0)
    regressor.fit(X,y)

    print(regressor1.predict([[5,15.6,7,4,1]]))
    #print(regressor1.predict([[p,s,g,r,h]]))
    return regressor1.predict([[p,s,g,r,h]])
    # if p == 3:
    #     r = regressor1.predict([[3,s ,g ,r ,h]])
    #     print(r)
    #     return r
    # if p == 5:
    #     r = regressor1.predict([[4,s ,g ,r ,h]])
    #     print(r)
    #     return r
    # if p == 7:
    #     r = regressor1.predict([[5,s ,g ,r ,h]])
    #     print(r)
    #     return r




def ML():
    GUI.next()


if __name__ == "__main__":
    ML()
