#Filename: Kilometers to Miles
#Date: Septembet 3, 2018
#Name: Anton Santos
#Description: This program converts kilometers to miles, typically in this
#sense as a distance traveled.


#define main function
def main():
    #Declare and initialize variables and constants
    #float kilometerTravel
    kilometerTravel = 0.0
    #float mileTravel
    mileTravel = 0.0
    #const float conversionConstant
    conversionConstant = 0.621371

    #Display intro to user
    print("Welcome to Anton's mile conversion program!")
    print()
    #Display use of program to user

    print("I will ask you for a number of kilometers and")
    print("then convert it how many miles you traveled")
    print()

    #Prompt for name
    userName = (input("What is your name?: "))
    print()

    #Prompt for number of kilometers
    kilometerTravel = float(input("Enter total number of kilometers: "))
    print()

    #Display Thank user
    print("Thank you", userName)

    #Calculate number of miles from number of kilometers
    mileTravel = kilometerTravel * conversionConstant

    print()
    #Display mileTravel
    print("Congratulations!!!, you have traveled:\t%0.1f" % mileTravel, "miles" )
    #Display end thanks
    print("Thank you for using my program, come again!")
main()