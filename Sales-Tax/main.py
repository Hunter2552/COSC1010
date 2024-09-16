
# Hunter Richardson
# Date
# Sales Tax Programming Project
# COSC 2409 DNT
# Variable declarations
# Constants for the state and county tax rates
# Get the amount of the purchase.
# Calculate the state sales tax.
# Calculate the county sales tax.
# Calculate the total tax.
# Calculate the total of the sale.
# Print information about the sale.

Total_amount=float(input('Enter Total: $'))

State_Tax_=0.05
County_Tax= 0.025

Total_state_tax=Total_amount*State_Tax_
Total_County_tax=Total_amount*County_Tax

Total_Tax=Total_state_tax+Total_County_tax

Final_Amount=Total_Tax+Total_amount

print(f"Total Amount: ${Total_amount:.2f}")
print(f"State Tax: ${State_Tax_:.2f}")
print(f"County Tax: ${County_Tax:.2f}")
print(f"Total Sales Tax: ${Total_Tax:.2f}")
print(f"Final Amount: ${Final_Amount:.2f}")