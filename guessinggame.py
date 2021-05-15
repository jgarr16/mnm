import random

print('------------------------------')
print('     M&M Guessing Game!')
print('------------------------------')

print("Guess the number of M&Ms and you get lunch on the house.")
print()

mm_count = random.randint(0,100)
attempt_limit = 5
attempts = 0

while attempts < attempt_limit:
    '''docstring for while loop'''
    guess_text = input("How many M&Ms? ")
    guess = int(guess_text)
    print(f'Guess #{attempts+1}: {guess_text}')
    attempts += 1
print(f'You used {attempts} tries. Better luck next time.')
