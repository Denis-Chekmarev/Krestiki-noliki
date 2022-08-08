from progress.bar import Bar
from time import sleep


def player_choise(symbol: str, board: list) -> int:
    valid = False
    while not valid:
        player_input = input(f'Chose the place for {symbol} -> ')
        try:
            player_input = int(player_input)
        except ValueError:
            print('Wrong input. Please input the number from 1 to 9 --> ')
            continue
        if 1 <= player_input <= 9:
            if str(board[player_input-1]) == ' ':
                valid = True
            else:
                print('This element is not empty. Try again --> ')
        else: 
            print('Wrong input. Input the number from 1 to 9 --> ')
    bar = Bar('Reading your choice', max=20)
    for i in range(20):
        sleep(0.05)
        bar.next()
    bar.finish()
    return player_input