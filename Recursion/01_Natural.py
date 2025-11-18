# # Sum of natural numbers by loop
# n=5

# for i in range(1, n + 1):
    
#     total = 0
#     for j in range(1, i + 1):
#         total += j  
#     print(total)


def Sum(N):
    if N == 1:
        return 1
    else:
        return Sum(N - 1)+N

N = int(input())
print(Sum(N))

# N = int(input())
    
# calcualte factorial of a number using recursion
# def factorial(N):
#     if N == 0:
#         return 1
#     else:
#         return N * factorial(N - 1)
    
# N= int(input())
# print(factorial(N))


# using recursion print numbers from 1 to N


# # N to 1
# def print1toN(N):
#     if N == 0:
#         return 0
#     else:
#         print1toN(N - 1)
#     # print(N)
# N = int(input())
# print(print1toN(N))

#  using a recusrsin find the nth fibonacci number 

# def fibonacci(N):
#     if N <= 1:
#         return N
#     else:
#         return fibonacci(N - 1) + fibonacci(N - 2)
# print(fibonacci(N))
# N = int(input())
