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
print(data_BM)


# drop the null values
data_BM = data_BM.dropna(how="any")
print(data_BM)


# sum price based on item type
item_group = data_BM.groupby('Item_Type')[[ 'Item_Weight', 'Item_Visibility','Item_MRP','Item_Outlet_Sales']].sum()[:6]
print(item_group )

def line_plot(x_axis, my_list, xticks, label, title):
      
    '''
    Data:This function defines multiple line plot, below are the attributes;
    Args:
         x_axis: this uses preferred columns to state the index
         title:  shows the title of the plot
         labels: these are the labels of each line plot 
     Returns:
        None
    
    '''
    
    plt.figure(figsize=(12,8))
    for i in range(len(my_list)):
        plt.plot(x_axis,my_list[i],label=label[i])
    plt.legend()
    plt.xticks(x_axis,xticks)
    plt.title(title,fontsize=15)
    plt.show()
    
# parameters for plotting multiple line plot
x_axis = item_group.index
my_list = [item_group['Item_Weight'], item_group['Item_Visibility'], item_group['Item_MRP'], item_group['Item_Outlet_Sales']]
xticks = ['Baking Goods', 'Breads', 'Breakfast', 'Canned', 'Dairy', 'Frozen Foods']
label = ['Item_Weight', 'Item_Visibility', 'Item_MRP','Item_Outlet_Sales']
title = 'A line plot of Item_Weight, Item_Visibility, Item_MRP and Item_Outlet_Sales'

line_plot(x_axis,my_list,xticks,label,title)   


# sales by outlet size
sales_by_outlet_size = data_BM.groupby('Outlet_Size').Item_Outlet_Sales.sum()
print(sales_by_outlet_size)

def bar_chart(x_axis,my_list,title):
      
    '''
    Data:This function defines box plot, below are the attributes;
    Args:
        x_axis: this uses preferred columns to state the index
        title:  shows the title of the plot
     Returns:
        None
    
    '''
    plt.figure(figsize=(12,8))
    plt.bar(x_axis, list, color = ['red', 'orange', 'magenta'])
   
    # sort by sales
    sales_by_outlet_size.sort_values(inplace=True)

    # set axis labels
    plt.xlabel('Outlet Size')
    plt.ylabel('Sales')

    # set title
    plt.title('Total sales for each outlet type')

    plt.show()
    return

# parameters for plotting bar plot
x_axis = sales_by_outlet_size.index.tolist()
list = sales_by_outlet_size.values.tolist() 
title = 'Mean sales for each outlet type'


bar_chart(x_axis, my_list, title)


    
    
def box_plot(x_axis,label,title):
    
    '''
    Data: This function defines box plot, below are the attributes;
    Args:
     
        x_axis: this uses preferred columns to state the index
        title:  shows the title of the plot
        labels: these are the labels of each box plot 
    Returns:
        None
    
    '''
    # etracts the data
    data = data_BM[['Item_Weight', 'Item_Visibility', 'Item_MRP', 'Item_Outlet_Sales']]
    plt.figure(figsize=(18,7))
    
    # create outlier point shape
    red_diamond = dict(markerfacecolor='r', marker='D')
    
    
    # generate subplots
    fig, ax = plt.subplots()
    
    plt.boxplot(data.values, labels=['Item Weight', 'Item_Visibility', 'Item MRP', 'Item_Outlet_Sales'], flierprops=red_diamond);
    return   
    
    
# parameters for plotting box plot
x_axis = [sales_by_outlet_size['Item_Weight'], sales_by_outlet_size['Item_Visibility'],sales_by_outlet_size['Item_MRP'],  sales_by_outlet_size['Item_Outlet_Sales'],]
label =  sales_by_outlet_size.index
title = ['box plot for item weight, visibility, MRP and outlet sales']
# creates the boxplot
box_plot(x_axis,label,title)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    