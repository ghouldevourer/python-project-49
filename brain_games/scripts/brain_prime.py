from brain_games.cli import chk_answer, welcome_user


def main():
    sname = welcome_user()
    chk_answer('prime', sname)