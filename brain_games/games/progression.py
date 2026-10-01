import random

DESCRIPTION = 'What number is missing in the progression?'


def generate():
    length = 10
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    stop = start + (step * length)
    numbers = [str(x) for x in range(start, stop, step)]
    correct_index = random.randint(0, (length - 1))
    correct = numbers[correct_index]
    numbers[correct_index] = '..'
    question = ' '.join(numbers)

    return question, str(correct)

    
