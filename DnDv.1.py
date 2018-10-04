#File Name: boardGamev1.py
#Group Members: Anton Santos, Matthew Coleman, Maxwell Jakus, Max Santos

def main():
    #Define and initialize variables
    #Disply intro
    #Prompt userName
    #Prompt menuChoice
    #(for now) Display rules
    #(for now) Display 3 potential cards

    #Define and initialize variables
    userName = ""

    #display introduction
    print("Welcome to our D&D board game!")

    #prompt user for his/her name
    userName = input("Please tell me your name: ")

    #display the main menu (1.See Rules 2.Play Game 3.Exit)
    print("1.See Rules")
    print("2.Play Game")
    print("3.Exit")

    #prompt the user for the main menu choice
    menuChoice = input("Select your choice: ")

    #display the rules of the game
    print("You progress through the game by picking up cards, trying to move forward")
    print("Every turn you are given a new card")
    print("These cards can will be either beneficial or detrimental")
    print("Your goal is to move forward 50 spaces")


    #display 3 card scenarios and their point values
    print("You have found an enchanted bow, move forward 5 spaces")
    print("You tried to use a magic scroll… it blew up if your face, move backwards 5 spaces")
    print("A priest blessed you on your travels, move forward 3 spaces")
    print()
    print("This is version 1 of our DnD Project")
main()
