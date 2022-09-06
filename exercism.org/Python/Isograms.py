# Determine if a word or phrase is an isogram.

# An isogram (also known as a "non-pattern word") is a word or phrase without a repeating letter, however spaces and hyphens are allowed to appear multiple times.

# Examples of isograms:

# lumberjacks
# background
# downstream
# six-year-old


def is_isogram(word):
    new_word = word.replace("-", "")
    x = len(new_word)
    b = len(set(new_word))
    if x == b:
        return f"{word} is an isogram!"
    else:
        return f"{word} is not an isogram!"



print(is_isogram("six-year-old"))
print(is_isogram("lumberjacks"))


