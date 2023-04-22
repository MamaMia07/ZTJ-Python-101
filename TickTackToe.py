import random

print("""
Welcome to Tic-Tac-Toe game.
Let's play!
""")

n=3 # game board size

while True:
    # generating field indexes
    fields = []
    for i in range(n):
        for j in range(n):
            fields.append(str(i+1) + str(j+1))
    remains = fields[:]


    # printing the game board
    while True:
        k=0
        print('  -- '*3)
        for i in range(n):
            for j in range(n):
                print(f'| {fields[k]} ',end='')
                k += 1
            print('|')
            print('  -- '*3)
        print('')

    # checking:  3 x 'X'  or  3 x 'O' 
        m = len(fields)
        if all(field == "X" for field in fields[0:n]) \
            or all(field == "X" for field in fields[n:2*n]) \
            or all(field == "X" for field in fields[2*n:3*n]) \
            or all(field == "X" for field in fields[0:m:3]) \
            or all(field == "X" for field in fields[1:m:3]) \
            or all(field == "X" for field in fields[2:m:3]) \
            or all(field == "X" for field in fields[0:m:4]) \
            or all(field == "X" for field in fields[2:m-1:2]):
                print("Congratulations!\nYou won!")
                break

        elif all(field == "O" for field in fields[0:n]) \
              or all(field == "O" for field in fields[n:2*n]) \
              or all(field == "O" for field in fields[2*n:3*n]) \
              or all(field == "O" for field in fields[0:m:3]) \
              or all(field == "O" for field in fields[1:m:3]) \
              or all(field == "O" for field in fields[2:m:3]) \
              or all(field == "O" for field in fields[0:m:4]) \
              or all(field == "O" for field in fields[2:m-1:2]):
                  print("Player 2 won")
                  break

    # player selection
        player1 = ''
        while player1 not in remains:
            player1 = input('Choose a field number: ')
        
        
        remains.remove(player1)
        fields = ['X' if field == player1 else field for field in fields]

        # random player 2 selection
        if len(remains)!= 0:  # to na warunek petli
            player2 = random.choice(remains)
            print('Player2 selected: '+ player2+'\n')
            remains.remove(player2)
            fields = ['O' if field == player2 else field for field in fields]
        else:
            print("Draw!\nGame over")
            break
        #elif all(fields[0,4,6] or

        #warunek +=2       
     
    answer = input('Do you want to play again? (y/n) ')
    print('')
    answer = answer.lstrip().lower()
    if answer.startswith("y")==False:
       break
