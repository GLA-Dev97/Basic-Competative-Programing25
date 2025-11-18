# given an array of a non negative number A and a non negative number B we need to find a number of subarray sum is less than A

# arr = [1, 2, 3]
# A = 5

# count = 0

# for i in range(len(arr)):
#     s = 0
#     for j in range(i, len(arr)):
#         s = s + arr[j]
#         if s < A:
#             count = count + 1
#         else:
#             break

# print(count)

# given an array of integer A a sub array of an array is said to be good it fulfilled any one of the creiteria
# condition!: length of array is even and of sum of all the element of subarray must be lesst than B
#codition2: length of array is odd and of sum of all the element of subarray must be greater than B
# your task is to find the  count 

# A = [1, 11, 2, 3, 15]
# B = 10

# count = 0
# n = len(A)

# for i in range(n):
#     s = 0
#     for j in range(i, n):
#         s += A[j]
#         length = j - i + 1

#         if (length % 2 == 0 and s < B) or (length % 2 == 1 and s > B):
#             count += 1


# print(count)

# you have given an integer arraY C of size of A now you need to find A subarray so that the sum of continous element is maximum the sum not exceed B

# A = 5
# B = 12
# C = [2, 1, 3, 4, 5]

# max_sum = 0
# n = len(C)

# for i in range(n):
#     sum = 0
#     for j in range(i, n):
#         sum += C[j]
#         if sum <= B and sum > max_sum:
#             max_sum = sum

# print(max_sum)

# given an array a of length N your task is to find maximum possible sum of any non empty non contigous sub array in among all the possible subrrays A determine the one that yeild the highr=est sum and return the sum


# 2. Print All the Values of Subarrays
# N = int(input("Enter size of array: "))
# arr = list(map(int, input("Enter elements: ").split()))

# for i in range(N):
#     for j in range(i, N):
#         print(*arr[i:j+1])


# N  = int(input())
# arr = list(map(int, input().split()))

# current_sum = 0
# max_sum = 0


# for i in range(1,N):
#     # current_sum+= arr[i]
#     # print(current_sum)
#     current_sum = max(arr[i],current_sum+arr[i])
#     max_sum = max(max_sum,current_sum)
# print(max_sum)

# n = int(input())
# arr = list(map(int, input().split()))

# total_sum = 0
# for i in range(n):
#     contribution = arr[i] * (i+1) * (n-i)
#     total_sum+= contribution
# # print(total_sum)

# W = int(input())
# for _ in range(W):
#     s = input().strip()
#     vowels = 0
#     consonnant = 0
#     for ch in s:
#         if ch.lower() in "aeiou":
#             vowels+=1
#         elif ch.isalpha():
#             consonnant+=1
#     print(vowels,consonnant)


# n = int(input())

# arr = list(map(int, input().split()))

# leaders = []

# max_from_right = arr[-1]  
# leaders.append(max_from_right)

# for i in range(n - 2, -1, -1):
#     if arr[i] > max_from_right:
#         leaders.append(arr[i])
#         max_from_right = arr[i]

# leaders.sort()
# print(*leaders)
