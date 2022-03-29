# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 14:34:47 2022

@author: Ranoo
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Reading an excel file using Python
import xlrd

 
# Give the location of the file
loc = ("GD_L2.xlsx")
 
# To open Workbook
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(1)

sheet2 = np.array(sheet)


#Converting the data to a data frame
df = pd.read_excel("GD_L2.xlsx")


W = np.zeros((1,3))
b = 0
X = np.array(df)

Y = np.round((np.zeros((1,300))+ np.asarray(X[0:300,3])).T)
X = X[:,0:3].T

alpha = 0.0001

iter_num = 300000
W_doc = np.zeros((iter_num,3))

for iter in range(iter_num):
    
    Ykova = np.dot(W,X).T + b
    dW = (-2 * np.dot((Y - Ykova).T , X.T)) / 300
    db = (-2 * np.sum(Y - Ykova)) / 300
    #print(dW)
    W = W - alpha * dW 
    b = b - alpha * db
    W_doc[iter,:] = W
print(W)

plt.plot(W_doc)
plt.show()

