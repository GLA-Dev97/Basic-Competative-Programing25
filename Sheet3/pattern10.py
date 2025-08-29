rows = 5

for i in range(1, rows+1):            
    for j in range(i):
        print("*", end="")
    for k in range(2*(rows-i)):
        print(" ", end="")
    for j in range(i):
        print("*", end="")
    print()