with open("notes.txt", "r") as file:
    text = file.read()

word_count = len(text.split())
print("Total words:", word_count)
