# given a string calculate the length of longest palindromic substring


'''x = input().strip()
max = 0

for i in range(len(x)):
    for j in range(i, len(x)):
        substr = x[i:j+1]
        if substr == substr[::-1]:
            if len(substr) > max:
                max = len(substr)
                print(substr)
                print(max)'''

`                      `


# given a n and index i print the ith bit of n

# n = 13
# i = 2
# output : 1

n = int(input())
# i = int(input())
i = 2
bit = (n >> i) & 1
print(bit) 






















# exapple: papad
#output : 3  --- pap and apa