import csv
from pprint import pprint




# Open the CSV file and read the first column
with open("master.csv", mode='r') as master_file:
    with open("transactions.csv", mode='r') as transactions_file:
        with open("discounts.csv", mode='r') as discount_file:
            master_reader = csv.reader(master_file)
            transaction_reader = csv.reader(transactions_file)
            discounts_reader = csv.reader(discount_file)
            data_master= next(master_reader, None)
            data_discounts = next(discounts_reader, None)
            for row in transaction_reader:
                print(row)
                if row[1] == data_master[0]:
                    balance_due = float(data_master[2])
                    if row[0] == "O":
                        print("order:")
                        # balance_due += float(row[4]) * float(row[5])
                        # print(balance_due)
                        print(float(row[4]) * float(row[5]))
                    if row[0] == "P":
                        print("payment:")
                        # balance_due -= float(row[4]) * (1 +(float(next(discounts_reader)[0]))/100)
                        # print(balance_due)
                        print(float(row[4]))
                else:
                    data_master = next(master_reader)
                    print("next data lines")
                    print(data_master)
            print(data_discounts)
            print(data_master)
            print(data_transactions)





# Customer Name
# Customer Number
# Standard Discount
# Previous Balance
# transaction number		item ordered	  order amount     discounted amount
# transaction number		item ordered	  order amount     discounted amount 
# transaction number 	payment	  payment amt      discounted pmt amt
# transaction number		item ordered	  order amount      discounted amount
# Balance Due
