# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 01:49:51 2021

@author: gyabe
"""

def add(k, l):
    ans = []
    x = 0
    n= k
    m= l
    if len(n) > len(m):
        while x < len(n):
            if x < len(m):
                c = n[x] + m[x]
            else:
                c = n[x]
            if c > 9 and x <= len(n) - 2:
                n[x+1] += 1
                print(n)
                ans.append(c % 10)
            elif c > 9 and x == len(n) - 1:
                ans.append(c % 10)
                ans.append(c // 10)
            else:
                ans.append(c % 10)
            x += 1
    else:
        while x < len(m):
            if x < len(n):
                c = n[x] + m[x]
            else:
                c = m[x]
            if c > 9 and x <= len(m) - 2:
                m[x + 1] += 1
                ans.append(c % 10)
            elif c > 9 and x == len(m) - 1:
                ans.append(c % 10)
                ans.append(c // 10)
            else:
                ans.append(c % 10)
            x += 1
    return ans
            
        