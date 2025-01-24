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


def chk_answer(question, correct_answer, name):
    right_answers = 0
    for _ in range(3):
        print(question)
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            right_answers += 1
        else:
            print(f'\'{user_answer}\' is wrong answer ;(. '
                  f'Correct answer was \'{correct_answer}\'.')
            print(f'Let\'s try again, {name}!')
            break
    if right_answers == 3:
        print(f'Congratulations, {name}!')
