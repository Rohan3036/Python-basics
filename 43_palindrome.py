def is_palindrome(text):
    def reverse_text(text):
        reversed_text = ""

        for ch in text:
            reversed_text = ch + reversed_text

        return reversed_text
    text = text.lower()
    return text == reverse_text(text)


word = "Madam"
print("Palindrome:", is_palindrome(word))
