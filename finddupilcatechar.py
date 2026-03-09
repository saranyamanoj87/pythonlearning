#print duplicates
from collections import Counter
#string
dupilcate=[]
def duplicate_in_str(s):
    count=Counter(s)
    for char in s:
        print(count)
        print(count[char])
        if count[char]>1:
            print(count[char])
            print(dupilcate.append(char))
    return set(dupilcate)
          
        

s="leeeettccode"
print(duplicate_in_str(s))
 