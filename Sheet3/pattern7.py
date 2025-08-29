n = int (input (" enter a no. "))
for i in range (1, n+1):
    for j in range (n-i):
        print ( "_",end="  ")
    for j in range (i):
        print(" *" , end=" ")

    
    print ()