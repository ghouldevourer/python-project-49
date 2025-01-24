import prompt

from brain_games.scripts.brain_calc import main as brain_calc
from brain_games.scripts.brain_even import main as brain_even
from brain_games.scripts.brain_gcd import main as brain_gcd
from brain_games.scripts.brain_prime import main as brain_prime
from brain_games.scripts.brain_progression import main as brain_progression


def main():
    # name = welcome_user()
    print('From here you can select the game you are interested in.')
    print('1. Brain Even. Let\'s check how much you understand about parity.')
    print('2. Brain Calc. Let\'s see how good you are with arithmetic.')
    print('3. Brain GCD. Let\'s check if you know '
          'what the greatest common divisor is.')
    print('4. Brain Progression. Let\'s see if you can '
          'find a pattern in a series of numbers.')
    print('5. Brain Prime. Let\'s check what you know about prime numbers.')
    answer = prompt.string('Enter a game number: ')
    match answer:
        case '1':
            brain_even()
        case '2':
            brain_calc()
        case '3':
            brain_gcd()
        case '4':
            brain_progression()
        case '5':
            brain_prime()
        case _:
            print('Good Bye!')

