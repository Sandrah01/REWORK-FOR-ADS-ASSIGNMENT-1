# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 20:32:32 2023

@author: udehs
"""

# importing required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# read the dataset
data_BM = pd.read_csv('bigmart_data.csv')
data_BM


# drop the null values
data_BM = data_BM.dropna(how="any")
data_BM 