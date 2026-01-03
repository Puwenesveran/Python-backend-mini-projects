import argparse
from expense_manager import ExpenseManager


def main():
    manager = ExpenseManager()

    parser = argparse.ArgumentParser(prog="expense-tracker")
    sub = parser.add_subparsers(dest="command")


    add = sub.add_parser("add")
    add.add_argument("--category", required=True)
    add.add_argument("--description", required=True)
    add.add_argument("--amount", type=float, required=True)

    lst = sub.add_parser("list")

    delete = sub.add_parser("delete")
    delete.add_argument("--id", type=int, required=True)

    summary = sub.add_parser("summary")

    cat = sub.add_parser("category")

    args = parser.parse_args()

    if args.command == "add":
        eid = manager.add(args.category, args.description, args.amount)
        print(f"Expense added successfully (ID: {eid})")

    elif args.command == "list":
        print("ID  Date        Category    Description    Amount")
        for e in manager.list():
            print(f"{e.id:<3} {e.date} {e.category:<10} {e.description:<12} ${e.amount}")

    elif args.command == "delete":
        if manager.delete(args.id):
            print("Expense deleted successfully")
        else:
            print("Expense ID not found")

    elif args.command == "summary":
        total, _ = manager.summary()
        print(f"Total expenses: ${total}")

    elif args.command == "category":
        data = manager.list_by_category()
        for cat, info in data.items():
            print(f"{cat} - {info['percentage']}%")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
