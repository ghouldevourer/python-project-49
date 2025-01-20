import prompt

from brain_games.cli import chk_answer, welcome_user


def main():
    sname = welcome_user()
    print('From here you can select the game you are interested in.')
    print('1. Brain Even. Let\'s check how much you understand about parity.')
    print('2. Brain Calc. Let\'s see how good you are with arithmetic.')
    print('3. Brain GCD. Let\'s check if you know '
          'what the greatest common divisor is.')
    print('4. Brain Progression. Let\'s see if you can '
          'find a pattern in a series of numbers.')
    print('5. Brain Prime. Let\'s check what you know about prime numbers.')
    answ = prompt.string('Enter a game number: ')
    match answ:
        case '1':
            chk_answer('even', sname)
        case '2':
            chk_answer('calc', sname)
        case '3':
            chk_answer('gcd', sname)
        case '4':
            chk_answer('progression', sname)
        case '5':
            chk_answer('prime', sname)
        case _:
            print('Good Bye!')

