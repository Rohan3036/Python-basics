ch = input("Enter a single alphabet: ").lower()

if ch in ['a', 'e', 'i', 'o', 'u']:
    print(ch, "is a vowel")
elif ch.isalpha():
    print(ch, "is a consonant")
else:
    print("Invalid input. Please enter a letter.")
