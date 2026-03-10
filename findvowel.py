def findvowel(s):
    vowels = 'aeiouAEIOU'
    output = []
    for char in s:
        if char in vowels:
            output.append(char)
    return output

s = "leetcodE"
print(findvowel(s))