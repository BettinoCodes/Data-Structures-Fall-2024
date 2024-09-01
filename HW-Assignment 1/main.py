import csv
from customer import customer
from pprint import pprint



customer_data = []
customer_numbers = []
transactions_history = []
transactions_dictionary = {}
customer_master = {}



# Open the CSV file and read the first column
with open("master.csv", mode='r') as master_file:
    csv_reader = csv.reader(master_file)
    next(csv_reader)
    for row in csv_reader:
        # customer_data.append(customer(row[0], row[1],  row[2], row[3]))
        customer_master[row[0]] = {
            "name": row[1],
            "balance": row[2],
            "discount": row[3]
        }

# pprint(customer_master)

# for cus in customer_data:
#     print(cus)

# Print the values from the first column
# for value in customer_numbers:
#     print(value)

print("------------transactions-------------\n")
with open("transactions.csv", mode='r') as transactions_file:
    csv_reader = csv.reader(transactions_file)
    next(csv_reader)

    for row in csv_reader:
        if row[1] not in transactions_dictionary:
            transactions_dictionary[row[1]] = [row]
        else:
            transactions_dictionary[row[1]].append(row)

# for transactions in transactions_history:
#     print(transactions)

# pprint(transactions_dictionary)

all_customer_data = {}
for cust_nums in customer_master:
    str_num = f'{cust_nums}'
    balance_due = round(float(customer_master[str_num]['balance']), 2)
    print(f'Customer Number {str_num} has a balance of {balance_due}')
    print(f"{str_num} list of transactions are:")
    all_customer_data[str_num] = {
        "name": cust_nums,
        "previous balance": balance_due,
        "discount": customer_master[str_num]['discount'],
        "customer number": str_num,
        "transactions": [],
        "current balance": 0
    }
    for transaction in transactions_dictionary[str_num]:
        cost = 0.0
        if transaction[0] == "O":
            try:
                cost = float(transaction[4]) * float(transaction[5]) * (1 - (float(customer_master[str_num]['discount'])/100))
            except ValueError:
                cost = float(transaction[4]) * float(transaction[5]) * 1
            try:
                cost = cost * (1 - (float(transaction[6])/100))
            except ValueError:
                cost = cost * 1
            print(f"{str_num} bought ${cost} of {transaction[3]}")
            balance_due += cost
            transaction_info = [transaction[2], transaction[3], cost, round(float(transaction[4]) * float(transaction[5]) - cost, 2), 'O']
        else:
            print(f"{str_num} made a payment of ${float(transaction[4])}") 
            try:
                cost = round(float(transaction[4]) * (1 + (float(transaction[6])/100)), 2)
                # balance_due -= float(transaction[4])
            except ValueError:
                cost = float(transaction[4])
            balance_due -= cost
            transaction_info = [transaction[2], transaction[3], cost, "P"]
        all_customer_data[str_num]["transactions"].append(transaction_info)
        all_customer_data[str_num]["current balance"] = balance_due
        

pprint(all_customer_data["1001"]['transactions'])

for customer_numbers in all_customer_data:
    print(f"Customer Name: {customer_master[customer_numbers]['name']}")
    print(f"Customer Number: {all_customer_data[customer_numbers]["customer number"]}")
    print(f"Standard Discount: {all_customer_data[customer_numbers]["discount"]}%")
    print(f"Previous Balance: ${all_customer_data[customer_numbers]["previous balance"]}")
    for transaction in all_customer_data[customer_numbers]['transactions']:
        if transaction[-1] == 'O':
            print(f"{transaction[0]}  {transaction[1]}  "
                    f"${transaction[2]}  ${transaction[3]}")
        elif transaction[-1] == 'P':
            print(f"{transaction[0]}  Payment  {transaction[1]}  "
                    f"${transaction[2]}")
    print(f"Balance Due: ${all_customer_data[customer_numbers]["current balance"]}")
    print("\n")
#     # print(f"{str_num} owes ${balance_due}")

    # print("\n")


# transaction number		item ordered	  order amount     discounted amount
# transaction number		item ordered	  order amount     discounted amount 
# transaction number 	payment	  payment amt      discounted pmt amt
# transaction number		item ordered	  order amount      discounted amount


