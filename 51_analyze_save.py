with open("notes.txt", "r") as file:
    text = file.read()

lines = len(text.splitlines())
words = len(text.split())
characters = len(text)

with open("report.txt", "a") as file:
    file.write("Analysis Report\n")
    file.write(f"Lines: {lines}\n")
    file.write(f"Words: {words}\n")
    file.write(f"Characters: {characters}\n")
    file.write("--------------------\n")
