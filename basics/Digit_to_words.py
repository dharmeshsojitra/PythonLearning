word_map = {
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",
    "0":"zero"
}

in_digit = input("enter a number: ")
word = ""
for digit in in_digit:
    if digit in word_map:
        word += word_map[digit] + " "

print(f'{word} ')