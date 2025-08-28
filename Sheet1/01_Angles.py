a = int(input("Enter the Angle a:"))
b = int(input("Enter the Angle b:"))
c = int(input("Enter the Angle c:"))

if(a+b+c ==180):
    if(a == 90 or b == 90 or c ==90):
        print("Right tringle ")
    elif(a > 90 or b >90 or c > 90):
        print("Obtuse Tringle")
    else:
        print("Acute Triangle")
else:
    print("Not a valid Triangle")
