

text = input("Enter text: ")

words = text.split()
vowels = "aeiou"

word_count = len(words)
vowel_count = 0
consonant_count = 0

for ch in text.lower():
    if ch in vowels:
        vowel_count += 1
    elif ch.isalpha():
        consonant_count += 1


simple_text = text.lower().replace(" ", "")
is_palindrome = simple_text == simple_text[::-1]


longest = ""
for w in words:
    if len(w) > len(longest):
        longest = w


frequency = {}
for w in words:
    if w in frequency:
        frequency[w] += 1
    else:
        frequency[w] = 1

print("Word count:", word_count)
print("Vowel count:", vowel_count)
print("Consonant count:", consonant_count)
print("Is Palindrome:", is_palindrome)
print("Longest word:", longest)
print("Word frequency:", frequency)
print("Reversed text:", text[::-1])