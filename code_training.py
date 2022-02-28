"""
    Input : ['h', 'y', 'n', 'p', 't', 'o'],[3 ,1, 5, 0, 2, 4]
    Output : python
"""

from inspect import ArgSpec
from operator import index
from pprint import pprint
from typing import List
from unittest import result

def order_change_by_indexes_v1(chars: List[str], indexes: List[int]) -> str:
    tmp = [None] * len(chars)
    for i, index in enumerate(indexes):
        tmp[index] = chars[i]
    return ''.join(tmp)    

def order_change_by_indexes_v2(chars: List[str], indexes: List[int]) -> str:
    i, len_indexes = 0, len(indexes) - 1
    while i < len_indexes:
        while i != indexes[i]:
            index = indexes[i]
            chars[index], chars[i] = chars[i], chars[index]
            indexes[index], indexes[i] =  indexes[i], indexes[index]
        i +=  1
    return ''.join(chars)    

if __name__ == '__main__':
    w = ['h', 'y', 'n', 'p', 't', 'o']
    i = [3 ,1, 5, 0, 2, 4]
    print(order_change_by_indexes_v1(w,i))
    

data = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]]
result=[[row[i] for row in data] for i in range(4)]
result

moji='dive\ninto\ncode\r'
print(len(moji))

