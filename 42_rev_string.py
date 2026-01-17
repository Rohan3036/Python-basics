def reverse_text(text):
    reversed_text = ""

    for ch in text:
        reversed_text = ch + reversed_text

    return reversed_text


word = "python"
print("Reversed:", reverse_text(word))
