from random import randint

number = 42  # randint(1, 99)
print('This is an interactive guessing game!')
print('You have to enter a number between 1 and 99 to find out the secret number.')
print("Type 'exit' to end the game.")
print('Good luck!\n')

tries = 0
while True:
    print("What's your guess between 1 and 99?")
    guess = input('>> ')
    if guess == 'exit':
        print('Goodbye!')
        break
    try:
        guess_num = int(guess)
        tries += 1
        if guess_num > number:
            print('Too high!')
        elif guess_num < number:
            print('Too low!')
        else:
            if number == 42:
                print(
                    'The answer to the ultimate question of life, the universe and everything is 42.')
            if tries == 1:
                print("Congratulations! You got it on your first try!")
            else:
                print("Congratulations, you've got it!")
                print('You won in {} attempts!'.format(tries))
            break
    except:
        print("That's not a number.")
