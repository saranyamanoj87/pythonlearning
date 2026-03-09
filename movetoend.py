def movtoend(eles):
    for ele in eles:
        if ele==0:
            #print(ele)
            eles.remove(ele)
            eles.append(0)
            #print(eles)  
    return eles  

eles=[0,1,0,3,12]
print(movtoend(eles))