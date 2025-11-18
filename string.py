'''n=65
for i in range(5):
    for j in range(i+1):
        print(chr(n),end=" ")
    n+=1
    print()'''

# reverse the ordern of the words
'''s="python is a programming language"
rev=s.split()
print(rev)
rev.reverse()
print(rev)
s=' '.join(rev)
print(s)'''

# reverse each word individually in   string
'''s="python is a programming language"
rev=s.split()
print(rev)
for i in range(len(rev)):
    rev[i]=rev[i][::-1]
print(rev)
s=' '.join(rev)
print(s)'''

# you have a given string and you have to find all the amazing substring of string an amazing substring that start with a vovel
# output = 6

'''s = "ABEC"
count = 0
vowels = "AEIOUaeiou"
for i in range(len(s)):
    if s[i] in vowels:
        count += (len(s) - i)
print(count)'''

# find the number of occurence of strring consisting of lowercase alphabet

'''s = "bob"
count = 0
l = 'abcdefghijklmnopqrstuvwxyz'

for char in s :
    if char in l:
        count += 1

print(count)'''


'''A = "aeiOUz"

result = A + A

temp = ""
for c in result:
    if c not in "AEIOU":
        temp += c
result = temp
final = ""
for c in result:
    if c in 'aeiou':
        final += '#'
    else:
        final += c
print(final)
'''


# give an array find the sum of all array sum

'''# guve an integer array num . find the sub array with the largest sum

def max_subarray_sum(nums):
    if not nums:
        return 0
    max_current = max_global = nums[0]
    for num in nums[1:]:
        max_current = max(num, max_current + num)
        if max_current > max_global:
            max_global = max_current
    return max_global

# Example usage
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(nums))  # Output: 6
'''
