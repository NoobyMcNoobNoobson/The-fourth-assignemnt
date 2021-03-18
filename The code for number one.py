import seaborn as sns 
import pandas as pd 
import matplotlib as plt
import os
from os import path

def main():
    surverys_df = pd.read_csv('surveys.csv')
    species_df = pd.read_csv('species.csv')
    sns.set()
    sns.relplot(x = 'weight',y='hindfoot_length',data = surverys_df,kind= 'scatter')
    #Every data point represents two things:- 1. Weight and 2. Hindfoot length 
    # it seems the data had two dense clusters of data points that are there thansk to some correlation, 
    #let's see if we can find what correlatation to be exact 
    left_merge = pd.merge(left = surverys_df, right = species_df, how ='left', left_on='species_id',right_on ='species_id')
    print(left_merge.head(1))
    filter_by_albigula_df = left_merge[left_merge.species == 'albigula']
    filter_by_baileyi_df = left_merge[left_merge.species == 'baileyi']
    #print(filter_by_species_df.shape)
    sns.relplot(x = 'weight',y='hindfoot_length',data = filter_by_albigula_df,kind= 'scatter')
    sns.relplot(x = 'weight',y='hindfoot_length',data = filter_by_baileyi_df,kind= 'scatter')
    #species_grouped_df = left_merge.groupby(['species'])['weight'].mean()
    #print(species_grouped_df)

main()

