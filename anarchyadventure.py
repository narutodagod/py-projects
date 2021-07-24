choice = -1


def getInput(choices):
    while True:
        num = input()
        try:
            num = int(num)
        except:
            print()
            print(f'Please enter a number from 1 to {choices}')
        else:
            if 0 < num <= choices:
                return num
            else:
                print(f'Please enter a number from 1 to {choices}')


def playAgain():
    again = input("Would you like to play again? (Y or N)").lower()
    while again == 'y':
        start()
        print('===============================================')
        print()
        again = input("Would you like to play again? (Y or N) ").lower()
        print()
    print('Thank you for playing')
    return


def start():
    print('')
    print('You have been trapped in a black box and you have no room to move and you hear people around you')
    print('What do you do?')
    print()
    print('1. Yell at the mysterious people to help you')
    print('2. Escape from the black box and run')
    print('3. Escape and ask the people where you are and what happened')
    choice = getInput(3)
    if choice == 1:
        print('They told you they were your enemy and you sat there and oofed of hunger')
        print('GAME OVER')
        return
    elif choice == 2:
        print('You were smart and decided not to talk to them and you escaped')
    else:
        print('After you escaped they took you and threw you into a 50ft pit and u oofed')
        print('GAME OVER')
        return

    print('You keep running until you see another person who is in full enchanted diamond armour')
    print('You walk up to him and he gives you a special enchanted golden apple')
    print()
    print('1. You decide to talk to him')
    print('2. You take it and run')
    choice = getInput(2)

    if choice == 1:
        print('You talk to him and make a new friend and he then decides to give you a kit full of goods')
    else:
        print("He doesnt appreciate that you just ran away and didn't talk to him so he shoots you with his bow")
        print('GAME OVER')
        return

    print('Now that you are kitted and made a new friend you can leave spawn')
    print("But you don't know which way to go")
    print()
    print('1. You travel on the North highway')
    print('2. You travel on the East highway')
    print('3. You travel on the South highway ')
    print('4. You travel on the West highway')
    choice = getInput(4)

    if choice == 1:
        print('You went the right away and did not encounter anybody else')
        return
    elif choice == 2:
        print('You ended up getting blown up by invisible pvpers on the highway')
        return
    elif choice == 3:
        print('You have autowalk on and end up drowning in water cube spawn')
        return
    else:
        print('You ended up getting out of spawn and now are free')

    print('Woah you have made it this for you are pretty special')
    print('Now that you have escaped spawn')
    print('You have to decide where to make a base')
    print()
    print('1. Make a sky base')
    print('2. Make an underground base')
    print('3. Make an above ground base')
    choice = getInput(3)

    if choice == 1:
        print("No one found your base and it wasn't greifed")
    elif choice == 2:
        print('Someone noticed your e chest and chests when they had esp on so they raidied your base and griefed it')
        return
    else:
        print("You didn't go far enough out to build a regular above ground base")
        return

    print('Since you have made it this far you seem like you have some pretty good luck')
    print('So which way do you want to test your luck?')
    print()
    print('1. You go back to spawn and cpvp')
    print('2. You go to netherspawn and cpvp')
    choice = getInput(2)

    if choice == 1:
        print('Some kid with a better client and configs destroyed you in an instant.  Next time make sure you have '
              'more totems')
        return
    else:
        print('You join the portal trappers and kill new players, such fun')

    print('You are now a verifed chad')
    print('This is only the first part of your adventure')
    print()
    print('1. Go dupe 32ks and kits')
    print('2. You go to the world border')
    choice = getInput(2)

    if choice == 1:
        print('Your stash ends up getting found but its fine')
    else:
        print('Cool you made it to world border')

    print('Now you have become a pro at epic')
    print('So do you want to')
    print('')
    print('1. Give noobs kits')
    print('2. Base find')
    choice = getInput(2)

    if choice == 1:
        print('good boi u made alot of peoples days')
    else:
        print('woah u found a pretty dope base')

    print('so you then join a group named the yakuza and you go to a base 260k in the end that is so big u cant '
          'comprehend it')
    print()
    print('1. You grief it')
    print('2. You steal the items')
    choice = getInput(2)

    if choice == 1:
        print('good boy you and the yakuza griefed it')
    else:
        print('the yakuza wanted you to greif it and you didnt so they killed you')
        return

    print('You are now on the second part of your adventure')
    print('')
    print('1. Greif another base')
    print('2. cheese pizza')
    choice = getInput(2)

    if choice == 1:
        print('you already griefed 1 base thats enough')
        return
    else:
        print('good boy no more greifing and cheese pizza')

    print('wow u are epic cool dude epic games')
    print('idk what to make so I put this now')
    print('go play roblox')
    food = input('what is ur favorite food? ')
    print(f'you like to eat {food}')
    print('or ')
    print('you eat donut')
    print('hab good day now :))')


start()
playAgain()
