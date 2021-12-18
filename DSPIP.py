# -*- coding: utf-8 -*-
"""
Created on Thu Dec 16 16:01:22 2021

@author: Ranoo
"""
import numpy as np
import pandas as pd
import functools

# Reading an excel file using Python
import xlrd

 
# Give the location of the file
loc = ("Iris.xlsx")
 
# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

sheet2 = np.array(sheet)


df = pd.read_excel("Iris.xlsx")
#df.as_matrix()

df2 = df.drop('#',axis=1)
df2.plot()

#Sertosa = I1;  Veriscolor = I2;  Verginica =I3


I1_mean = df[0:50].mean()[1:]
I1_std  = df[0:50].std()[1:]

I2_mean = df[50:100].mean()[1:]
I2_std  = df[50:100].std()[1:]

I3_mean = df[100:].mean()[1:]
I3_std  = df[100:].std()[1:]


def naive_bayes(traits):
    #This function receives a list with the 4 properties of the Iris flower:
    # sepal and petal width and length
    # and returns the type of flower that is the most probable one
    # This function relys on the Naive Bayes method
    # Based on the mean and standard deviations of the data of each property for each flower:
    # it calculates the pseudo probabilities of the flower to belong to each of the types:
    # Iris Setoas, Iris Veriscolor or Iris Virginica
    # The values calculated are not probabilities, as they can be greater than 1.
    # However, they do represent probabilities when normalizing each value by the sum of the three pseudo probabilities
    
    P_I1 = np.zeros(4)
    P_I2 = np.zeros(4)
    P_I3 = np.zeros(4)
    
    x = 0
    for trait in traits:
        P_I1[x] = 1/np.sqrt(2 * np.pi * I1_std[x] ** 2) * np.exp(-(trait - I1_mean[x]) ** 2 / (2 * I1_std[x]) ** 2)
        P_I2[x] = 1/np.sqrt(2 * np.pi * I2_std[x] ** 2) * np.exp(-(trait - I2_mean[x]) ** 2 / (2 * I2_std[x]) ** 2)
        P_I3[x] = 1/np.sqrt(2 * np.pi * I3_std[x] ** 2) * np.exp(-(trait - I3_mean[x]) ** 2 / (2 * I2_std[x]) ** 2)
        x += 1
    P_I1 = functools.reduce(lambda x, y: x * y, P_I1)
    P_I2 = functools.reduce(lambda x, y: x * y, P_I2)
    P_I3 = functools.reduce(lambda x, y: x * y, P_I3)
    
    results = [P_I1, P_I2, P_I3]
    
    Iris = ['I.setosa', 'I.veriscolor', 'I.virginica']
    
    return 'The flower is probably ' + Iris[np.argmax(results)]
    
def knn(traits, neighbors):
    #This function receives a list with the 4 properties of the Iris flower:
    # sepal and petal width and length
    # and a number that determines the number of nearest neighbors
    # and returns the type of flower that is the most probable one, according to the KNN method
    df["distance"] = (traits[0] - df["Sepal length"]) ** 2 + \
                 (traits[1] - df["Sepal width" ]) ** 2 + \
                 (traits[2] - df["Petal length"]) ** 2 + \
                 (traits[3] - df["Petal width" ]) ** 2 
                       
    df2 = df.sort_values("distance")
    return 'The flower is probably ' + list(df2[0:neighbors]["Species"].value_counts().index)[0]

    
    
test_traits = [5, 3, 1.4, 0.2]
print(naive_bayes(test_traits))
print(knn(test_traits, 30))

test_traits = [7, 3, 4.5, 1.5]
print(naive_bayes(test_traits))
print(knn(test_traits, 30))

test_traits = [7, 4, 7, 2]
print(naive_bayes(test_traits))
print(knn(test_traits, 30))

