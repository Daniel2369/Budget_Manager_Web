# Modules
from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__) # constractor
app.secret_key = "supersecretkey" # Needed for flash messages

# Storage data lists
incomes: list = [
    {"amount": 1000, "description": "Salary"},
    {"amount": 200, "description": "Freelance work"}
]

expenses: list = [
    {"amount": 500, "description": "Rent"},
    {"amount": 100, "description": "Utilities"}
]


@app.route("/") # define the main page
def index(): # main index func
    balance: int = 0 # Initialize balance

    for income in incomes:
        balance += income["amount"]

    for expense in expenses:
        balance -= expense["amount"]

    return render_template("index.html", incomes=incomes, expenses=expenses, balance=balance)


@app.route("/add_income", methods=["POST"]) # define
def add_income(): # add_income func
    global incomes, expenses
    description = request.form.get("description") # get the description passed from the user
    amount = request.form.get("amount") # get the amount passed from the user

    if not description or not amount: # validate if one is missing
        flash("Please provide both a description an an amount!", "error") # error msg
        return redirect(url_for("index")) # redirct to the home page
        
    try:
        amount = float(amount)
        if amount <= 0: # Check if amount is a positive number and > 0
            flash("Amount must be a positive number!", "error")
            return redirect(url_for("index"))
        
        new_income:dict = { # Initilize new_income dict
            "amount": amount,
            "description": description
        }

        incomes.append(new_income) # append the new dict to the incomes list
        flash("Income added successfully!", "success")
    except ValueError:
        flash("Invalid amount! Please enter a valid number.", "error")

    return redirect(url_for("index"))


@app.route("/add_expense", methods=["POST"])
def add_expense():
    global incomes, expenses
    description = request.form.get("description") # get the description passed from the user
    amount = request.form.get("amount") # get the amount passed from the user

    if not description or not amount:
        flash("Please provide both a description and an amount!", "error")
        return redirect(url_for("index"))
    
    try:
        amount = float(amount)
        if amount <= 0:
            flash("Amount must be a positive number!", "error")
            return redirect(url_for("index"))
        
        new_expense:dict = { # Initilize new_expense dict
            "amount": amount,
            "description": description
        }
        expenses.append(new_expense) # append the new dict to the expenses list
        flash("Expense added successfully!", "success")

    except ValueError:
        flash("Invalid amount! Please enter a valid number.", "error")

    return redirect(url_for("index"))
