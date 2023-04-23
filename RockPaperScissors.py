import random

print("""
  Welcome to Paper-Rock-Scissors game.
  Let's play!
""")

options={1:'paper' , 2:'rock', 3:'scissors'}

while True:
    [score_player1, score_player2]  = [0, 0]
    rounds = int(input('How many rounds? : '))
    for _ in range(rounds):
        player1 = ''
        while player1 not in ['1', '2', '3']:
            print('''\nOptions:
    1 - paper    2- rock    3 - scissors
            ''')
            player1 = input('Choose number 1, 2 or 3: ')
        player1 = int(player1)
        print('Your choice: ', options[player1])

    # random player 2 selection
        player2 = random.choice([1, 2, 3])
        print("Player2's choice: ", options[player2])

        compare = player1 - player2
        if compare == -1 or compare == 2:
            score_player1 += 1
        elif compare == 1 or compare == -2:
            score_player2 += 1
        else:
            score_player1 += 1
            score_player2 += 1
        print(f'the current score {score_player1}:{score_player2}')
    
    if score_player1 > score_player2:
        print(f'\nGame result {score_player1}:{score_player2}\n Congratulations! You won!')
    elif score_player1 < score_player2:
        print(f'\nGame result {score_player1}:{score_player2}\n Player_2 won')
    else:
        print(f'\nGame result {score_player1}:{score_player2}\n Draw')
        
    answer = input('Do you want to play again? (y/n) ')
    print('')
    answer = answer.lstrip().lower()
    if answer.startswith("y")==False:
        break
