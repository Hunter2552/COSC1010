#
# Hunter Richardson
# 9/23/2024
# Budget Analysis Programming Project
# COSC 2409 DNT
#
# Use comments liberally throughout the program. 

def main():
    # Ask for budgeted amount
    budget = float(input("Enter the budget amount for this month: $"))
    
    # Total expenses
    total_expenses = 0.0
    
    # The Loop Function
    while True:
        expense = input("Enter expense (or 'n/a' to finish): $")
        if expense.lower() == 'n/a':
            break
        total_expenses += float(expense)
    
    # Calculate difference between budget - total expenses
    difference = budget - total_expenses
    
    # Results
    if difference > 0:
        print(f"You are under by ${difference:.2f}")
    elif difference < 0:
        print(f"You are over by ${-difference:.2f}")
    else:
        print("You are exactly on budget.")

# Main function
if __name__ == "__main__":
    main()