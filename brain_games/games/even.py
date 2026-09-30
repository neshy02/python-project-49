import random

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

def generate() -> None:
    question = random.randint(0, 100)
    correct = 'yes' if question % 2 == 0 else 'no'
    return str(question), correct