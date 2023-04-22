import random
from tabulate import tabulate

print("""
Welcome to Tic-Tac-Toe game.
Let's play!
""")

def print_nice_table(data_set, board_size):
    ''' print 1D list in tabular format '''
    k=0
    table = [['' for x in range(board_size)] for y in range(board_size)]
    for i in range(board_size):
        for j in range(board_size):
            table[i][j]= data_set[k]
            k += 1
    print(tabulate(table, tablefmt='grid')) 


def is_the_winner(data_set, board_size, mark):
    ''' check if 3 x mark (e.g.'X' or 'O') in rows, columns,
        main diagonal and secondary diagonal of game board '''
    m = len(data_set)
    n = board_size
    if all(field == mark for field in data_set[0:n]) \
        or all(field == mark for field in data_set[:2*n]) \
        or all(field == mark for field in data_set[2*n:3*n]) \
        or all(field == mark for field in data_set[0:m:3]) \
        or all(field == mark for field in data_set[1:m:3]) \
        or all(field == mark for field in data_set[2:m:3]) \
        or all(field == mark for field in data_set[0:m:4]) \
        or all(field == mark for field in data_set[2:m-1:2]):
        return True
    else:
        return False      
   
# game starts
while True:
    n=3 # set the game board size

    # generating the list of field indexes 
    fields = []
    for i in range(n):
        for j in range(n):
            fields.append(str(i+1) + str(j+1))
    remains = fields[:]

    # printing the game board
    while True:
        print_nice_table(fields, n)
            
    # checking: is the winner?     
        if is_the_winner(fields, n, 'X'):
            print('Congratulations!\nYou won!')
            break
        elif is_the_winner(fields, n, 'O'):
            print('Player_2 won')
            break

    # player selection
        player1 = ''
        while player1 not in remains:
            player1 = input('Choose a field number: ')         

        remains.remove(player1)
        fields = ['X' if field == player1 else field for field in fields]

    # random player2 selection
        if len(remains)!= 0:  
            player2 = random.choice(remains)
            print('Player_2 selected: '+ player2+'\n')
            remains.remove(player2)
            fields = ['O' if field == player2 else field for field in fields]
        else:
            print('Draw!\nGame over')
            break
         
    answer = input('Do you want to play again? (y/n) ')
    print('')
    answer = answer.lstrip().lower()
    if answer.startswith('y')==False:
       break
