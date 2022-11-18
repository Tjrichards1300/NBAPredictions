import pandas as pd

def getColDict():
    with open('../../data/Rolling15Games.csv', 'r') as f: 
        df = pd.read_csv(f)
    df.drop('home_win',axis=1,inplace=True)    
    cols = df.columns
    col_dict = {}
    i = 0
    for i,col in enumerate(df.columns):
        col_dict[col] = i 
    return col_dict