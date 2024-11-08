# Name: Katherine Morris
# Prog Purpose: This program finds the cost of a meal at Branch Barbeque Buffet.
#   Price for an adult meal: $19.95
#   Price for a child meal: $11.95
#   Service fee: 10%
#   Sales tax rate: 6.2%

import datetime

#################### define glabal variables ########################
# define tax rate, service fee, and prices
ADULT_MEAL = 19.95
CHILD_MEAL = 11.95
SALES_TAX_RATE = .062
SERV_FEE = .10

# define global variables
num_adult_meals = 0
num_child_meals = 0
sales_tax = 0
service_fee = 0
subtotal_adult = 0
subtotal_child = 0
subtotal = 0

###################### define program functions #####################
def main():

    more_meals = True

    while more_meals:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input("\nWould you like to order again (Y or N)")
        if yesno == "N" or yesno == "n":
            more_meals = False
            print("Thank you for your order. Enjoy your meal!")


def get_user_data():
    global num_adult_meals
    global num_child_meals
    num_adult_meals = int(input("Number of adult meals:"))
    num_child_meals = int(input("Number of child meals:"))

def perform_calculations():
    global subtotal, service_fee, sales_tax, total, subtotal_adult, subtotal_child
    subtotal_adult =(num_adult_meals * ADULT_MEAL)
    subtotal_child =( num_child_meals * CHILD_MEAL)
    subtotal = subtotal_adult + subtotal_child
    sales_tax = subtotal * SALES_TAX_RATE
    service_fee = subtotal * SERV_FEE
    total = subtotal + sales_tax + service_fee
    
def display_results():
    money = '8,.2f'
    print('--------------------------------')
    print('**** Branch Barbeque Buffet ****')
    print('**** The Best BBQ Around *****')
    print('--------------------------------')
    print('Adult Meal      $ ' + format(subtotal_adult,money))
    print('Child Meal      $ ' + format(subtotal_child,money))
    print('Sales Tax       $ ' + format(sales_tax,money))
    print('Service Fee     $ ' + format(service_fee,money))
    print('Total           $ ' + format(total,money))
    print('-----------------------------------')
    print('******* Come back soon! ***********')
    print(str(datetime.datetime.now()))


############# call on main progrm to execute ###############
main()
                
