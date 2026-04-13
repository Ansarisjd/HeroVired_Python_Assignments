  
def atm_withdrawal(withdrwal_amount):
    currentBalance = 5000   
    if withdrwal_amount < 0:
       print("Invalid amount. Please enter a positive amount.")
       return False
    
    if withdrwal_amount % 500 != 0:
       print("Invalid amount. Please enter a multiple of 500.")
       return False
    if withdrwal_amount > currentBalance:
       print("Insufficient balance. Please enter amount less than or equal to your current balance.")
       return False 

    currentBalance -= withdrwal_amount
    print(f"You have withdrwan amount {withdrwal_amount} successfully. \n Your current balance is:{currentBalance} \n Thank you for using our ATM service." )
    return True 

amount = int(input("Enter the amount you want to withdrawn"))
result = atm_withdrawal(amount)
print("Return:" , result)