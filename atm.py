balance = 10000
print("Welcome to ATM")
pin = input("Enter PIN :")
if pin == "1234":
    print("\n 1. balance")
    print("2. Deposit")
    print("3.Withdraw")
    choice = int(input("Enter the Choice:"))
    if choice == 1:
        print(f"Balance: {balance}")
    elif choice == 2:
        amount = float(input("Deposit Amount:"))
        balance += amount
        print("Updated Balance =",balance)
    elif choice == 3:
        amount = float(input("Withdraw Amount:"))
        if amount<=balance :
            balance -= amount
            print("Updated Balance =",balance) 
        else  :
            print ("insuffient balance")
            
        
