from random import randint


print('Welcome to my Rock paper scissor game. ')

# 1 == Rock
# 2 == Paper
# 3 == Scissors
# Rock beats Scissors
# Paper beats Rock
# Scissors beats paper

player = input('Options 1.Rock 2.Paper 3.Scissors. Choose a number.')
player = int(player)
if int(player) > 3:
    print('Invalid Entry')

computer = randint(1,3)

def game(player, computer):
    if (computer == 1) and (player == 2):
        print('Paper beats rock. You win!')
    elif (computer == 1) and (player == 3):
        print('Rock beats scissors. You lost!')
    elif (computer == 2) and (player == 1):
        print('Paper beats rock. You lose!')
    elif (computer == 2) and (player == 3):
        print('Scissors beats paper. You win!')
    elif (computer == 3) and (player == 1):
        print('Rock beats scissors. You lose!')
    elif (computer == 3) and (player == 2):
        print('Scissors beats paper. You lose!')
    else: print('You tied!')

game(computer, player)