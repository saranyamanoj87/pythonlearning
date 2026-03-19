def duplicates():
    listitems=[(1,2),(3,4),(1,2)]
    seen=[]
    repeat=[]
    for i in listitems:
        if i not in seen:
            seen.append(i)
        else:
            repeat.append(i)
    return repeat

print(duplicates())
