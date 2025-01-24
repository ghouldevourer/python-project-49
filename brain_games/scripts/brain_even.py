import random

from brain_games.cli import check_answer, welcome_user


def main():
    a = random.randint(1, 999)
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    question = f'Question: {a}'
    correct_answer = 'yes' if a % 2 == 0 else 'no'
    check_answer(question, correct_answer, name)