def main():
    #declare and initalize variables
    student_average = 0 
    days_missed = 0

    

    print("Welcome to my progam!")
    print()
    print("We will see whether or not you can exempt the final exam.")

    student_average = -1
    days_missed = -1

    while student_average <= 0 or student_average > 100 and days_missed < 0:
        #promt for student average
        student_average = int(input("What is your class average? "))

        #prompt for days missed
        days_missed = int(input("How many days of school have you missed this year? "))
        
        if student_average >= 96 and student_average <= 100:
            print("You can exempt because your class average is above 96.")

        elif student_average >= 93 and student_average <= 100 and days_missed < 3:
            print("You can exempt because your average is above 93 and you've missed less than 3 days.")

        elif student_average >= 90 and student_average <= 100 and days_missed == 0:
            print("You can exempt because your average is above 90 and you've missed zero days.")
            
        elif student_average < 90 and student_average > 0 and student_average < 93 and student_average > 0 or days_missed > 0 and student_average < 96:
            print("You cannot exempt the final exam")
        else:
            print("Invalid input, please try again")
            print()
            print("********************")
            print()
            
    

main()
