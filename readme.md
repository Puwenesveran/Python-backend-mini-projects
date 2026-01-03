# Expense Tracker (Python Console Application)

A simple expense tracker built in Python to manage daily expenses.
Supports adding, deleting, listing expenses and viewing summaries.
Data is persisted using a JSON file.

## Features
- track your expense 
- Supports common function types (add, list, summary, delete, category)
- Prints output to console


## Tech Stack
- Python

## Setup

```bash
git clone https://github.com/puwenesveran/expense_tracker_project.git
cd expense_tracker_project
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

cli commands example:

expense-tracker add --category Food --description "Lunch" --amount 120
expense-tracker list
expense-tracker summary
expense-tracker summary --month 1
expense-tracker delete --id 2

1. Add Expense
2. List Expenses
3. Delete Expense
4. Total Summary
5. Category Summary
6. Exit