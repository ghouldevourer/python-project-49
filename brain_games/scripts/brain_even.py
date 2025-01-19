from random import randint

import prompt


def main():
    print('Welcome to the Brain Games!')
    sname = prompt.string('May I have your name? ')
    print('Hello,', sname)
    print('Answer "yes" if the number is even, otherwise answer "no".')
    num_list = [randint(1, 999), randint(1, 999), randint(1, 999)]
    right_answer = 0
    wrong_answer = 0
    for i in num_list:
        if (right_answer < 3) and (wrong_answer == 0):    
            num = i
            print(f'Question: {num}')
            answ = prompt.string('Your answer: ')
            match answ:
                case 'yes':
                    if num % 2 == 0:
                        print('Correct!')
                        right_answer += 1
                    else:
                        print(f'\'{answ}\' is wrong answer ;(.' 
                              f' Correct answer was \'no\'.')
                        print(f'Let\'s try again, {sname}!')
                        wrong_answer = 1
                case 'no':
                    if num % 2 != 0:
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
    if wrong_answer == 0:
        print(f'Congratulations, {sname}!')
