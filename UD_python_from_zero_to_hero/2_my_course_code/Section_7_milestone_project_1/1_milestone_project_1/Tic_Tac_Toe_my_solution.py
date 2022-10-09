def main_game():
    
    a1 = ' '
    a2 = ' '
    a3 = ' '
    a4 = ' '
    a5 = ' '
    a6 = ' '
    a7 = ' '
    a8 = ' '
    a9 = ' '
    
    marker_X = 'X'
    marker_O = 'O'

    player_1 = ''
    player_2 = ''
    print('\n'*40)
    
    while True: 
        player_input = input('Player 1 choose {} or {}: '.format(marker_X, marker_O))
        try:
            if player_input == marker_X:
                player_1 = 'X'
                player_2 = 'O'
                print('\n'*40)
                print('Nice, lets start the game. Player 1 goes first!')
                print('Player 1 use X')
                print('Player 2 use O')
                break
            elif player_input == marker_O:
                player_1 = 'O'
                player_2 = 'X'
                print('\n'*40)
                print('Nice, lets start the game. Player 1 goes first!')
                print('Player 1 use O')
                print('Player 2 use X')
                break
            else:
                raise ValueError
        except:
            print('\n'*40)
            print('Wrong key\nTRY BETTER')

   
    line_1 = ''
    line_2 = ''
    line_3 = ''
    col_1 = ''
    col_2 = ''
    col_3 = ''
    diog_1 = ''
    diog_2 = ''
    
    
    print('\n')
    print('         |         |         ')
    print('    {}    '.format(a7) + '|' + '    {}    '.format(a8) + '|' + '    {}    '.format(a9))
    print('         |         |         ')
    print('---------|---------|---------')
    print('         |         |         ')
    print('    {}    '.format(a4) + '|' + '    {}    '.format(a5) + '|' + '    {}    '.format(a6))
    print('         |         |         ')
    print('---------|---------|---------')
    print('         |         |         ')
    print('    {}    '.format(a1) + '|' + '    {}    '.format(a2) + '|' + '    {}    '.format(a3))
    print('         |         |         ')
    print('\n')


    count = []
    while line_1!='XXX' and line_2!='XXX' and line_3!='XXX' and col_1!='XXX' and col_2!='XXX' and col_3!='XXX' and diog_1!='XXX' and diog_2!='XXX' and\
          line_1!='OOO' and line_2!='OOO' and line_3!='OOO' and col_1!='OOO' and col_2!='OOO' and col_3!='OOO' and diog_1!='OOO' and diog_2!='OOO':
            move = input('Press 1-9 keys')
            count.append(move)
            Winner = ''      
            if len(count)%2 != 0:
                winner = 'PLAYER 1'
                if int(move) == 1:
                    a1 = player_1
                elif int(move) == 2:
                    a2 = player_1
                elif int(move) == 3:
                    a3 = player_1
                elif int(move) == 4:
                    a4 = player_1
                elif int(move) == 5:
                    a5 = player_1
                elif int(move) == 6:
                    a6 = player_1
                elif int(move) == 7:
                    a7 = player_1
                elif int(move) == 8:
                    a8 = player_1
                elif int(move) == 9:
                    a9 = player_1
                print('\n'*40)
                print('         |         |         ')
                print('    {}    '.format(a7) + '|' + '    {}    '.format(a8) + '|' + '    {}    '.format(a9))
                print('         |         |         ')
                print('---------|---------|---------')
                print('         |         |         ')
                print('    {}    '.format(a4) + '|' + '    {}    '.format(a5) + '|' + '    {}    '.format(a6))
                print('         |         |         ')
                print('---------|---------|---------')
                print('         |         |         ')
                print('    {}    '.format(a1) + '|' + '    {}    '.format(a2) + '|' + '    {}    '.format(a3))
                print('         |         |         ')
            if len(count)%2 == 0:
                winner = 'PLAYER 2'
                if int(move) == 1:
                    a1 = player_2
                elif int(move) == 2:
                    a2 = player_2
                elif int(move) == 3:
                    a3 = player_2
                elif int(move) == 4:
                    a4 = player_2
                elif int(move) == 5:
                    a5 = player_2
                elif int(move) == 6:
                    a6 = player_2
                elif int(move) == 7:
                    a7 = player_2
                elif int(move) == 8:
                    a8 = player_2
                elif int(move) == 9:
                    a9 = player_2
                print('\n'*40)
                print('         |         |         ')
                print('    {}    '.format(a7) + '|' + '    {}    '.format(a8) + '|' + '    {}    '.format(a9))
                print('         |         |         ')
                print('---------|---------|---------')
                print('         |         |         ')
                print('    {}    '.format(a4) + '|' + '    {}    '.format(a5) + '|' + '    {}    '.format(a6))
                print('         |         |         ')
                print('---------|---------|---------')
                print('         |         |         ')
                print('    {}    '.format(a1) + '|' + '    {}    '.format(a2) + '|' + '    {}    '.format(a3))
                print('         |         |         ')
            line_1 = a1+a2+a3
            line_2 = a4+a5+a6
            line_3 = a7+a8+a9
            col_1 = a1+a4+a7
            col_2 = a2+a5+a8
            col_3 = a3+a6+a9
            diog_1 = a1+a5+a9
            diog_2 = a3+a5+a7
            
    return print('\nAND THE WINNER IS {}'.format(winner))

main_game()
