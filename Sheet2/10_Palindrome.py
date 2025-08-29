N = int(input("Enter A: "))
original = str(N)
reversed_N = original[::-1]
if original == reversed_N:
    print("Yes,It is palindrome")
else:
    print("It is not Palindrome")
