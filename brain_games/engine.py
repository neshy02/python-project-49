import prompt


def main(game):
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.DESCRIPTION)

    ROUNDS = 3 

    for _ in range(ROUNDS):
        question, correct = game.generate()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if answer == correct:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(.")
            print(f"Correct answer was '{correct}'") 
            print(f"Let's try again, {name}!")
            return 
  
    print(f'Congratulations, {name}!')






