from collections import Counter
#string
def first_non_repeat(s):
    count=Counter(s)
    for char in s:
        if count[char]==1:
            return char
    return None      

s="l"
print(first_non_repeat(s))

 
 
 
 
 
 
 
 
 #list   
def counting_ele(s,x):
    count=Counter(s)
    return(count[x])


s=[1,2,2,3,3,3]
x=1
print(counting_ele(s,x))
