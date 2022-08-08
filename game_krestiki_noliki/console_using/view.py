from os import system

def draw_field(field: list) -> None:
    system('cls')
    print('-------------')
    for i in range(3):
        print(f'| {field[0+i*3]} | {field[1+i*3]} | {field[2+i*3]} |')
        print('-------------')