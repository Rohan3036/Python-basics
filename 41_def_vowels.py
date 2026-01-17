def count_vowels(text):
    vowels = "aeiou"
    count = 0

    for ch in text.lower():
        if ch in vowels:
            count += 1

    return count


word = "Artificial Intelligence"
print("Vowel count:", count_vowels(word))
