num1 =int(input("enter the num1:"))
num2 = int(input("enter the num2:"))
num3 = int(input("enter the num3:"))
if((num1<num2) and (num2<num3)):
    print("num1 is smallest:", num1)

elif((num2<num3) and (num3<num1)):
    print("num2 is smallest", num2)
else:
    print("num3 is smallest", num3)
