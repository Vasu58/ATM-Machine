'''Create an ATM Machine Simulation:

Your program should simulate the basic functions of an ATM machine.
functions to include:
1)Account balance inquiry
2)Cash withdrawal
3)Cash deposit
4)PIN change
5)Transaction history'''
import time 
#Reading the card
print("====================PLEASE INSERT YOUR ATM CARD====================")
time.sleep(3)
#Here sleep()method is used to suspend the execution of a program for the given number of seconds
Actual_Pin="6255"
current_Balance=10000
Entered_pin=input("enter your ATM pin number(4 Digit Pin):")
if(Entered_pin==Actual_Pin):
    user_id=int(input("Enter your user_id:"))
    print(f"====================WELCOME {user_id} ====================") 
    print("""
    1 == Balance Amount
    2 == Withdraw
    3 == Deposit
    4 == Transfer
    5 == Pin change
    6 == Exit
    """)
    try:
        option=int(input("Please enter your choice:"))
    except ValueError:
        print("====================Please Enter valid option====================")
    if(option==1):
        print(f"Your current Balance is {current_Balance}")
    elif(option==2):
        withdraw_amount=int(input("Please Enter your withdraw amount:"))
        if(withdraw_amount>current_Balance):
            print("Insufficient funds")
        else:
            current_Balance=((current_Balance)-(withdraw_amount))
            print(f"{withdraw_amount} is Debited from your account")
            print(f"Your current balance is {current_Balance}")
    elif(option==3):
        Deposit_amount=int(input("Please Enter your deposit amount:"))
        current_Balance=((current_Balance)+(Deposit_amount))
        print(f"{Deposit_amount} is creadited from your account")
        print(f"your current balance is {current_Balance} ")
    if(option==4):
        Transfer_Account_number=int(input("Enter the account number you want to Transfer:"))
        Transfer_Amount=int(input("Enter amount you want to transefer:"))
        if(withdraw_amount>current_Balance):
            print("Insufficient funds")
        else:
            current_Balance=current_Balance-Transfer_Amount
            print(f"transfer {Transfer_Amount} rupees to {Transfer_Account_number} and remaining balance is {current_Balance}") 
    elif(option==5):
        print("====================WELCOME TO THE ATM PIN CHANGE ====================")
        #verify current pin
        if(Entered_pin==Actual_Pin):
            new_pin=input("Please enter your new PIN(4-Digit PIN):")
            #validate new PIN format
            if(len(new_pin)==4):
                confirm_new_pin=input("Please confirm your new PIN:")
                #confirm new PIN
                if confirm_new_pin==new_pin:
                    Actual_Pin==new_pin
                    print(f"Your PIN has been successfully changed. The new_pin is {new_pin}")
                else:
                    print("PINs do not match. PIN change unsuccessful.")
            else:
                print("Invalid PIN format. PIN must be exactly 4 digits")                  
    elif(option==6):
        print("==================== THANK YOU ====================")
else:
    print("**************************************************************")
    print("---------------INCORRECT PIN PLEASE TRY AGAIN---------------")
    print("**************************************************************")
