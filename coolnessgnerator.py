import random
coolPeople = ['','','','','','','','','','']
for i in range(len(coolPeople)):
    coolness = random.randint(0, 50)
    print(f"{coolPeople[i]} has a coolness of {coolness}")


