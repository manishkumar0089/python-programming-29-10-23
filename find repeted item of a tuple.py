a=(1,2,3,4,5,2,3)
reg=[]
for i in a:
    if a.count(i)>1 and i not in reg:
        print(i)
        reg.append(i)
    
