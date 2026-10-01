import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number < 2:
        return False
    
    # Идем от 2 до квадратного корня из number (включительно)
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False  # Нашли делитель — число не простое
            
    return True


def generate():
    question = random.randint(0, 30)
    if is_prime(question):
        correct = 'yes'
    else:
        correct = 'no'

    return str(question), correct
