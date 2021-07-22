while True:
    name = input("What is your name? ")
    goldInBank = input("How much gold is in your bank? ")
    goldInWallet = input("How much gold is in your wallet? ")


    if (goldInBank.isnumeric() and goldInWallet.isnumeric()):
        goldInBank = int(goldInBank)
        goldInWallet = int(goldInWallet)

        totalGold = goldInBank + goldInWallet

        print(name + " has " + str(totalGold) + " in total ")

        if totalGold > 1000000:
            print("ur rich :/")
        elif totalGold < 100:
            print("man that's sad ")
        else:
            print("You're middle class den ")

        break
    else:
        print('Please input a numeric value')
