# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 03:25:49 2021

@author: gyabe
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
l1 = ListNode()
l1.val = 2
b= ListNode()
b.val = 4
b.next = l1
a = ListNode()
a.val = 3
a.next = b


'''class Solution:
    def addTwoNumbers(self, l1, l2):
        ans = []
        x = 0
        n= l1
        m= l2
        while l2:
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

'''