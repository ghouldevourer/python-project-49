import random

import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    sname = prompt.string('May I have your name? ')
    print('Hello,', sname)
    return sname


def get_question_and_answer(type):
    a = random.randint(1, 999)
    c = random.randint(1, 999)
    if type == 'even':
        print('Answer "yes" if the number is even, otherwise answer "no"')
        question = f'Question: {a}'
        correct_answer = 'yes' if a % 2 == 0 else 'no'
    elif type == 'calc':
        print('What is the result of the expression?')
        b = random.choice(['*', '+', '-'])
        exp = f'{a} {b} {c}'
        question = f'Question: {exp}'
        correct_answer = str(eval(exp))
    elif type == 'gcd':
        print('Find the greatest common divisor of given numbers.')
        question = f'Question: {a} {c}'
        while a != 0 and c != 0:
            if abs(a) > abs(c):
                a = a % c
            else:
                c = c % a
            exp = a + c
        correct_answer = str(exp)
    return question, correct_answer


def chk_answer(type):
    sname = welcome_user()
    right_answers = 0
    for _ in range(3):
        question, correct_answer = get_question_and_answer(type)
        print(question)
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            right_answers += 1
        else:
            print(f'\'{user_answer}\' is wrong answer ;(. '
                  f'Correct answer was \'{correct_answer}\'.')
            print(f'Let\'s try again, {sname}!')
            break
    if right_answers == 3:
        print(f'Congratulations, {sname}!')
