<<<<<<< HEAD
while True:
    
    try:
        
        print("Welcome to The Tip Calculator!")
        
        def calcTotalBill(bill_amount, tip_percentage):
            tip = (bill_amount * (tip_percentage / 100))
            total = tip + bill_amount
            return total

    
        bill_amount = int(input("What's your bill? \n> "))
        tip_percentage = int(input("Enter tip: 5%, 10%, 25%, custom(not less than 5%).\n> "))
            
        totalbill = calcTotalBill(bill_amount, tip_percentage)
        print(f"Your total bill is {totalbill}.")
        
        
        
        
    except ValueError:
        print("Oops! Thats not a valid number.")
        
    print("Do you want to perform another calculation (yes/no)?") 
    if not input("> ").lower().startswith("y"):
        break

print("Goodbye!")
    
    
    

=======
while True:
    
    try:
        
        print("Welcome to The Tip Calculator!")
        
        def calcTotalBill(bill_amount, tip_percentage):
            tip = (bill_amount * (tip_percentage / 100))
            total = tip + bill_amount
            return total

    
        bill_amount = int(input("What's your bill? \n> "))
        tip_percentage = int(input("Enter tip: 5%, 10%, 25%, custom(not less than 5%).\n> "))
            
        totalbill = calcTotalBill(bill_amount, tip_percentage)
        print(f"Your total bill is {totalbill}.")
        
        
        
        
    except ValueError:
        print("Oops! Thats not a valid number.")
        
    print("Do you want to perform another calculation (yes/no)?") 
    if not input("> ").lower().startswith("y"):
        break

print("Goodbye!")
    
    
    

>>>>>>> bf8013e071c541f11e82095432aa98a05bae22cc
    