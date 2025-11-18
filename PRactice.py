"""n = int(input())
sum = 0

for i in range(1,n+1):
    sum += i 
print(sum)"""


"""a= int(input())
c=0
while a>0:
    r = a%10
    c = c+1
    a = a//10
print(c)
"""

"""n = int(input())
sum =0
while n>0:
    r = n%10
    sum = sum + r
    n = n//10
print(sum)"""

"""n = int(input())
temp = n
rev = 0
while(n>0):
    digit = n%10
    rev = rev*10 + digit
    n = n//10
if(temp==rev):
    print("Palindrome")
else:
    print("Not a Palindrome")"""

"""n = int(input())
for i in range(1,11):
    print(n,"X",i,"=",n*i)"""

""""n = int(input())
for i in range(n-1):
    for j in range(n):
        print("*",end=" ")
    print()"""

"""n = int(input())
for i in range(n,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()"""

""""n = int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        if j%2==0:
            print("*", end=" ")
        else:
            print(j, end=" ")
    print()"""

"""n = int(input())
for i in range(0,n):
    print("*", end=" ")
    for j in range(n):
        print(" ", end=" ")
    print("*")"""

""""n = int(input())
for i in range(n,0,-1):
    if i==1:
        print("_")
    else:
        for j in range(i):
            if j==0 or j==i-1:
                print("*", end=" ")
            else:
                print("_", end=" ")
        print()"""

""""n = int(input())

for i in range(1,n+1):
    for j in range(n-i):
        print("_", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()"""
"""
n = int(input())
for i in range(n,0,-1):
    for j in range(n-i):
        print("_", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()"""

'''n = int(input())
for i  in range(n,0,-1):
    for j in range(i):
        print("*",end =" ")
    for k in range(2*(n-i)):
        print(" ", end=" ")
    for l in range(i):
        print("*", end=" ")
    print()'''

'''n = int(input())
for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    for k in range(2*(n-i)):
        print(" ", end=" ")
    for l in range(i):
        print("*", end=" ")
    print()'''


'''n = int(input())
for i  in range(n,0,-1):
    for j in range(i):
        print("*",end =" ")
    for k in range(2*(n-i)):
        print(" ", end=" ")
    for l in range(i):
        print("*", end=" ")
    print()

for i in range(1,n+1):
    for j in range(i):
        print("*",end=" ")
    for k in range(2*(n-i)):
        print(" ", end=" ")
    for l in range(i):
        print("*", end=" ")
    print()'''

"""n = int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()"""

'''n = int(input())
for i in range(1,n):
    for j in range(1,n-i+1):
        print(j, end=" ")
    print()'''

'''n = int(input())
c=0
for i in range(1,n+1):
    for j in range(i):
        c+=1
        print(c,end=" ")
    print()'''

"""n = int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*", end=" ")
    print()
for i in range(n-1,0,-1):
    for j in range(1,i+1):
        print("*", end=" ")
    print()"""

'''a =list(map(int, input().split()))
print(a)
b = 0
for i in a:
    b = b + i
print(b)'''

''''a = list(map(int, input().split()))
c =[]
b = int(input())
for i in a:
    c.append(b+i)
print(c) '''

'''a = list(map(int, input().split()))
b = min(a)
c = max(a)
print("maximum value is : ",c)
print("minimum value is : ", b)'''

'''a = list(map(int, input().split()))
b = int(input())
for i in range(len(a)):
    if a[i] ==b:
        print(b, "is present at index", i)
        break'''

'''a = list(map(int, input().split()))
for i in range(len(a)):
    if a[i]<0:
        print(a[i])'''

'''a = list(map(int, input().split()))
even = 0
odd = 0
for i in a:
    if i%2==0:
        even +=i
    else:
        odd +=i
diff = even - odd
print(odd)
print(even)
print(diff)'''

'''a = list(map(int, input().split()))
even = []
odd = []
for i in a:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)
'''

'''a = list(map(int, input().split()))
s = []
for i in a:
    s.append(i**2)
print(s)'''

'''a = list(map(int, input().split()))
b = []
for i in range(len(a)-1,-1,-1):
    b.append(a[i])
print(b)'''

'''list = list(map(int, input().split()))
print(list[:])
print(list[::])
print(list[2:5])
print(list[2:])
print(list[2::])
print(list[:2])
print(list[::2])
print(list[1::2])
print(list[2:10:2])

'''

'''mylist = [1.4, 2, 3, 4, 5]
mylist.reverse()
print(mylist)
'''

"""s= "Hello everyone how are you"
print(s.split())
s = "Hello-everyone-how are you"
print(s.split("-"))
word = 'Suyash:Chaudhary:Noida'
print(word.split(':'))
t = "23456"
print(t.split())
t = "2 3 4 5"
print(t.split())

"""

'''arr = [1, 2, 3]
n = len(arr)
for i in range(n):
    for j in range(i, n):
        subarray = []
        for k in range(i, j+1):
            subarray.append(arr[k])
        print(subarray)'''


'''def ps(A, S, E):
    sum_sub = 0
    for i in range(S, E+1):
        sum_sub += A[i]
    print(sum_sub)

def print_AllS(A):
    N = len(A)
    for i in range(N):
        for j in range(i, N):
            ps(A, i, j)

A = [1, 2, 3]
print_AllS(A)
'''
# given an integer array nums find the sub array with largest sum and return sum

'''def max_subarray_sum(nums):
    max_sum = nums[0]       
    current_sum = nums[0]   

    for i in range(1, len(nums)):
        
        current_sum = max(nums[i], current_sum + nums[i])
        
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Example
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Maximum Subarray Sum:", max_subarray_sum(nums))
'''
'''def max_subarray_sum(nums):
    max_sum = nums[0]       
    current_sum = nums[0]   

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Example
nums = [5,4,-1,7,8]
print("Maximum Subarray Sum:", max_subarray_sum(nums))
'''

