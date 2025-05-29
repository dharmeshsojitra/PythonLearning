magic_number =9
attempts = 0
number_guessed = False
while attempts < 3:
    guess = input('guess a number: ')
    guess = int(guess)
    attempts += 1
    if guess == magic_number:
        print('you got it')
        number_guessed = True
        break

if not number_guessed:
    print('you did not guess it')