def count_chars(text):
    count = 0
    for _ in text:
        count += 1
    return count

word = "python"
print("Length:", count_chars(word))
