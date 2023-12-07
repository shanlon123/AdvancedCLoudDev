import random


def rock_paper_scissors():
    rock_paper_scissors = ['rock', 'paper', 'scissors']
    user_move = input(f'Please enter your move pick from any of {rock_paper_scissors}: ')
    user_move = user_move.lower()
    print(f'Your input is {user_move.upper()}')
    computer_input = (random.choice(rock_paper_scissors)).lower()
    print(f'Computer Move is {computer_input.upper()}')

    if user_move.lower() == computer_input.lower():
        return f' No one wins, it is a draw!'

    else:
        if user_move.lower() == 'rock':
            if computer_input.lower() == 'scissors':
                return 'You win!'
            else:
                return 'Computer Wins!'

        elif user_move.lower() == 'scissors':
            if computer_input.lower() == 'rock':
                return 'You Win!'
            else:
                return 'Computer Wins!'

        elif user_move.lower() == 'paper':
            if computer_input.lower() == 'scissors':
                return 'Computer Wins!'
            else:
                return 'You Win!'

        else:
            raise Exception('User input is not Valid')
until_user_wins = 0
while until_user_wins == 0:
    game = rock_paper_scissors()
    if game.lower()== 'you win!':
        until_user_wins +=1
    print(game)