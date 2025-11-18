# a= int(input())
# b= int(input())
# if(a*b)<=1000:
#     print(a*b)
# else:
#     print(a+b)
#-----------------------------------------------------

# Exercise 2: Print the Sum of a Current Number and a Previous number

"""
a = int(input())

for i in range(0,a):
    print("Current Number is:",i,"previous Number is:",i-1,"Sum:",i+(i-1))
"""

#Exercise 3: Print characters present at an even index number

"""str1 = input()
for i in range(0,len(str1)):
    if i%2==0:
        print(str1[i])"""

# Remove first n characters from a string
"""
str1 = input()
n = int(input())
print(str1[n:])"""

#5. Check if the first and last number of a list are same 

"""n = int(input())
list = []
for i in range(n):
    a = int(input())
    list.append(a)
if list[0]==list[-1]:
    print("True")
else:
    print("False")"""

#Display number divisible by 5

"""n = int(input())
list = []

for i in range(n):
    a = int(input())
    list.append(a)
if a%5==0:
    print(a)
else:
    pass"""

# Find the number of occurrences of a substring in a string:
"""str1 = input()
sub_str = input()
count = str1.count(sub_str)
print(count)"""

# check palindrome Number 
"""
n = int(input())
temp = n
rev = 0
while(n>0):
    digit = n%10
    rev = rev*10 + digit
    n = n//10"""

# Merge two lists using even odd condition

"""list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
list3 = []
for i in list1:
    if i%2!=0:
        list3.append(i)
for j in list2:
    if j%2==0:
        list3.append(j)
print(list3)"""

# Get Each digit from a number in the reverse order with singlw space
'''
n = int(input())
rev = 0
while(n>0):
    digit = n%10
    rev = rev*10 + digit
    n = n//10
print(digit, end="  ")'''

'''number = int(input())
print("Given number", number)
while number > 0:
    # get the last digit
    digit = number % 10
    # remove the last digit and repeat the loop
    number = number // 10
    print(digit, end=" ")'''

# The Scholarship Eligibility Checker

"""n = int(input())
count = 0
for i in range(n):
    marks1, marks2 = map(int, input().split())
    if marks1 >= 75 and marks2 >= 80:
        count += 1
print(count)"""

# the perfect pair finder
'''
n = int(input())
arr = list(map(int, input().split()))
k = int(input())
count = 0
for i in range(n):
    for j in range(i+1, n):
        if arr[i] + arr[j] == k:
            count += 1
print(count)'''

# the Attendace Tracker

""" Sample Input:
10
1 0 0 1 0 0 0 1 1 0
sample Output:
3
"""

''' = int(input())
a = list(map(int, input().split()))
ms = 0
cs = 0
for i in range(n):
   if a[i] == 0:
    cs += 1
   else:
        ms = max(ms, cs)
       cs = 0
print(max(ms, cs))'''

'''n = int(input())
a = list(map(int, input().split()))

c = 0
for i in range(1, n):
    if a[i] > a[i-1]:
        c += 1
print(c)'''
'''
n = int(input())
a = list(map(int, input().split()))

c = 0
b = sum(a)
avg = b/len(a)
for i in a:
    if i>=avg:
        c+=1
print(c)
'''