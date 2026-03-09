def comparison(num,pivot):
   
    positivesum=0
    negativesum=0
    
    for n in num :
        if n > 0 :
            positivesum +=n
            
            #print(greater)
        elif n < 0 :
            negativesum +=n
            
    #print(positivesum)
    #print(negativesum)
    if positivesum ==  pivot or negativesum == pivot :
        print("tie")  
    elif negativesum < pivot :
        print("smaller")
    elif positivesum > pivot :
        print("Greater")

num=[0,0,0,0,2]
pivot=2
print(comparison(num,pivot))