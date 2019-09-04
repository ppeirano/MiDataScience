import pandas as pd 

def hello_world():
    print("")
    print("Hello World!")

def show_df(df):
    print(df.shape)
    print("\n")
    print(df.head())
    print("\n")
    print(df.describe())