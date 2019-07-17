import pandas as pd
from matplotlib import pyplot as plt #gives an unfamiliar reader a hint that pyplot is a module, rather than a function which could be incorrectly assumed from the first form
from sklearn import manifold  #Manifold Learning can be thought of as an attempt to generalize linear frameworks like PCA to be sensitive to non-linear structure in data
import numpy as np
#Imports NumPy library, which adds more support for vectors and matrices, constituting a library of high level mathematical functions to operate with those vectors or matrices. And pandas, which provides tools, methods and functionality for basic data structures

def action():
    att=["ID", "LIMIT_BAL", "SEX", "EDUCATION", "MARRIAGE", "AGE", "BILL_AMT1", "BILL_AMT2", "BILL_AMT3", "BILL_AMT4", "BILL_AMT5", "BILL_AMT6", "PAY_AMT1", "PAY_AMT2", "PAY_AMT3", "PAY_AMT4", "PAY_AMT5", "PAY_AMT6", "default payment next month"] #define project attributes
    data = pd.io.parsers.read_csv('static/dataset.csv',
         delimiter=';', #it's going to read the data separated by semicolon
         header=0, # rows numbers to use as colums numbers. header=0 is the standard
# read the csv file inside the database
        );

#Standardize the characteristics by eliminating the average and the scale to the variation of the unit
    from sklearn.preprocessing import StandardScaler
    features = ["AGE", "LIMIT_BAL", "BILL_AMT1", "BILL_AMT2", "BILL_AMT3", "BILL_AMT4", "BILL_AMT5", "BILL_AMT6", "PAY_AMT1", "PAY_AMT2", "PAY_AMT3", "PAY_AMT4", "PAY_AMT5", "PAY_AMT6"]

    # Separating out the features
    x = data.loc[:, features].values
    # Separating out the target
    y = data.loc[:,['default payment next month']].values
    # Standardizing the features
    x = StandardScaler().fit_transform(x)
    from sklearn.decomposition import PCA #Principal Component Analysis
    pca = PCA(n_components=6)
    principalComponents = pca.fit_transform(x)
# Creates the data structure, columns and rows, and puts them in principalDf. The data are principalComponents and the columns X1,X2,X3,X4,X5 and X6
    principalDf = pd.DataFrame(data = principalComponents, columns = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6'])
    midDf=pd.concat([principalDf, data[["ID"]]], axis=1)
#We are defining the atributtes
    list_of_attributes=["SEX", "AGE", "EDUCATION", "MARRIAGE","LIMIT_BAL", "BILL_AMT1", "BILL_AMT2", "BILL_AMT3", "BILL_AMT4", "BILL_AMT5", "BILL_AMT6", "PAY_AMT1", "PAY_AMT2", "PAY_AMT3", "PAY_AMT4", "PAY_AMT5", "PAY_AMT6"]
#We are going to add the data of the attributes
    for elem in list_of_attributes:
        midDf=pd.concat([midDf, data[[elem]]], axis=1)
    finalDf = pd.concat([midDf, data[['default payment next month']]], axis = 1)
    finalDf=finalDf.rename(index=str, columns={"default payment next month": "target"})
    finalDf.to_csv("static/pca.csv", sep=',', index=False)
    return 0;

#main executes action()
if __name__ == "__main__":
    action()
