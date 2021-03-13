import seaborn as sns 
import pandas as pd 
import matplotlib as plt
import os
from os import path

def main():
    surverys_df = pd.read_csv('surveys.csv')
    weight_and_hindfoot_df = surverys_df.groupby(['weight','hindfoot_length'])
    print(weight_and_hindfoot_df.shape)

main()

