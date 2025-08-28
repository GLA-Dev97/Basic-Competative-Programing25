num = int(input("Enter a number: "))
if num % 7 == 0 and num % 10 == 5:
    print("Divisible by 7 and last digit is 5")
else:
    print("It is not divisible by 7 and not last digit is 5")