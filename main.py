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
        number = float(number)
    except ValueError:
        print(f"❌ You entered '{number}', it is not a number!\nPlease, try again!")
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
                f"Your budget for this week is ${number:.2f}. Not bad!\nLet the game begin...🤡"
            )
    else:
        if number < 0:
            print(
                f"❌ Expenses cannot be negative. Setting default expenses = {default_day_expenses}."
            )
            number = default_day_expenses
        print(f"Your daily expenses for {day_name} are ${number:.2f}")

    return number


weekly_budget = input(
    "Please enter your total weekly budget (positive number, in dollars):\n"
)
total_expenses = 0

weekly_budget = validate_amount(weekly_budget, True)

days_of_week = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
)

for day in days_of_week:
    daily_expenses = input(
        f"Please enter your daily expenses for {day} (positive number, in dollars):\n"
    )
    daily_expenses = validate_amount(daily_expenses, False, day)
    total_expenses += daily_expenses
    weekly_budget -= daily_expenses
    if weekly_budget > 0:
        print(f"💵 By the end of {day} you have ${weekly_budget:.2f} left!")
    elif weekly_budget == 0:
        print(
            f"💸 By the end of {day} you have ${weekly_budget:.2f} left! Now you need to save"
        )
    else:
        print(f"🚫 You are completely out of budget, don't buy anything else")

# Final report
print(f"\n✅ End of the week summary!")
print(f"\nTotal spent:{total_expenses:.2f}")
print(f"Total left:{weekly_budget:.2f}")

if weekly_budget < 0:
    print(f"❌ You have overspent by ${abs(weekly_budget):.2f}")
else:
    print(f"✅ Congratulations! You saved ${weekly_budget:.2f} this week!")

print("\nThanks for using the Budget App 🤡💸")
