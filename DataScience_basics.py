# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 17:24:42 2019

@author: srinidhi
"""

import pandas as pd
import numpy as np

#to convert a list to a array using numpy 

list_1 = [1,2,3,4]
list_1 = np.array(list_1)
print(list_1)
print(type(list_1))

#2d arrays
r = np.array([[1,2,3,4],[1,2,3,4]])
print(r)
print(r[1][2])

my_list = [number for number in range(0,100) if number%2==0]
print(my_list)

n =np.arange(0,30)
print(n)
#to print uni_diagonal elements
print(np.eye(3))
#to print diagonal elements
y = [1,2,3]
p = np.diag(y)
print(p)

print(np.vstack([p,p*2]))
#The Different array operations
e = np.array([-4,-3,-2,-1,0,1,2,3,4])
print(e)
print(e.sum())
print(e.mean())
print(e.argmax())
print(e.argmin())

s=np.arange(8)**2

my_list = []
for number in range(0,1000):
    if number%2==0:
        my_list.append(number)
print(my_list)
#repeat the elements of the list
np.repeat([1,2,3],3)
#use of classes 
class Person():
    department = 'Infornation Science'
    def set_name(self,new_name):
       self.name = new_name
    def set_location(self,new_loc):
        self.loc=new_loc
person =Person()  

person.set_name('Srinidhi M')
person.set_location('Mysuru')
print('{} is from {} studying in this {} department'.format(person.name,person.loc,person.department))
 
#pandas useage

#use of series
animals = ['Tiger','Lion','Bear']       
animals = pd.Series(animals)
print(animals)

#direct use of series
numbers = pd.Series([1,2,3])
print(numbers)

sports = {'Cricket':'England',
          'FootBall':'Spain',
          'BaseBall':'USA'
        }
sports = pd.Series(sports)
print(sports)

athletics_loving_countries = pd.Series(['Jamica','China','Japan'],index=['athletics','athletics','athletics'])
allsports = sports.append(athletics_loving_countries)
print(allsports)
print(athletics_loving_countries)


#another beautiful example for implementation of series
purchase_1 = pd.Series({'name':'srinidhi',
                       'Item_purchased':'vicky_ball',
                       'cost':95})
purchase_2 = pd.Series({'name':'Manjunath',
                       'Item_purchased':'Rice',
                       'cost':68})
purchase_3 = pd.Series({'name':'Roopa',
                       'Item_purchased':'Cheese_blocks',
                       'cost':26})
purchase_4 = pd.Series({'name':'vani',
                       'Item_purchased':'Pizza',
                       'cost':500})
df=pd.DataFrame([purchase_1,purchase_2,purchase_3,purchase_4],index=['store1','store2','store3','store4'])
df.head()

df_copy = df.copy()
print(df_copy)
#drop a horizonzal row
df_copy = df_copy.drop('store4')
print(df_copy)
#to drop a vertical column make use of del
#a discount of 10% given we get the cost as:

df_copy['cost']*=0.9
print(df_copy)

#read csv files
df = pd.read_csv('project.csv')
print(df.head)

#to drop vertical axis

del df['Timestamp']
print(df)
#making a copy of the dataframe
new_df = df.copy()
print(new_df.head())
#to write to csv
new_df.to_csv('Modified.csv')

#to read modified csv
df = pd.read_csv('Modified.csv')
print(df.head())







