#exempt_Algorithm
#author: Anton Santos
#Description: This program asks for a students average grade along with the
#students number of days missed to see if they can exempt the final exam.

def main():
    #initialize variables
    #float student_average
    student_average = 0.0
    #int days_missed
    days_missed = 0
    #text for being able to exempt and not able
    can_exempt_96 = "You can exempt from the final exam becuse your average is at least 96."
    can_exempt_93 = "You can exempt from the final exam because your average is at least 93 and you missed less than 3 days."
    can_exempt_90 = "You can exempt from the final exam because your average is at least 90 and you have perfect attendance"
    cannot_exempt = "You can not exempt the final exam"
    wrong_input = ("Please input an average that is non-negative and below 100\n"
                    "Also please input a non-negative value for days missed")

    #Display the introduction
    print("Welcome to the exemption program!")
    print("This program will see if you can exempt the final exam or not.")
    print()

    #calculate to see if the student can exempt, including input validation
    student_average = -1
    days_missed = -1
    while student_average < 0 or student_average > 100 or days_missed < 0:
        #Prompt the user for a students average
        student_average = float(input("What is your average for the class?: "))
        #prompt the user for number of  days days_missed
        days_missed = int(input("How many days of school have you missed?: "))
        if student_average >= 96 and student_average <= 100 and days_missed >= 0:
            print(can_exempt_96)
        elif student_average >= 93 and student_average < 96 and days_missed <= 3 and days_missed >= 0:
            print(can_exempt_93)
        elif student_average >= 90 and student_average <93 and days_missed == 0:
            print(can_exempt_90)
        elif student_average < 90 and student_average > 0 or days_missed > 0 and student_average < 93 and student_average > 0 or days_missed > 0 and student_average < 96:
            print(cannot_exempt)
        else:
            print(wrong_input)
            print()
            print("******************************************************")
            print()
main()
