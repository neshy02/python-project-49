import math
import random

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate():
    first, second = random.randint(0, 50), random.randint(0, 50)
    question = f'{first} {second}'
    correct = math.gcd(first, second)

    return question, str(correct)
    