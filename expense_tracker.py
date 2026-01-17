import csv
import os
from tabulate import tabulate
import matplotlib.pyplot as plt

class ExpenseTracker:
    def __init__(self, filename="expenses.csv"):
        self.filename = os.path.join(os.getcwd(), filename)
        self.expenses = []
        self.load_expenses()

    def load_expenses(self):
        try:
            with open(self.filename, "r") as file:
                reader = csv.DictReader(file)
                self.expenses = [row for row in reader]
        except FileNotFoundError:
            self.expenses = []

    def save_expenses(self):
        with open(self.filename, "w", newline="") as file:
            fieldnames = ["date", "category", "amount", "description"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.expenses)

    def add_expense_direct(self, date, category, amount, description):
        self.expenses.append({
            "date": date,
            "category": category,
            "amount": round(float(amount),2),
            "description": description
        })
        self.save_expenses()

    def show_expenses_table_detailed(self):
        if not self.expenses:
            print("No expenses to show!\n")
            return
        print("📋 Detailed Expenses Table:\n")
        print(tabulate(self.expenses, headers="keys", tablefmt="fancy_grid"), "\n")

    def show_expenses_table_summed(self):
        if not self.expenses:
            print("No expenses to show!\n")
            return
        
        categories = {}
        total_sum = 0
        for exp in self.expenses:
            cat = exp['category']
            amount = float(exp['amount'])
            categories[cat] = categories.get(cat, 0) + amount
            total_sum += amount

        summary = [{"Category": k, "Total Amount": round(v,2)} for k, v in categories.items()]
        print("📊 Summed Expenses Table (by Category):\n")
        print(tabulate(summary, headers="keys", tablefmt="fancy_grid"), "\n")
        print(f"💰 Total Expenses: {round(total_sum,2)}\n")

        if categories:
            max_cat = max(categories, key=categories.get)
            print(f"🔥 Highest spending category: {max_cat} ({round(categories[max_cat],2)})\n")

    def show_expenses_bar_graph(self):
        if not self.expenses:
            print("No expenses to show!\n")
            return
        
        categories = {}
        for exp in self.expenses:
            cat = exp['category']
            amount = float(exp['amount'])
            categories[cat] = categories.get(cat, 0) + amount

        sorted_categories = dict(sorted(categories.items(), key=lambda x: x[1], reverse=True))
        colors = ['skyblue', 'orange', 'green', 'red', 'purple', 'yellow']

        plt.figure(figsize=(8,5))
        plt.bar(sorted_categories.keys(), [round(v,2) for v in sorted_categories.values()],
                color=colors[:len(sorted_categories)])
        plt.title("💹 Expenses by Category")
        plt.xlabel("Category")
        plt.ylabel("Amount Spent")
        plt.show()


if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.expenses = []
    tracker.save_expenses()

    demo_expenses = [
        ("2026-01-15", "Food", 250, "Lunch"),
        ("2026-01-16", "Transport", 100, "Bus Fare"),
        ("2026-01-17", "Entertainment", 300, "Movie Tickets"),
        ("2026-01-18", "Shopping", 500, "Clothes"),
        ("2026-01-19", "Bills", 150, "Electricity")
    ]

    for exp in demo_expenses:
        tracker.add_expense_direct(*exp)

    tracker.show_expenses_table_detailed()
    tracker.show_expenses_table_summed()
    tracker.show_expenses_bar_graph()


