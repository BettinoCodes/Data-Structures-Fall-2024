import csv
from pprint import pprint
#WE GOT O(N+M) BOYS ILL TAKE IT

customer_data = []
transactions_list = []
customer_master = {}
discounts = []
discount_start = 0

with open("discounts.csv", mode='r') as discount_file:
    csv_reader = csv.reader(discount_file)
    for row in csv_reader:
        discounts.append(row[0])

# Open the CSV file and read the first column
with open("master.csv", mode='r') as master_file:
    csv_reader = csv.reader(master_file)
    next(csv_reader)
    for row in csv_reader:
        # customer_data.append(customer(row[0], row[1],  row[2], row[3]))
        if row[0] in customer_master:
            print(f"Error: Duplicate customer number {row[0]} in master file.")
        else:
            customer_master[row[0]] = {
                "customer number": row[0],
                "original balance": row[2],
                "name": row[1],
                "balance": row[2],
            }

customer_numbers = {}
cust_nums = []

with open("transactions.csv", mode='r') as transactions_file:
    csv_reader = csv.reader(transactions_file)
    next(csv_reader)

    for row in csv_reader:
        if row[1] not in customer_master:
            print(f'Error: {row[1]} is not in masters file')
        else:
            transactions_list.append(row)

for transaction in transactions_list:
    if transaction[1] not in cust_nums:
        cust_nums.append(transaction[1])
        customer_master[transaction[1]]["transactions"] = ""
    balance_due = float(customer_master[transaction[1]]['balance'])
    cost = 0.0
    if transaction[0] == "O":
        cost = float(transaction[4]) * float(transaction[5])
        # print(f"{str_num} bought ${cost} of {transaction[3]}")
        balance_due += cost
        customer_master[transaction[1]][
            "transactions"] += f"TRANSACTION NUMBER: {transaction[2]} | TRANSACTION ITEM:{transaction[3]} | PAYMENT AMOUNT: ${cost}\n"
    else:
        cost = round(
            float(transaction[4]) *
            (1 + (float(discounts[discount_start])) / 100), 2)
        balance_due -= cost
        discount_start += 1
        customer_master[transaction[1]]["transactions"] += (
            f"TRANSACTION NUMBER: {transaction[2]} | "
            f"TRANSACTION TYPE: {transaction[3]} | "
            f"PAYMENT AMOUNT: ${round(float(transaction[4]), 2)} | "
            f"PAYMENT W/DISCOUNT: ${cost}\n")

    customer_master[transaction[1]]['balance'] = balance_due
    # print(f"AFTER BALANCE DUE: {balance_due}")

# print(customer_numbers)
# pprint(customer_master)

print("\n")
for customer_numbers in customer_master:
    print(f"Customer Name: {customer_master[customer_numbers]['name']}")
    print(
        f"Customer Number: {customer_master[customer_numbers]['customer number']}"
    )
    print(
        f"Previous Balance: ${customer_master[customer_numbers]['original balance']}"
    )
    print(
        f"Transactions:\n{customer_master[customer_numbers]['transactions']}")
    print(f"Current Balance: {customer_master[customer_numbers]['balance']}\n")
