A = int(input("Enter the first number: "))
B = int(input("Enter the Second Number: "))
C = int(input("Enter the third Number: "))
if(A>B)and(B>C):
    print("A is Greater")
elif(B>C)and(C>A):
    print("B is Greater")
else:
    print("C is Greater")