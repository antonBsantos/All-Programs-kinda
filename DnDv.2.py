def main():
    #Declare and initialize variables
    total_points = 0.0
    menu_choice = " "



    card1_points = 5
    card2_points = -2
    card3_points = 1
    card4_points = -4
    card5_points = 5
    card6_points = -3
    card7_points = 2

    #const
    rules = ("You progress through the game by picking up cards, trying to move forward.\n"
             "Every turn you are given a new card.\n"
             "These cards  will be either beneficial or detrimental, giving or taking away spaces."
             "You can have negative spaces."
             "Your goal is to move forward 50 spaces.")

    intro = ("Welcome to DnD BoardgameV.2, we hope you have a fun time!")

    card1 = ("You have found an enchanted bow, you see the runes were written by ancient elves."
              "You fire the bow and notice anything hit with it freezes over, move foward 5 spaces.")
    card2 = ("You tried to use a magic scroll without knowing its incantation, it slowly starts "
             "glowing red and... it blows up in your face, move backwards 4 spaces.""
    card3 = ("As you are crossing the countryside a wayward priest seems to have fallen asleep on the"
             "road. You awake him and remind him of the dangers of bandits, and as a thank you he"
             "blesses you on your journy, move foward 1 space.")
    card4 = ("On your travels your belongings were stolen when you slept! They took everything from the"
             "food to the lamps to even your prized dragon figurine, move backwards 4 spaces.")
    card5 = ("While fighting a dragon, it seems to lose its balance and fall with all its might "
             "HEART FIRST on your sword! Move foward 5 spaces.")
    card6 = ("You come across a rowdy drinker in the local tavern, challenging you to a drinking contest"
             "being proud in you ability you accept... and awake with your belongings gone, move backward 3 spaces.")
    card7 = ("A wandering bear comes into your camp in the middle of a cold and frozen night..."
             "he then procedes to sleep next to you, giving him and you warmth, move fowards 2 spaces.")

    next_card = "Please enter ""next"" to get the next card: "
    next_card_choice = " "
    distance_intro = "You have traveled"
    divider = "--------------------------------------------------------"

    #display menu
    #prompt for menu choice
    print("1) Start Game")
    print("2) Rules")
    print("3) Exit")
    print()
    menu_choice = int(input("Select an option: "))

    if menu_choice == 3:
        quit()

    if menu_choice == 2:
        print(divider)
        print(rules)
        print()
        print("1) Start Game")
        print("2) Rules")
        print("3) Exit")
        print()
        menu_choice = int(input("Select an option:"))

    if menu_choice == 1:
        print()
        print(intro)
        print(divider)
        print(card1)
        #calculate total_points
        total_points = card1_points
        print()
        print(distance_intro,total_points,"spaces")
        print()
        #prompt for next card
        next_card_choice = input(next_card)

    if next_card_choice == "next":
        print(divider)
        print()
        print(card2)
        print()
        #calculate total_points
        total_points = total_points + card2_points
        #Display total_points
        print(distance_intro,total_points,"spaces")
        print()
        next_card_choice = input(next_card)

    if next_card_choice == "next":
        print(divider)
        print
        print(card3)
        print()
        #calculate total_points
        total_points = total_points + card3_points
        #Display total_points
        print(distance_intro,total_points,"spaces")
        print()
        next_card_choice = input(next_card)

    if next_card_choice == "next":
        print(divider)
        print()
        print(card4)
        print()
        #calculate total_points
        total_points = total_points + card4_points
        #Display total_points
        print(distance_intro,total_points,"spaces")
        print()
        next_card_choice = input(next_card)

    if next_card_choice == "next":
        print(divider)
        print()
        print(card5)
        print()
        #calculate total_points
        total_points = total_points + card5_points
        #Display total_points
        print(distance_intro,total_points,"spaces")
        print()
        next_card_choice = input(next_card)

    if next_card_choice == "next":
        print(divider)
        print()
        print(card6)
        print()
        #calculate total_points
        total_points = total_points + card6_points
        #Display total_points
        print(distance_intro,total_points,"spaces")
        print()
        next_card_choice = input(next_card)

    if next_card_choice == "next":
        print(divider)
        print()
        print(card7)
        print()
        #calculate total_points
        total_points = total_points + card7_points
        #Display total_points
        print(distance_intro,total_points,"spaces")
        print()
        next_card_choice = input(next_card)



    if menu_choice == 3:
        quit()
main()
