def vowel(s):
    return "".join(char for char in s if char.lower() not in "aeiou")

input_string = "Hello, World!"
print("String after removing vowels:", vowel(input_string))
