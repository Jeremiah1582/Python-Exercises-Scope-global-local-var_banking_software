**Exercise: Savings Account Balance**
<!-- aim: 
to improve the students understanding of scope through global and local variables  
-->

# Backstory:
Imagine you're developing a software system for a bank. One of the functionalities needed is to manage the balance of a savings account. The bank has a policy that all newly created accounts start with a balance of $100 as an incentive for new customers.

# Objective:
Write a Python program that allows the user to:

- Check the balance of their account.
- Deposit money.
- Withdraw money.
- Exit the program.
- The program should update and remember the account balance after each transaction. Utilize local and global variables to manage and differentiate the scope of variables.

# Task:

1. Define a global variable account_balance with an initial value of 100.
2. Create a function check_balance() to print the current account balance.
3. Create a function deposit(amount) to add a certain amount to the account_balance.
4. Create a function withdraw(amount) to deduct a certain amount from the account_balance, but don't allow withdrawals that exceed the current balance.
5. In the main body of your program, use a loop to display a menu for the user to select an action (check balance, deposit, withdraw, exit).
6. Execute the corresponding function based on the user's choice.

# Hints:
- Use *global keyword* in functions to indicate the usage of the global account_balance variable.
- Utilize *local variables* inside the functions for user-defined amounts and other temporary data.