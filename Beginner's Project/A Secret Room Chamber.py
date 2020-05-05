#A secret Room Chamber...
# Here i am gonna code for a basic TextBased Adventure game. Actually it is a game where the adventurer only play with string/text and also directed by text.
#So let's start.......!

#First Step -- let's take an array to store answers and another array to store the directions..#

from random import randint
answers = ["yes", "Yes", "YES", "YeS", "no", "No", "NO", "nO"]
directions = ["East", "West", "North", "South"]

# This part is our Introduction part.

print("\'Welcome To Secret Room Chamber.\'")
name = input("Please Tell Your Name: \n")
print("I am glad to see you here", name, ".", "You are in a cave, so it's difficult to get back from here!\nDo you want to explore The room? ")

#This is starting part of the game

ans = ""
while ans not in answers:
    ans = input("So, are you ready?")
    if ans == "yes" or ans == "Yes" or ans == "YES" or ans == "YeS":
        print("\nThen go ahead\n")
    elif ans == "no" or ans == "No" or ans == "NO" or ans == "nO":
        print("You are not ready yet")
        print("GoodBye,", name)
        quit()
    else:
        print('I did not understand what are you saying! :(\n')

    # Here is next part ,,,, After saying yes!

    reply = ""
    ans = ""

    while reply not in directions:
        print("In the East side, You will explore a locked door.")
        print("In the North side, You will see a wall")
        print("In the South, You will see a large box arrounded by snakes.")
        print("In the West, there is door to exit the room.")
        print("\n")

        reply = input("Which direction do you want to move? East or West or North or South?\n")

        if reply == "East":
            # here we will play a guessing game
            print("In front of you there is a locked door.\nYou can unlocked the door if you play a guessing game and win the game.")
            print("After wining, the door will open automatically and you can exit secret room safely.")
            while ans not in answers:
                ans = input("Do you want to play?")
                if ans == "yes" or ans == "Yes" or ans == "YES" or ans == "YeS":
                    print("Ok,Let's play.")
                    for x in range(1, 6):
                        guess_num = int(input("Enter a number between 1 to 5: "))
                        randomNumber = randint(1, 5)

                        if guess_num == randomNumber:
                            print("Hurray!!You have won.")
                            print("Yor are safe now", name)
                            print("Please go your home. Goodbye!")
                            quit()
                        else:
                            print("OH!dear,You have lost")
                            print("The random number was ", randomNumber)
                elif ans == "no" or ans == "No" or ans == "NO" or ans == "nO":
                    print("You are not ready yet")
                    print("GoodBye,", name)
                    quit()
                else:
                    print('I did not understand what are you saying! :(\n')
        elif reply == "North":
            print("In front of you there is a wall and you cannot escape from this.")
        elif reply == "South":
            print("Oh my god! Those snakes are baneful!")
        elif reply == "West":
            print("You leave the room.Goodbye,", name)
            quit()
        else:
            print("You are out of the room.")











