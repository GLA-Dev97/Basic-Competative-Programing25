A = input("Enter string: ")

A = A + A

new_str = ""
for ch in A:
    if not ch.isupper():
        new_str += ch

result = ""
for ch in new_str:
    if ch in "aeiou":
        result += '#'
    else:
        result += ch

print(result)
