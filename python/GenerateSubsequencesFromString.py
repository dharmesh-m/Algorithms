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
    
    clist = [[[slist[0]]]]
    for i in range(1, len(slist)):
        nlist = list(clist[i-1])
        n = len(nlist)
        for j in range(n):
            l = list(nlist[j])
            l.append(slist[i])
            nlist.append(l)
        nlist.append(list(slist[i]))    
        clist.append(nlist)
    return clist[len(slist) - 1]

pprint.pprint(getSubsequences(None))
pprint.pprint(getSubsequences(10))
pprint.pprint(getSubsequences('')) 
pprint.pprint(getSubsequences('abcd'))
        

