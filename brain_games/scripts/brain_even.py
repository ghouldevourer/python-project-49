import random

from brain_games.cli import chk_answer, welcome_user


def main():
    a = random.randint(1, 999)
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    question = f'Question: {a}'
    correct_answer = 'yes' if a % 2 == 0 else 'no'
    chk_answer(question, correct_answer, name)