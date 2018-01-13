#This program is to find next greater number from a given number
"""
Input: n='231'
Output: 'next greater value=321'
"""
#NOTE: Using permutations will not give you efficient time complexity if number will be too large
from itertools import permutations
import time
n='231'
#Start and end will give you actual time the program need to execute
start=time.time()

temp=[]
new=[]
#Find permutations for finding combinations of number
for i in permutations(n):
    per=''.join(i)
    temp.append(per)
    temp.sort()
print temp
if n==max(temp):
    print "not"
else:
    for i in temp:
        if n<i:
            new.append(i)
    print min(new)
end=time.time()
total=end-start
print total
def find(number,n):
    for i in range(n-1,0,-1):
        if number[i]>number[i-1]:
            break
    if i==0:
        print "not possible"
    
