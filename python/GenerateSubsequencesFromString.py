"""
This program generates all possible subsequence from a given string
Example: 'abc' -> 'a', 'b', 'c', 'ab', 'ac', 'bc', 'abc'
Complexity: 2 power n
"""

import pprint

def getSubsequences(input_string):
    if not isinstance(input_string, basestring):
       return [[]]
    
    slist = list(input_string)

    if len(slist) == 0:
        return [[]]
    
    clist = [[slist[0]]]
    for i in range(1, len(slist)):
        n = len(clist)
        for j in range(n):
            l = list(clist[j])
            l.append(slist[i])
            clist.append(l)
        clist.append(list(slist[i]))    
    return clist

pprint.pprint(getSubsequences(None))
pprint.pprint(getSubsequences(10))
pprint.pprint(getSubsequences('')) 
pprint.pprint(getSubsequences('abcd'))
        

""" Output
[[]]
[[]]
[[]]
[['a'],
 ['a', 'b'],
 ['b'],
 ['a', 'c'],
 ['a', 'b', 'c'],
 ['b', 'c'],
 ['c'],
 ['a', 'd'],
 ['a', 'b', 'd'],
 ['b', 'd'],
 ['a', 'c', 'd'],
 ['a', 'b', 'c', 'd'],
 ['b', 'c', 'd'],
 ['c', 'd'],
 ['d']]
"""
