#Python 3.9

field = [['_','_','_'], ['_','_','_'], ['_','_','_']]
player1 = input('X - Hrac 1 napis svoje meno: ')
player2 = input('O - Hrac 2 napis svoje meno: ')

'''zapis suradnice ktore sa pouzili do listu, podla toho skontroluje ci uz niesu obsadene'''
s_list = []
round_num = 0   #cislovania kola
end_game = False    #hra bezi kym sa tato hodnota nezmeni (kym nesplni podienku winner)

def print_field():  #vytlac hracie pole
    print('  0 1 2')
    for i in range(len(field)):
        print(i, ' '.join(field[i]))

def winner():
    global end_game
    if field[0] == ['X', 'X', 'X'] or field[1] == ['X', 'X', 'X'] or field[2] == ['X', 'X', 'X']:
        print(f'Vyhral {player1}')
        end_game = True
    elif [field[0][0], field[1][0], field[2][0]] == ['X', 'X', 'X']:
        print(f'Vyhral {player1}')
        end_game = True
    elif [field[0][1], field[1][1], field[2][1]] == ['X', 'X', 'X']:
        print(f'Vyhral {player1}')
        end_game = True
    elif [field[0][2], field[1][2], field[2][2]] == ['X', 'X', 'X']:
        print(f'Vyhral {player1}')
        end_game = True
    elif [field[0][0], field[1][1], field[2][2]] == ['X', 'X', 'X']:
        print(f'Vyhral {player1}')
        end_game = True
    elif [field[0][2], field[1][1], field[2][0]] == ['X', 'X', 'X']:
        print(f'Vyhral {player1}')
        end_game = True
    elif [field[0] == ['O', 'O', 'O'] or field[1] == ['O', 'O', 'O'] or field[2]] == ['O', 'O', 'O']:
        print(f'Vyhral {player2}')
        end_game = True
    elif [field[0][0], field[1][0], field[2][0]] == ['O', 'O', 'O']:
        print(f'Vyhral {player2}')
        end_game = True
    elif [field[0][1], field[1][1], field[2][1]] == ['O', 'O', 'O']:
        print(f'Vyhral {player2}')
        end_game = True
    elif [field[0][2], field[1][2], field[2][2]] == ['O', 'O', 'O']:
        print(f'Vyhral {player2}')
        end_game = True
    elif [field[0][0], field[1][1], field[2][2]] == ['O', 'O', 'O']:
        print(f'Vyhral {player2}')
        end_game = True
    elif [field[0][2], field[1][1], field[2][0]] == ['O', 'O', 'O']:
        print(f'Vyhral {player2}')
        end_game = True
    elif ('_' in field[0]) or ('_' in field[1]) or ('_' in field[2]):
        pass
    else:
        print('Remiza')
        end_game = True

def player1_turn():
    print(f'Si na rade {player1}')
    try:
        x1 = int(input(f'{player1} zadaj suradnicu x '))
        y1 = int(input(f'{player1} zadaj suradnicu y '))
        p1_list = [x1, y1]
        if x1 not in range(0,3):
            print('Zadal si zle suradnice, skus znova')
            player1_turn()
        elif y1 not in range(0,3):
            print('Zadal si zle suradnice, skus znova')
            player1_turn()
        elif p1_list in s_list:
            print('Suradnica obsadena')
            player1_turn()
        else:
            s_list.append(p1_list)
            field[y1][x1] = 'X'
    except (ValueError):
        print('nezadal si platne cislo, zadaj znova')
        return player1_turn()

def player2_turn():
    print(f'Si na rade {player2}')
    try:
        x2 = int(input(f'{player2} zadaj suradnicu x '))
        y2 = int(input(f'{player2} zadaj suradnicu y '))
        p2_list = [x2, y2]
        if x2 not in range(0,3):
            print('Zadal si zle suradnice, skus znova')
            player2_turn()
        elif y2 not in range(0,3):
            print('Zadal si zle suradnice, skus znova')
            player2_turn()
        elif p2_list in s_list:
            print('Suradnica obsadena')
            player2_turn()
        else:
            s_list.append(p2_list)
            field[y2][x2] = 'O'
    except ValueError:
        print('nezadal si platne cislo, zadaj znova')
        player2_turn()

while end_game == False:
    print(f'Vitaj v kole {round_num}')
    round_num += 1
    player1_turn()
    winner()
    print_field()
    if end_game == True:
        break
    player2_turn()
    winner()
    print_field()
    if end_game == True:
        break
