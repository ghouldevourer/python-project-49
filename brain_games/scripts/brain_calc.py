import random

from brain_games.cli import check_answer, welcome_user


def main():
    a = random.randint(1, 999)
    c = random.randint(1, 999)
    name = welcome_user()
    print('What is the result of the expression?')
    b = random.choice(['*', '+', '-'])
    exp = f'{a} {b} {c}'
    question = f'Question: {exp}'
    correct_answer = str(eval(exp))
    check_answer(question, correct_answer, name)