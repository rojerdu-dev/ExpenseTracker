import calendar
import datetime

from expense import Expense


# First Func
def get_user_expense():
    print("🎯 Getting User Expense")
    expense_name = input("Enter expense name: ")
    expense_amount = float(input("Enter expense amount: $"))
    print(f"You've entered {expense_name}: ${expense_amount:.2f}")

    expense_categories = ["🍜 Food", "🏠 Home", "💻 Work", "🕺 Fun", "✨ Misc"]

    while True:
        print("Select a category: ")
        for i, ele in enumerate(expense_categories, start=1):
            print(f"  {i}. {ele}")

        value_range = f"(1 - {len(expense_categories)})"
        selected_index = int(input(f"Enter a category number {value_range}: ")) - 1

        if selected_index in range(0, len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(
                name=expense_name, category=selected_category, amount=expense_amount
            )
            return new_expense
        else:
            print("Invalid Category. \nPlease Try Again!")


# Second Func
def save_expense_to_file(expense: Expense, expense_file_path):
    print(f"🎯 Saving User Expense Expense: {expense} to {expense_file_path}")
    with open(expense_file_path, "a") as f:
        f.write(f"{expense.name}, {expense.category}, {expense.amount}\n")


# Third Func
def summarize_expense(expense_file_path, budget):
    print("🎯 Summarizing User Expense")
    expenses: list[Expense] = []
    with open(expense_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            expense_name, expense_category, expense_amount = line.strip().split(",")
            line_expense = Expense(
                name=expense_name,
                amount=float(expense_amount),
                category=expense_category,
            )
            expenses.append(line_expense)

        amount_by_category: dict = {}
        for expense in expenses:
            key = expense.category
            if key in amount_by_category:
                amount_by_category[key] += expense.amount
            else:
                amount_by_category[key] = expense.amount

        print("Expenses By Category 📈:")
        for key, amount in amount_by_category.items():
            print(f"  {key}: ${amount:.2f}")

        total_spent = sum([x.amount for x in expenses])
        print(f"💸 Total Spent: ${total_spent:.2f}")

        remaining_budget = budget - total_spent
        print(f"💸 Budget Remaining: ${remaining_budget:.2f}")

        # Get current date
        now = datetime.datetime.now()

        # Get number of days in current month
        days_in_month = calendar.monthrange(now.year, now.month)[1]

        # Calc remaining number of days in current month
        remaining_days = days_in_month - now.day

        print(f"📅 Remaining days in current month: {remaining_days}")

        daily_budget = remaining_budget / remaining_days
        print(green(f"👉 Budget Per Day: ${daily_budget:.2f}"))


# Green Func -> Turn Text Green
def green(text):
    return f"\033[92m{text}\033[0m"


# Main Func
def main():
    print("🎯 Running Expense Tracker")
    name = input("Hello friend! What's your name? ")
    budget = float(
        input(
            f"Hey there, {name}! \
        \nWhat's your monthly budget in dollars? \
        \nFor example, enter 5000 if your budget is $5000. \
        \n$"
        )
    )

    expense_file_path = "expenses.csv"

    # Get User Input For Expense
    expense = get_user_expense()

    # Write Expense to File
    save_expense_to_file(expense, expense_file_path)

    # Read File & Summarize Expenses
    summarize_expense(expense_file_path, budget)


if __name__ == "__main__":
    main()
