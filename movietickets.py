# Katherine Morris
# Prog Purpose: This program finds the cost of movie tickets.

#   Price for one ticket: $10.99
#   Sales tax rate: 5.5%

import datetime
########## difine glabal variables ##########
# define tax rate and prices
SALES_TAX_RATE = .055
PR_TICKET = 10.99

# define global variables
num_tickets = 2
subtotal = 0
salestax = 0.055
total = 0

########## define program functions ##########
def main():
    
    more_tickets: true
    
    while more_tickets:
       get_user_data()
       perform_calculations()
       display_results

       yesno==input("Would you like to order again (y or no)?")
       if yesno=="N" or yesno== "n":
           more_tickets=False
           print("Thank you for your order. Enjoy your movie!")
           total = subtotal + sales_tax

def display_results():
    print('--------------------------')
    print('****CINEMA HOUSE MOVIES****')
    print('Your neighborhood movie house')
    print('----------------------------')
    print('Tickets    $ ' +str(subtotal, '8,.2f'))
    print('Sales Tax   $ ' +str(sales_tax, '8,.2f'))
    print('Total       $ ' +str(total, '8,.2f'))
    print('------------------------------')
    print(str(datetime.datetime.now()))

########### call on main program to execute #############
main()

