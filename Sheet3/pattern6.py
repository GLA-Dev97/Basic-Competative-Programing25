rows = 5

for i in range(rows, 0, -1):      
    for j in range(i+1):         
        if j == 0 or j == i:     
            print("*", end=" ")
        else:                     
            print("_", end=" ")
    print()