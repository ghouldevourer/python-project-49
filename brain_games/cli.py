import random

import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    sname = prompt.string('May I have your name? ')
    print('Hello,', sname)
    return sname


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True


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
    elif type == 'progression':
        print('What number is missing in the progression?')
        progression = []
        start_num = random.randint(1, 50)
        step_num = random.randint(1, 9)
        progression.append(start_num)
        next_num = start_num + step_num
        progression_len = range(5, 15)
        for _ in progression_len:
            progression.append(next_num)
            next_num += step_num
        hidden_index = random.randint(0, (len(progression) - 1))
        correct_answer = str(progression[hidden_index])
        progression[hidden_index] = '..'
        question_format = ' '.join(map(str, progression))
        question = f'Question: {question_format}'
    elif type == 'prime':
        print('Answer "yes" if given number is prime. Otherwise answer "no".')
        question = f'Question: {a}'
        correct_answer = 'yes' if is_prime(a) else 'no'
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
