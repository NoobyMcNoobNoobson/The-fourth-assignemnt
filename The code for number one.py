import seaborn as sns 
import pandas as pd 
import matplotlib as plt
import os
from os import path

def main():
    surverys_df = pd.read_csv('surveys.csv')
    sns.set()
    sns.relplot(x = 'weight',y='hindfoot_length',data = surverys_df,kind= 'scatter')
    #Every data point represents two things:- 1. Weight and 2. Hindfoot length 
    # it seems the data had two dense clusters of data points that are there thansk to some correlation, 
    #let's see if we can find what correlatation to be exact 

main()

