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

outfile = 'pvccweb.html'

################  define program functions  #################
def main():

    open_outfile()
    more = True
    
    while more:
        get_user_data()
        perform_calculations()
        create_output_file()

        askAgain = input("\nWould you like to calculate tuition & fees for another student? (Y/N):")
        if askAgain.upper() == 'N':
            more = False
            print("Thank you for enrolling in PVCC. Enjoy the semester!")
            f.write('</body><html>')
            f.close()

def open_outfile():
    global f
    f = open(outfile, 'w')
    f.write('<html> <head> <title> PVCC Tuition </title>\n')
    f.write('<style> td{text-align: left} </style> </head>\n')
    f.write('<body style ="background-image: url(wp-pvcc.png)>')

def get_user_data():
    global inout, numcredits, scholarship_amt
    f.write('**** PIEDMONT VIRGINIA COMM COLLEGE Tuition & Fees ****')
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

def create__output_file():
    currency = '8,.2f'
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    tr ='<tr><td>'
    endtd = '</td><td>'
    endtr = '</td><tr>\n'
    colsp = '<tr><td colspan= "3">'
    sp = " "

    f.write('\n<table border = "3"  style = "background-color: #00ff00; font-family: monospace; margin: auto>\n')
    f.write(colsp + '\n')   
    f.write('<h2>**** PIEDMONT VIRGINIA COMM COLLEGE ****</h2></td></tr>')
    f.write('**********  Tuition and Fees Report***********')
    
    
    f.write(tr + 'Tuition' + endtd + str(tuition_amt,currency) + format(cost_tuition,currency) + endtr)
    f.write(tr + 'Institution Fee' + endtd + str(inst_fee,currency) + format(cost_inst_fee,currency) + endtr)
    f.write(tr + 'Activity Fee' + endtd + str(act_fee,currency) + format(cost_act_fee,currency) + endtr)
    f.write(tr + 'Scholarship' + endtd +  str(scholarship_amt,currency) + format(cost_scholarship) + endtr)
    f.write(tr + 'Total' + endtd + str(total, currency)+ endtr)
    f.write(tr + 'Balance' + endtd + str(balance,currency) + endtr)

    f.write(colsp + 'Date/Time: ' + day_time + endtr)
    f.write('</table><br />')




################### call on main program to execute ################
main()    
    
