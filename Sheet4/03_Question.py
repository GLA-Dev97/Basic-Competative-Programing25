t = int(input("Enter number of strings: "))
for _ in range(t):
    s = input()
    if s == s[::-1]:
        print(1)
    else:
        print(0)
