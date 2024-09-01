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
        customer_data.append(customer(row[0], row[1],  row[2], row[3]))
        customer_master[row[0]] = {
            "name": row[1],
            "balance": row[2],
            "discount": row[3]
        }

pprint(customer_master)

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

# print(transactions_dictionary)

