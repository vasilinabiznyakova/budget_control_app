import sys

"""
Tech Task: Weekly Budget Control App

Objective:
Develop an application to help users control their weekly budget.

Requirements:
1. At the beginning of the week, prompt the user to enter their total weekly budget (positive number, in dollars). +
2. At the end of each day (7 days in total):
    - Prompt the user to input their daily expenses.
    - If the user enters an invalid input (non-numeric or empty), assume default daily expenses of 100$.
    - After entering daily expenses, show the user:
        - Total spent so far.
        - Remaining budget (weekly budget - total expenses).
3. At the end of the week (after 7 inputs):
    - Notify the user whether they stayed within the budget or exceeded it.
    - If exceeded, show by how much.
4. Validate user inputs where possible:
    - Expenses should be non-negative numbers (integers or floats with up to 2 decimal points).
5. No interruption if budget is exceeded during the week — just notify at the end.

Assumptions:
- No need for persistent data storage — the app works for a single session.
- User must interact via console/terminal.

"""


def validate_amount(number, is_weekly_budget, day_name=None):
    default_day_expenses = 100
    try:
        number = int(number)
    except ValueError:
        print(f'❌ You entered "{number}", it is not a number!\nPlease, try again!')
        sys.exit(1)

    if is_weekly_budget:
        if number <= 0:
            if number == 0:
                print("💸 You have $0 to spend, you should try to find a job!")
            else:
                print("❌ Your amount is negative, please try again!")
            sys.exit(1)
        else:
            print(
                f"Your budget for this week is ${number}. Not bad!\nLet the game begin...🤡"
            )
    else:
        if number < 0:
            print(
                f"❌ Expenses cannot be negative. Setting default expenses = {default_day_expenses}."
            )
            number = default_day_expenses
        print(f"Your daily expenses for {day_name} are ${number}")

    return number


weekly_budget = input(
    "Please enter your total weekly budget (positive number, in dollars):\n"
)
weekly_budget = validate_amount(weekly_budget, True)

day_name = "Monday"
daily_expenses = input(
    f"Please enter your daily expenses for {day_name} (positive number, in dollars):\n"
)
daily_expenses = validate_amount(daily_expenses, False, day_name)
