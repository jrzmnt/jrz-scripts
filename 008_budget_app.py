"""
Budget App: Category and Spending Chart

This script implements a budget tracking system using the `Category` class and a `create_spend_chart` function.
The `Category` class allows users to create budget categories, track deposits and withdrawals, transfer funds
between categories, and display a formatted ledger. The `create_spend_chart` function generates a bar chart
showing the percentage of spending across multiple categories.

Classes:
    Category: Represents a budget category with methods for managing deposits, withdrawals, transfers, and
              displaying the ledger.

Methods of the Category class:
    __init__(self, name: str) -> None: Initializes a budget category with a name and an empty ledger.
    deposit(self, amount: float, description: str = "") -> None: Adds a deposit to the ledger.
    withdraw(self, amount: float, description: str = "") -> bool: Adds a withdrawal to the ledger if funds are available.
    get_balance(self) -> float: Returns the current balance of the category.
    transfer(self, amount: float, category: 'Category') -> bool: Transfers funds to another category.
    check_funds(self, amount: float) -> bool: Checks if the category has sufficient funds for a transaction.
    __str__(self) -> str: Returns a formatted string representation of the ledger.

Functions:
    create_spend_chart(categories: list[Category]) -> str: Generates a bar chart showing the percentage of spending
                                                           across categories.

Usage Example:
    food = Category("Food")
    food.deposit(1000, "deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    clothing = Category("Clothing")
    food.transfer(50, clothing)
    print(food)

    categories = [food, clothing]
    print(create_spend_chart(categories))
"""


class Category:
    def __init__(self, name: str) -> None:
        self.name = name
        self.ledger = []

    def deposit(self, amount: float, description: str = "") -> None:
        """Add a deposit to the ledger."""
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount: float, description: str = "") -> bool:
        """Add a withdrawal to the ledger if there are enough funds."""
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self) -> float:
        """Return the current balance of the budget category."""
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount: float, category: "Category") -> bool:
        """Transfer funds to another category."""
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount: float) -> bool:
        """Check if there are enough funds for a withdrawal or transfer."""
        return amount <= self.get_balance()

    def __str__(self) -> str:
        """Return a formatted string representation of the budget category."""
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            description = item["description"][:23].ljust(23)
            amount = f"{item['amount']:.2f}".rjust(7)
            items += f"{description}{amount}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories: list[Category]) -> str:
    """Create a bar chart showing the percentage spent by category."""
    # Calculate total withdrawals for each category
    withdrawals = []
    for category in categories:
        total_withdrawn = sum(
            item["amount"] for item in category.ledger if item["amount"] < 0
        )
        withdrawals.append(total_withdrawn)
    total_withdrawn = sum(withdrawals)

    # Calculate percentages (rounded down to the nearest 10)
    percentages = [int((w / total_withdrawn) * 100) // 10 * 10 for w in withdrawals]

    # Build the chart
    chart = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        chart += f"{i:3}| "
        for p in percentages:
            chart += "o  " if p >= i else "   "
        chart += "\n"
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # Add category names vertically
    max_name_length = max(len(category.name) for category in categories)
    for i in range(max_name_length):
        chart += "     "
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + "  "
            else:
                chart += "   "
        if i < max_name_length - 1:
            chart += "\n"

    return chart


# Example usage
food = Category("Food")
food.deposit(1000, "deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
print(food)

# Example of the bar chart
categories = [food, clothing]
print(create_spend_chart(categories))
