# Reverse a string
# For example: input: "cool" output: "looc"


def reverse_string(x):
    new_string = []
    for c in range(len(x) - 1, -1, -1):
        new_string.append(x[c])
    return ''.join(new_string)


print(reverse_string("cool"))