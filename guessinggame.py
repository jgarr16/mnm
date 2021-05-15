import random

print('------------------------------')
print('     M&M Guessing Game!')
print('------------------------------')

print("Guess the number of M&Ms and you get lunch on the house.")
print()

mm_count = 7  # random.randint(0,100)
attempt_limit = 5
attempts = 0

while attempts < attempt_limit:
    '''docstring for while loop'''
    guess_text = input("How many M&Ms? ")
    guess = int(guess_text)
    attempts += 1
    if attempts == 1:
        tries = "try"
    else:
        tries = "tries"
    if mm_count == guess:
        print(f"You win! The number was {guess}.")
        break
    elif mm_count < guess:
        print(f"Sorry, {guess} is too HIGH.")
    else:
        print(f"Sorry, {guess} was too LOW.")
print(f'You used {attempts} {tries}.')
