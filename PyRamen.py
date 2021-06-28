# -*- coding: UTF-8 -*-
"""PyRamen Homework Starter."""

# @TODO: Import libraries
import csv
from pathlib import Path

# @TODO: Set file paths for menu_data.csv and sales_data.csv
menu_filepath = Path('Resources/menu_data.csv')
sales_filepath = Path('Resources/sales_data.csv')

# @TODO: Initialize list objects to hold our menu and sales data
menu = []
sales = []

# @TODO: Read in the menu data into the menu list
with open(menu_filepath, newline="") as menudata:
    csvreader = csv.reader(menudata, delimiter=",")
    csvheader = next(csvreader)

    for x in csvreader:
        menu.append(x)









# @TODO: Read in the sales data into the sales list
with open(sales_filepath, newline="") as salesdata:
    csvreader_sales = csv.reader(salesdata, delimiter=",")
    csvheader_sales = next(csvreader_sales)

    for x in csvreader_sales:
        sales.append(x)









# @TODO: Initialize dict object to hold our key-value pairs of items and metrics
report = {}

# Initialize a row counter variable
row_count = 0

# @TODO: Loop over every row in the sales list object
for x in sales:



    # Line_Item_ID,Date,Credit_Card_Number,Quantity,Menu_Item
    # @TODO: Initialize sales data variables
    Quantity = int(x[3])
    Menu_Item = x[4]

    # @TODO:
    # If the item value not in the report, add it as a new entry with initialized metrics
    # Naming convention allows the keys to be ordered in logical fashion, count, revenue, cost, profit
    if Menu_Item not in report.keys():
        report[Menu_Item] = {"01-count": 0, "02-revenue": 0, "03-cogs": 0, "04-profit": 0}

    








    # @TODO: For every row in our sales data, loop over the menu records to determine a match
    for row in menu:

        

        


        # Item,Category,Description,Price,Cost
        # @TODO: Initialize menu data variables
        Item = row[0]
        Price = float(row[3])
        Cost = int(row[4])




        # @TODO: Calculate profit of each item in the menu data
        Profit = Price - Cost


        # @TODO: If the item value in our sales data is equal to the any of the items in the menu, then begin tracking metrics for that item
        if Menu_Item == Item:
            report[Menu_Item]["01-count"] += Quantity
            report[Menu_Item]["02-revenue"] += Price * Quantity
            report[Menu_Item]["03-cogs"] += Cost * Quantity
            report[Menu_Item]["04-profit"] += Profit * Quantity

            


        # @TODO: Else, the sales item does not equal any fo the item in the menu data, therefore no match
        



    # @TODO: Increment the row counter by 1
    


# @TODO: Print total number of records in sales data





# @TODO: Write out report to a text file (won't appear on the command line output)

