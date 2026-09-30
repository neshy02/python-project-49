import random

DESCRIPTION = 'What is the result of the expression?'


def generate():
    first, second = random.randint(0, 30), random.randint(0, 10)
    operators = ['+', '-', '*']
    operator = random.choice(operators)
    question = f'{first} {operator} {second}'
    match operator:
        case '+':
            correct = first + second
        case '-':
            correct = first - second
        case '*':
            correct = first * second
    return question, str(correct)