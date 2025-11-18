# Write a program to input T strings (S) from user and print count of vowels and consonants in it.

n = int(input())

vowel = "aeiouAEIOU"


for _ in range(n):
    s = input()
    vowel_count = 0
    for ch in s:
        if ch in vowel:
            vowel_count +=1
        
print(vowel_count)


