# Katherine Morris
# Prog Purpose: This program finds the cost of a meal at Palermo Pizza.

import datetime

################ define global variables #################

# Prices
PRICE_SMALL = 9.99
PRICE_MED = 12.99
PRICE_LRG = 17.99
PRICE_XL = 21.99
PRICE_BREAD = 6.99
PRICE_DRINK = 3.99
SALES_TAX_RATE = .055

# define global variables
num_pizzas = 0
num_drinks = 0
num_breadsticks = 0
cost_pizzas = 0
cost_drinks = 0
cost_breadsticks = 0
subtotal = 0
sales_tax_rate = 0
total = 0

############### define program functions ################
def main():

    more = True

    while more:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input("\nWould you like to order again (Y or N)?")
        if yesno.upper() == "N":
                more = False
                print("Thank you for your order. Enjoy your pizza!")

def get_user_data():
    global pizza_size, num_pizzas, num_drinks, num_breadsticks

    print('**** Palermo Pizza ****')
    print('S Small Pizza    $ 9.99')
    print('M Medium Pizza   $12.99')
    print('L Large Pizza    $17.99')
    print('X Large Pizza    $21.99')

    pizza_size = input('\nWhat size pizza would you like to order?(S, M, L, XL):')
    pizza_size = pizza_size.upper()

    num_pizzas = int(input("Number of pizzas: "))
    num_drinks = int(input("Number of drinks: "))
    num_breadsticks = int(input("Number of breadstick orders: "))

def perform_calculations():
    global cost_pizzas, cost_drinks, cost_breadsticks, subtotal, sales_tax, total

    if pizza_size == "S":
        cost_pizzas = num_pizzas * PRICE_SMALL
    elif pizza_size == "M":
        cost_pizzas = num_pizzas * PRICE_MED
    elif pizza_size == "L":
        cost_pizzas = num_pizzas * PRICE_LRG
    elif pizza_size == "XL":
        cost_pizzas = num_pizzas * PRICE_XL

    cost_breadsticks = num_breadsticks * PRICE_BREAD
    cost_drinks = num_drinks * PRICE_DRINK
    subtotal = cost_pizzas + cost_breadsticks + cost_drinks
    sales_tax = subtotal * SALES_TAX_RATE
    total = sales_tax + subtotal

def display_results():
    currency = '8,.2f'
    line = '----------------------'
    full_date = str(datetime.datetime.now())
    short_date = full_date[0:16]

    print(line)
    print('***** Palermo Pizza *****')
    print(short_date)
    print(line)
    print('Number of pizzas ordered:' + str(num_pizzas))

    print(line)
    print('Pizzas       $ ' + format(cost_pizzas,currency))
    print('Drinks       $ ' + format(cost_drinks,currency))
    print('Breadsticks  $ ' + format(cost_breadsticks,currency))
    print('Sales Tax    $ ' + format(sales_tax,currency))
    print('Total        $ ' + format(total,currency))
    print(line)
    print("*** Enjoy your pizza! ***")
    print(line)

############### call on main program to execute #################
main()


        


        
    
    


