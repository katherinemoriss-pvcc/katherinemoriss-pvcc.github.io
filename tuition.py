# Katherine Morris
# Prog Purpose: This program computes PVCC College tuition and fees
#   PVCC Fee Rates are from: https://www.pvcc.edu/tuition-and-fees

import datetime
# define tuition & fee rates
RATE_TUITION_IN = 164.40
RATE_TUITION_OUT = 353.00
RATE_CAPITAL_FEE = 26.00
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.90

#define global variables
inout = 1
numcredits = 0
scholarship_amt = 0

tuition_amt = 0
inst_fee = 0
cap_fee = 0
act_fee = 0
total = 0
balance = 0

################  define program functions  #################
def main():

    more = True
    while more:
        get_user_data()
        perform_calculations()
        display_results()

        yesno = input("\nWould you like to calculate tuition & fees for another student? (Y/N):")
        if yesno == "n" or yesno == "N":
            more = False
            print("Thank you for enrolling in PVCC. Enjoy the semester!")

def get_user_data():
    global inout, numcredits, scholarship_amt
    print('**** PIEDMONT VIRGINIA COMM COLLEGE Tuition & Fees ****')
    inout = int(input("Enter a 1 for IN-STATE; enter a 2 for OUT-OF-STATE: "))
    numcredits = int(input("Number of credits registered for: "))
    scholarship_amt = int(input("Scholarship amount received: "))

def perform_calculations():
    global tuition, inst_fee, cap_fee, act_fee, total, balance

    if inout == 1:
        tuition = numcredits * RATE_TUITION_IN
        cap_fee = 0
    else:
        tuition = numcredits * RATE_TUITION_OUT
        cap_fee = numcredits * RATE_CAPITAL_FEE

    inst_fee = RATE_INSTITUTION_FEE * numcredits
    act_fee  = RATE_ACTIVITY_FEE  * numcredits
    total = tuition + cap_fee + inst_fee + act_fee
    balance = total - scholarship_amt

def display_results():
    currency = '8,.2f'
    line = '----------------------------------------'

    print(line)
    print('**** PIEDMONT VIRGINIA COMM COLLEGE ****')
    print('        Tuition and Fees Report         ')
    print(str(datetime.datetime.now()))
    print(line)
    print('Tuition          $ ' + format(tuition,currency))
    print('Capital Fee      $ ' + format(cap_fee,currency))
    print('Institution Fee  $ ' + format(inst_fee,currency))
    print('Activity Fee     $ ' + format(act_fee,currency))
    print('Total            $ ' + format(total,currency))
    print('Scholarship      $ ' + format(scholarship_amt,currency))
    print('Balance          $ ' + format(balance,currency))
    print(line)

################### call on main program to execute ################
main()    
    
