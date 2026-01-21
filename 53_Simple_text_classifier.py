def classify_text(text):
    text = text.lower().strip()

    if "error" in text:
        return "This looks like an error message"
    elif text.endswith("?"):
        return "This is a question"
    elif text.startswith("hi") or text.startswith("hello"):
        return "This is a greeting"
    else:
        return "General statement"


print(classify_text("Hello, how are you?"))
print(classify_text("File not found error"))
print(classify_text("I am learning Python"))
