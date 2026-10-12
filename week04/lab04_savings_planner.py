def main():
    
    while True:
        try:
            starting_balance = float(input("Enter starting balance: "))
            if starting_balance >= 0:
                break
            print("Starting balance cannot be negative.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

   
    while True:
        try:
            deposit = float(input("Enter monthly deposit: "))
            if deposit > 0:
                break
            print("Monthly deposit must be positive.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    
    while True:
        try:
            rate = float(input("Enter monthly interest rate (%): "))
            if rate >= 0:
                break
            print("Monthly interest rate cannot be negative.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

  
    while True:
        try:
            goal = float(input("Enter savings goal: "))
            if goal > 0:
                break
            print("Savings goal must be positive.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    balance = starting_balance
    total_interest = 0.0
    months = 0

   
    if balance >= goal:
        print("\nStarting balance already meets or exceeds the savings goal!")
    else:
        print("\nMonth    | Interest     | Balance")
        print("-" * 35)

       
        month = 1
        goal_reached = False

        while month <= 60:
            interest = balance * rate / 100
            balance += interest
            total_interest += interest
            
            balance += deposit
            
            print(f"{month:<8} | {interest:<12.2f} | {balance:<12.2f}")
            
           
            if balance >= goal:
                months = month
                goal_reached = True
                break
            
            month += 1

        if not goal_reached:
            months = 60

        print("-" * 35)
        if balance >= goal:
            print(f"Goal reached in {months} months!")
        else:
            print("Goal not reached after 60 months.")

    
    print(f"Final Balance: {balance:.2f}")
    print(f"Total Interest Earned: {total_interest:.2f}")

if __name__ == "__main__":
    main()
    
