# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 07:09:45 2016

@author: hoilus
"""
from itertools import chain, combinations

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

for result in powerset([1, 2, 3]):
    print(result)
    
results = list(powerset([1, 2, 3]))
print(results)
