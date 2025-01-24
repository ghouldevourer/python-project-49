import random

from brain_games.cli import chk_answer, welcome_user


def main():
    a = random.randint(1, 999)
    c = random.randint(1, 999)
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    question = f'Question: {a} {c}'
    while a != 0 and c != 0:
        if abs(a) > abs(c):
            a = a % c
        else:
            c = c % a
        exp = a + c
    correct_answer = str(exp)
    chk_answer(question, correct_answer, name)