A = input("Enter string A: ")
B = input("Enter substring B: ")
pos = A.find(B)
if pos != -1:
    print(pos)
else:
    print(-1)
