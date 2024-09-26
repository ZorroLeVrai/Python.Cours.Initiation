import pandas as pd

def hello():
    print("HELLO!")

def get_dataframes():
    df_eleves = pd.read_csv(r"D:\Users\amine\Documents\GitHub\Python.Cours.Initiation\Librairies\eleves.csv",
                            encoding="latin-1")
    return [df_eleves]


EULER = 2.71
