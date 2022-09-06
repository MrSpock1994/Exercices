# An Armstrong number is a number that is the sum of its own digits 
# each raised to the power of the number of digits.


def check_armstrong_number(a):
    a_string = str(a)
    number_digits = len(a_string)
    sum_digits = 0
    for c in range(0, number_digits):
        sum_digits += (int(a_string[c]) ** number_digits)
    if a == sum_digits:
        return f"{a} is an Armstrong number!"
    else:
        return f"{a} is not an Armstrong number!"


print(check_armstrong_number(154))