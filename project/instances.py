import pandas as pd
#Imports pandas, which provides tools, methods and functionality for basic data structures

def action():
    dataset="static/dataset.csv" #file handler

    att=["ID", "LIMIT_BAL", "SEX", "EDUCATION", "MARRIAGE", "AGE", "BILL_AMT1", "BILL_AMT2", "BILL_AMT3", "BILL_AMT4", "BILL_AMT5", "BILL_AMT6", "PAY_AMT1", "PAY_AMT2", "PAY_AMT3", "PAY_AMT4", "PAY_AMT5", "PAY_AMT6", "default payment next month"]
    data = pd.io.parsers.read_csv(dataset,
         delimiter=';', #it's going to read the data separated by semicolon
         header=0, # rows numbers to use as colums numbers. header=0 is the standard
# read the csv file inside the database
        );
    features = ["AGE", "LIMIT_BAL", "BILL_AMT1", "BILL_AMT2", "BILL_AMT3", "BILL_AMT4", "BILL_AMT5", "BILL_AMT6", "PAY_AMT1", "PAY_AMT2", "PAY_AMT3", "PAY_AMT4", "PAY_AMT5", "PAY_AMT6"]
    frequency_of=["SEX", "EDUCATION", "MARRIAGE", "AGE"]

#fill the rows of SEX, EDUCATION, MARRIAGE and AGE.
    for elem in frequency_of:
        table=pd.crosstab(index=data[elem], columns=data["default payment next month"])
#Compute a simple cross-tabulation of two (or more) factors. By default computes a frequency table of the factors unless an array of values and an aggregation function are passed
#index=data[elem]-> Values to group by in the rows=data[elem]
#columns=data["default payment next month"]-> Values to group by in the columns
        table.columns=["0", "1"]
        table.to_csv("static/"+elem+"_instances.csv")
    return 0;

#main
if __name__ == "__main__":
    action()
