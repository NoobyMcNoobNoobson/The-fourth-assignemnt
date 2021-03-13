import seaborn as sns 
import pandas as pd 
import matplotlib as plt
import os
from os import path

def main():
    surverys_df = pd.read_csv('surveys.csv')
    sns.set()
    sns.relplot(x = 'weight',y='hindfoot_length',data = surverys_df,kind= 'scatter')

main()

