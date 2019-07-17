import pandas as pd
import numpy as np 
#Imports NumPy library, which adds more support for vectors and matrices, constituting a library of high level mathematical functions to operate with those vectors or matrices. And pandas, which provides tools, methods and functionality for basic data structures


def action():
    att=["X1", "X2", "X3", "X4", "X5", "X6", "ID", "SEX", "AGE", "EDUCATION", "MARRIAGE", "LIMIT_BAL", "BILL_AMT1", "BILL_AMT2", "BILL_AMT3", "BILL_AMT4", "BILL_AMT5", "BILL_AMT6", "PAY_AMT1", "PAY_AMT2", "PAY_AMT3", "PAY_AMT4", "PAY_AMT5", "PAY_AMT6", "target"] # define project attributes
    data = pd.io.parsers.read_csv('static/pca.csv', # file handler
         delimiter=',', # it's going to read the data separated by coma
         header=0,  # rows numbers to use as colums numbers. header=0 is the standard
# read the csv file inside the database
        );

    from sklearn.preprocessing import StandardScaler #Standardize the characteristics by eliminating the average and the scale to the variation of the unit


    features = ["BILL_AMT1", "BILL_AMT2", "BILL_AMT3", "BILL_AMT4", "BILL_AMT5", "BILL_AMT6", "PAY_AMT1", "PAY_AMT2", "PAY_AMT3", "PAY_AMT4", "PAY_AMT5", "PAY_AMT6"]

    # Separating out the features
    x = data.loc[:, features].values

    # Standardizing the features. average=0 y deviation=1.  fit_transform adjust the data and after it transforms them
    x = StandardScaler().fit_transform(x)
# Creates the data structure, columns and rows, and puts them in midDf
    standard_data_frame = pd.DataFrame(data = x, columns = features)
#empty structure of data
    midDf=pd.DataFrame()
    list_of_attributes=["X1", "X2", "X3", "X4", "X5", "X6", "ID", "SEX", "AGE", "EDUCATION", "MARRIAGE", "LIMIT_BAL"]
#concatenate list_of attributes to midDf 
    for elem in list_of_attributes:
	# reads the data separated by comas and adds them at midDf
        midDf=pd.concat([midDf, data[[elem]]], axis=1)#adds colums because axis=1, if axis=0 it adds rows
    almostFinalDF = pd.concat([midDf, standard_data_frame], axis = 1)#adds to midFf the data structure created with the features
    finalDf = pd.concat([almostFinalDF, data[["target"]]], axis = 1)
    finalDf.to_csv("static/standardized_data.csv", sep=',', index=False)
    return 0;
#main. execute action()
if __name__ == "__main__":
    action()
