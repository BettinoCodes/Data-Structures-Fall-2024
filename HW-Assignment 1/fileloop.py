import csv
import pandas as pd
from pprint import pprint



# Open the CSV file and read the first column
with open("master.csv", mode='r+') as master_file:
    with open("transactions.csv", mode='r') as transactions_file:
        with open("discounts.csv", mode='r') as discount_file:
            csv_file = 'master.csv'
            df = pd.read_csv(csv_file, header=None)  # header=None if no headers in the CSV

            master_reader = csv.reader(master_file)
            transaction_reader = csv.reader(transactions_file)
            discounts_reader = csv.reader(discount_file)
            data_master= next(master_reader, None)
            print(f"first:{data_master}")
            print(f"start dis: {discounts_reader}")
            # data_discounts = next(discounts_reader, None)
            # print(data_discounts)
            row_number = 0
            # company_name = 
            # company_balance = 
            # company_number = 
            for row in transaction_reader:
                print(row)
                if row[1] == data_master[0]:
                    balance_due = float(data_master[2])
                    if row[0] == "O":
                        print("order:")
                        balance_due += float(row[4]) * float(row[5])
                        data_master[2] = str(balance_due)
                        csv.DictWriter
                        print(data_master[2])
                    if row[0] == "P":
                        print("payment:")
                        amount = float(row[4])
                        discount_per = (1 +(float(next(discounts_reader, None)[0]))/100)
                        print(f"AM: {amount}")
                        print(f"DIS: {discount_per}")
                        balance_due -= float(row[4]) * discount_per
                        print(f"BAL DISC: {balance_due}")
                        data_master[2] = str(balance_due)
                        print(data_master[2])
                else:
                    print(f"{data_master[1]} owes {data_master[2]}")
                    data_master = next(master_reader, None)
                    row_number += 1
                    print("next data lines")
                    print(data_master)
            # print(data_discounts)
            print(data_master)


# 1001,ABC Corporation,1200
# 1002,XYZ Enterprises,2500
# 1003,Delta Solutions,3100
# 1004,Echo Technologies,800
# 1005,Foxtrot Industries,4000
# 1006,Gamma Ltd.,2200
# 1007,Bravo Corp.,1500
# 1001,ABC Corporation,1200



# Customer Name
# Customer Number
# Standard Discount
# Previous Balance
# transaction number		item ordered	  order amount     discounted amount
# transaction number		item ordered	  order amount     discounted amount 
# transaction number 	payment	  payment amt      discounted pmt amt
# transaction number		item ordered	  order amount      discounted amount
# Balance Due
