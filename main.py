import random

def roll_dice():
    dice = random.randint(1,6)
    return dice

def main():
    playerOne = input('Player One - Please enter your name: ')
    print(f'Hello, {playerOne}')

    playerTwo = input('Player Two - Please enter your name: ')
    print(f'Hello, {playerTwo}')

    winsPlayer1 = 0
    winsPlayer2 = 0 
    rounds = 1 

    while rounds != 3:
        print('Round '+ str(rounds))
        p1 = roll_dice()
        p2 = roll_dice()
        print(playerOne + ' Roll: ' + str(p1))
        print(playerTwo + ' Roll: ' + str(p2))

        if p1 > p2:
            winsPlayer1 = winsPlayer1 + 1
            print(playerOne + ' wins! \n')
        elif p2 > p1:
            winsPlayer2 = winsPlayer2 + 1
            print(playerTwo + ' wins! \n')
        else:
            print('Draw! \n')

        rounds = rounds + 1 

    if winsPlayer1 > winsPlayer2:
        print(playerOne + ' Wins - Rounds Won: '+ str(winsPlayer1))
    elif winsPlayer2 > winsPlayer1:
        print(playerTwo + ' Wins - Rounds Won: '+ str(winsPlayer2))
    else:
        print('Draw!')

if __name__ == '__main__':
    main()
