# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

file_name= r'C:\Users\Davidg\Desktop\names.xlsx'
advocates = []
tempAdvocates = []
names = ()
n = 0


import pandas as pd
df = pd.read_excel(io=file_name, sheet_name = 0)


for name in df.itertuples():
    for letter in name:
        n += 1
        if n%2 == 0:
            advocates.append(letter)  

for name in advocates:
    n=0
    for letter in name:
        n += 1
        if ' ' in letter:
            first = name[:n]
            last = name[n:]
            names = (last, first + last)
            tempAdvocates.append(names)
            tempAdvocates.sort()
            
advocates.clear()
n = 0
for name in tempAdvocates:
    for letter in name:
        n += 1
        if n % 2 == 0:
            advocates.append(letter)
 


print(advocates)
# =============================================================================
# sorted(tempAdvocates, key = lambda advocate: advocate(1))
# print(tempAdvocates)
# =============================================================================
    
            

#print(names)
    

