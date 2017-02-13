# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 06:38:01 2016

@author: hoilus
"""

import random

# Code Sample A
mylist = []
a = random.randint(1, 10)
print("a=", a)
a1 = random.randint(1, 10)
print("a1=", a1)

for i in range(a1):
    random.seed(0)
    b = random.randint(1, 10)
    b1 = random.randint(1, 10)
    print("b=",b)
    print("b1=",b1)
    if b > 3:
        number = random.randint(1, 10)
        print("number",number)
        if number not in mylist:
            mylist.append(number)
print(mylist)
