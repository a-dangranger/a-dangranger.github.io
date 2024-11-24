"""
Mortgage Calculator - Summary of Steps

1. **Import Required Libraries**:
   - Tkinter: A standard Python library for creating graphical user interfaces (GUIs).
   - Messagebox: A module within Tkinter to display message boxes.

2. **Define the Mortgage Calculation Function**:
   - Convert the annual interest rate to a monthly rate and express it as a decimal.
   - Calculate the total number of monthly payments.
   - Use the formula for an amortizing loan to calculate the monthly mortgage payment.
   - Calculate the total cost of the loan and the total interest paid over the life of the loan.
   - Handle input errors by displaying error messages using the messagebox module.

3. **Create the Main Application Window**:
   - Use Tkinter to create a window with the title "Mortgage Calculator".
   - Add labels and entry widgets for user input (loan amount, annual interest rate, and loan term).
   - Add a button that triggers the mortgage calculation function when clicked.

4. **Run the Application**:
   - Use Tkinter's main loop to run the application and keep the window open.

5. **Creating an Executable**:
   - Use PyInstaller to package the Python script into a standalone executable file.
   - PyInstaller bundles the Python interpreter and all necessary dependencies, including Tkinter, into the executable file.
   - Command: `pyinstaller --onefile --windowed your_script_name.py` (replace `your_script_name.py` with the name of your Python script file).

The resulting executable will work on any Windows PC without needing to install Python or Tkinter.
"""

import tkinter as tk
from tkinter import messagebox

# Function to calculate the mortgage details
def calculate_mortgage():
    try:
        # Get user input from the entry widgets and convert to appropriate types
        loan_amount = float(entry_loan.get())
        annual_interest_rate = float(entry_rate.get())
        loan_term_years = int(entry_term.get())

        # Convert annual interest rate to a monthly rate and express as a decimal
        monthly_interest_rate = annual_interest_rate / 100 / 12

        # Calculate the total number of monthly payments
        total_payments = loan_term_years * 12

        # Calculate the monthly mortgage payment using the formula for an amortizing loan
        monthly_payment = loan_amount * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -total_payments)

        # Calculate the total cost of the loan over its lifetime
        total_cost = monthly_payment * total_payments

        # Calculate the total interest paid over the life of the loan
        total_interest = total_cost - loan_amount

        # Prepare the result text with formatted numbers
        result_text = (f"Monthly Mortgage Payment: ${monthly_payment:,.2f}\n"
                       f"Total Interest Paid: ${total_interest:,.2f}\n"
                       f"Total Cost of the Loan: ${total_cost:,.2f}")

        # Display the result in a message box
        messagebox.showinfo("Mortgage Calculation", result_text)
    except ValueError:
        # Display an error message if the user input is not valid
        messagebox.showerror("Input Error", "Please enter valid numbers for all fields.")

# Create the main application window
root = tk.Tk()
root.title("Mortgage Calculator")

# Create and place labels and entry widgets for user input
tk.Label(root, text="Loan Amount:").grid(row=0, column=0, padx=10, pady=5)
entry_loan = tk.Entry(root)
entry_loan.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Annual Interest Rate (%):").grid(row=1, column=0, padx=10, pady=5)
entry_rate = tk.Entry(root)
entry_rate.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Loan Term (years):").grid(row=2, column=0, padx=10, pady=5)
entry_term = tk.Entry(root)
entry_term.grid(row=2, column=1, padx=10, pady=5)

# Create and place a button to trigger the calculation
tk.Button(root, text="Calculate", command=calculate_mortgage).grid(row=3, columnspan=2, pady=10)

# Run the application
root.mainloop()
