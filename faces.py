print("Enter text + an emoticon")


def convert(words):
    words = words.replace(":)", "🙂")
    words = words.replace(":(", "🙁")
    return words
