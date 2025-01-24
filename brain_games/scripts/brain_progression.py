import random

from brain_games.cli import chk_answer, welcome_user


def main():
    name = welcome_user()
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
    chk_answer(question, correct_answer, name)