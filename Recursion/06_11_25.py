# using recusrsion print 1 to n numbers

# def print_numbers(N):
#     if N == 0:
#         return 0
#     else:
#         print_numbers(N - 1)
#     print(N)
# N = int(input())
# print(print_numbers(N))

# using recursion print n to 1 numbers

# def printNto1(N):
#     if N == 0:
#         return 0
#     else:
#         print(N)
#         printNto1(N - 1)
# N = int(input())
# print(printNto1(N))


# using a recusrsin find the nth fibonacci number 

# def fibonacci(N):
#     if N <= 1:
#         return N
#     else:
#         return fibonacci(N - 1) + fibonacci(N - 2)
# N = int(input())
# print(fibonacci(N))

# print series of fibonacci numbers upto n

# def fibonacci(N):
#     if N <= 1:
#         return N
#     else:
#         return fibonacci(N - 1) + fibonacci(N - 2)
# N = int(input())
# print(fibonacci(N))
# for i in range(N):
#     print(fibonacci(i))

#  find the sum of digit using recursion

# def sum_digit(n):
#     if n == 0:
#         return 0
#     else:
#         return n % 10 + sum_digit(n //10)
    
#     n = int(input())
#     print(sum_digit(n))

#  reverse a string using recursion
def revrse_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + revrse_string(s[:-1])
s = input()
print(revrse_string(s))