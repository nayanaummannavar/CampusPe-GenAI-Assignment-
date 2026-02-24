

text = input("Enter a word or number: ")

# Convert to lowercase to ignore case
text = text.lower()

# Reverse the text
reverse_text = text[::-1]

if text == reverse_text:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")