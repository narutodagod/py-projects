import random

dice = random.randint(1, 6)

player0pts = 0
player1pts = 0
maxScore = 100

roundScore = 0
playerTurn = 0
safePts = 0

stopping = False

while player0pts < maxScore and player1pts < maxScore:
    if playerTurn == 1:
        safePts = player1pts
    else:
        safePts = player0pts
    print('======= NEW ROUND =======')
    print('It is Player ' + str(playerTurn + 1) + "'s turn.")
    print('\t Total Score: ' + str(safePts))
    print('\t Round Score: ' + str(roundScore))
    print()
    rolling = input('Would you like to roll for more points or save what you have? (R or S) ').lower()
    if rolling == 'r' or rolling == 'roll':
        dice = random.randint(1, 6)
        print('Player ' + str(playerTurn + 1) + ' rolled a ' + str(dice))
        if dice == 1:
            print(' oof u got a one, you lost ' + str(roundScore) + ' points, stop making me feel bad')
            print(' You have ' + str(safePts) + ' total points')
            stopping = True
            roundScore = 0
        else:
            roundScore += dice
    elif rolling == 's' or rolling == 'save':
        stopping = True

    else:
        print()
        print('\tPlease enter a R (roll) or S (save)')

    if stopping:
        if playerTurn == 0:
            player0pts += roundScore
        else:
            player1pts += roundScore
        print()
        print('Your total score is ' + str(safePts + roundScore))
        print()
        roundScore = 0
        stopping = False
        if playerTurn == 0:
            playerTurn = 1
        else:
            playerTurn = 0


if player0pts >= maxScore:
    print('Player 1 wins with a score of ' + str(player0pts) + '\n\t ggz bro')
else:
    print('Player 2 wins with a score of ' + str(player1pts) + '\n\t ggz bro')
