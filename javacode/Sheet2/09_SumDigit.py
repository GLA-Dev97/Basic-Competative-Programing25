N = int(input("Enter N: "))
total = 0
num = N
while num > 0:
    digit = num % 10
    total += digit
    num //= 10
print(total)
