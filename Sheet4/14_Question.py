A = input("Enter string: ")
B = int(input("Enter ASCII code: "))
ch = chr(B)
if ch in A:
    print(A.index(ch))
else:
    print(-1)
