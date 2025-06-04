def ret_word(number):
    word_map = {
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
        "0": "zero"
    }

    word = ""
    for digit in number:
        if digit in word_map:
            word += word_map[digit] + " "

    return word

in_digit = input("enter a number: ")
print(in_digit)