N = int(input("Enter N: "))
count = 0
num = N
while num != 0:
    count += 1
    num //= 10
print(count)
