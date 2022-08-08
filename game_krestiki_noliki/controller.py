import console_using as console


def is_win(board):
    win_coords = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for elem in win_coords:
        if board[elem[0]] == board[elem[1]] == board[elem[2]]:
            return board[elem[0]]
    return False


def game(field=[' ' for x in range(1, 10)]):
    counter = 0
    win = False
    symbol = 'X'
    while not win:
        console.view.draw_field(field)
        if counter % 2:
            field[console.input.player_choise(symbol, field) - 1] = symbol
            symbol = 'X'
        else:
            field[console.input.player_choise(symbol, field) - 1] = symbol
            symbol = '0'
        counter += 1
        if counter > 4:
            temp = is_win(field)
            if temp:
                print(f'{temp} is win')
                win = True
                break
        if counter == 9:
            print('Nobody win')
            break