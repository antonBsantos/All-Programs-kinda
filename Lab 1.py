#FileName: Lab 1
#Author: Anton Santos
#description: displays the revinue from the amount of differing tickets sold
#at sports game



def main():
    #Declare and initialize variables
    #float STUDENT_TICKET
    STUDENT_TICKET = 9.00

    #float SENIOR_TICKET
    SENIOR_TICKET = 12.00

    #float GENERAL_TICKET
    GENERAL_TICKET = 15.00

    #int studentTicketSold
    #int seniorTicketSold
    #int generalTicketSold
    #int ticketSold
    studentTicketSold = seniorTicketSold = genralTicketSold = 0
    #float studentTicketRevenue
    #float seniorTicketRevenue
    #float generalTicketRevenue
    #float totalRevenue
    studentTicketRevenue = seniorTicketRevenue = generalTicketRevenue = totalRevenue = 0.0

    #display intro
    print("WELCOME TO THE COOPER CITY STADIUM \n")

    #prompt for number of student tickets sold
    studentTicketSold = float(input("Enter the number of student tickets sold: "))
    #prompt for number of senior tickets sold
    seniorTicketSold = float(input("Enter the number of senior tickets sold: "))
    #prompt for number of general tickets sold
    generalTicketSold = float(input("Enter the number of general tickets sold: "))
    print()

    
    #display line
    print("********************************")

    #calculate number of tickets sold
    ticketSold = studentTicketSold + seniorTicketSold + generalTicketSold

    #display number of tickets sold
    (print("Total number of tickets sold \t%0.0f" % ticketSold))

    #calculate revenue generated
    studentTicketRevenue = studentTicketSold * STUDENT_TICKET
    seniorTicketRevenue = seniorTicketSold * SENIOR_TICKET
    generalTicketRevenue = generalTicketSold * GENERAL_TICKET
    totalRevenue = studentTicketRevenue + seniorTicketRevenue + generalTicketRevenue

    
    #display revenue generated
    print("revenue Generated\n")
    
    #display total number of tickets sold
    print("Student Tickets:\t$%0.2f" %studentTicketRevenue)
    print("Senior Tickets:\t\t$%0.2f" % seniorTicketRevenue)
    print("General Tickets:\t$%0.2f" % generalTicketRevenue)
    print("Total Revenue:\t\t$%0.2f" % totalRevenue)
    
main()    
