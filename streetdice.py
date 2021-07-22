import random

gameOver = False
while gameOver == False:
    rolling = input("Would you like to roll (Yes)or (No)?   ")
    if rolling.lower() == 'y' or rolling.lower() == 'yes':
        dieOne = random.randint(1,6)
        dieTwo = random.randint(1,6)
        if dieOne == dieTwo or dieOne + dieTwo == 7 or dieOne + dieTwo == 11:
            print('You rolled a ' + str(dieOne) + 'and ' + str(dieTwo) + ' which is a total of ' + str(dieOne+dieTwo))
            print('how de heck did u win')
            if dieOne == dieTwo and dieOne == 1:
                print('You rolled a snake eyes lucky boi')
            gameOver = True
        else:
            print('You rolled a ' + str(dieOne) + 'and ' + str(dieTwo) + ' which is a total of ' + str(dieOne + dieTwo))
            print('oof u no win 1!!1')
            print('-------Next Round-------')
            pass
    else:
        gameOver = True
