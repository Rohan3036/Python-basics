def count_words(sentence):
    words = sentence.split()
    return len(words)


text = "Artificial intelligence is very interesting"
print("Word count:", count_words(text))
