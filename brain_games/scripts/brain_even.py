import random

import prompt


def main() -> None:
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    ROUNDS = 3 
    for _ in range(ROUNDS):
        number = random.randint(0, 100)
        print(f'Question: {number}')

        correct = 'yes' if number % 2 == 0 else 'no'

        answer = prompt.string('Your answer: ')
        if answer == correct:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.c")
            print(f"Let's try again, {name}!")
            return
        
    print(f'Congratulations, {name}!')