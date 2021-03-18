import seaborn as sns 
import pandas as pd 
import matplotlib as plt
import os
from os import path

def the_two_clouds():
    surverys_df = pd.read_csv('surveys.csv')
    species_df = pd.read_csv('species.csv')
    sns.set()
    sns.relplot(x = 'weight',y='hindfoot_length',data = surverys_df,kind= 'scatter')
    #Every data point represents two things:- 1. Weight and 2. Hindfoot length 
    # it seems the data had two dense clusters of data points that are there thansk to some correlation, 
    #let's see if we can find what correlatation to be exact 
    left_merge = pd.merge(left = surverys_df, right = species_df, how ='left', left_on='species_id',right_on ='species_id')
    print(left_merge.head(1))
    list_of_bottom_cloud_species = ['albigula','baileyi','eremicus','fulviventer','hispidus','merriami']
    list_of_top_cloud_species = ['spectabilis','spilosoma','taylori']

    left_merge.species.isin(list_of_top_cloud_species)
    left_merge.species.isin(list_of_top_cloud_species)
    
    filter_by_bottom_cloud = left_merge[left_merge.species.isin(list_of_bottom_cloud_species)]

    filter_by_top_cloud = left_merge[left_merge.species.isin(list_of_top_cloud_species)]


    print('The following is the filtered bottom cloud')
    sns.relplot(x = 'weight',y='hindfoot_length',data = filter_by_bottom_cloud,kind= 'scatter')
    
    print('The following is the filtered top cloud:-')

    sns.relplot(x = 'weight',y='hindfoot_length',data =filter_by_top_cloud ,kind= 'scatter')

    species_grouped_df = left_merge.groupby(['species'])['weight'].mean()
    print(species_grouped_df)

def violin_plot():
    surverys_df = pd.read_csv('surveys.csv')
    by_size_df = pd.DataFrame(surverys_df,columns = ['species_id'])
    print(by_size_df)
#the_two_clouds()
violin_plot()




