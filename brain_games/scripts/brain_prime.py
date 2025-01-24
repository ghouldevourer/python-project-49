import random

from brain_games.cli import chk_answer, is_prime, welcome_user


def main():
    a = random.randint(1, 999)
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    question = f'Question: {a}'
    correct_answer = 'yes' if is_prime(a) else 'no'
    chk_answer(question, correct_answer, name)
