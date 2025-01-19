import random

import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    sname = prompt.string('May I have your name? ')
    print('Hello,', sname)
    return sname


def booltostr(answ, exp):
    if answ == exp:
        return 'yes'
    else:
        return 'no'


def chk_answer(type):
    sname = welcome_user()
    operators_list = ['*', '+', '-'] 
    right_answer = 0
    wrong_answer = 0
    for i in range(3):
        if (right_answer < 3) and (wrong_answer == 0):
            match type:
                case 'even':
                    print('Answer "yes" if the number is even,'
                          ' otherwise answer "no".')
                    a = random.randint(1, 999)
                    exp = f'{a}'
                    print(f'Question: {exp}')
                    answ = prompt.string('Your answer: ')
                    answ_case = booltostr(answ, 'yes')
                    match answ_case:
                        case 'yes':
                            if eval(exp) % 2 == 0:
                                print('Correct!')
                                right_answer += 1
                            else:
                                print(f'\'{answ}\' is wrong answer ;(.' 
                                       f' Correct answer was \'no\'.')
                                print(f'Let\'s try again, {sname}!')
                                wrong_answer = 1
                        case 'no':
                            if eval(exp) % 2 != 0:
                                print('Correct!')
                                right_answer += 1
                            else:
                                print(f'\'{answ}\' is wrong answer ;(.' 
                                       f' Correct answer was \'yes\'.')
                                print(f'Let\'s try again, {sname}!')
                                wrong_answer = 1
                        case _:
                            print(f'\'{answ}\' is wrong answer ;(.')
                            print(f'Let\'s try again, {sname}!')
                            wrong_answer = 1
                    
                case 'calc':
                    print('What is the result of the expression?')    
                    a = random.randint(1, 999)
                    b = random.choice(operators_list)
                    c = random.randint(1, 999)
                    exp = f'{a} {b} {c}'  
                    print(f'Question: {exp}')
                    answ = prompt.string('Your answer: ')
                    answ_case = booltostr(answ, str(eval(exp)))
                    try:
                        match answ_case:
                            case 'yes':
                                print('Correct!')
                                right_answer += 1
                            case 'no':
                                print(f'\'{answ}\' is wrong answer ;(.'
                                    f' Correct answer was '
                                    f'\'{str(eval(exp))}\'.')
                                print(f'Let\'s try again, {sname}!')
                                wrong_answer = 1
                            case _:
                                print(f'\'{answ}\' is wrong answer ;(.'
                                      f' Correct answer was '
                                      f'\'{str(eval(exp))}\'.')
                                print(f'Let\'s try again, {sname}!')
                                wrong_answer = 1
                    except ValueError:
                        print(f'\'{answ}\' is wrong answer ;(.'
                            f' Correct answer was \'{str(eval(exp))}\'.')
                        print(f'Let\'s try again, {sname}!')
                        wrong_answer = 1

    if wrong_answer == 0:
        print(f'Congratulations, {sname}!')
