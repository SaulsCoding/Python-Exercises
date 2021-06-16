import random

num = random.randint(1, 20)
tries = 1

print('I am thinking of a number between 1 and 20. ')
print('Take a guess.')

guess = int(input(''))

while guess != num :
    tries += 1
    if guess > num :
        print('Your guess is too high. ')
        print('Take a guess.')
        guess = int(input(''))
    elif guess < num :
        print('Your guess is too low. ')
        print('Take a guess.')
        guess = int(input(''))
    if guess == num :
        print('Good job! You guessed my number in ' + str(tries) + ' guesses!')
        
