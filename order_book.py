##### Generating dummy orders #####

import random

# create a list with 30 names of the instruments
stock_names = ["POLY", "BRBY", "FRES", "AHT", "IAG", "DCC", "LLOY", "VOD", 
               "BARC", "RJ13", "BT", "SPA", "III", "3IN", "4BB", "DDDD", 
               "4GBL", "FOUR", "SIXH", "7DIG", "88E", "888", "ABDP", "ABI", 
               "ABC", "ADIG", "ASLI", "AJIT", "ABD", "ANII"]

# create a list containing all the orders
# we store the buy orders first, then use 'extend' method to add sell orders
orders_lst = []
random.seed(123)
for i in range(1,501):
    x = random.choice(stock_names)
    n = random.randint(1, 101)
    p = random.randint(30, 101)
    orders_lst.append({"order_id" : i,
                       "stock_name" : x,
                       "quantity" : n,
                       "price" : p,
                       "order_side" : "BUY",
                       "order_status" : "None" # 3 levels: None, partially, fully
                      })
    
sell_orders_lst = []
random.seed(456)
for i in range(1,501):
    x = random.choice(stock_names)
    n = random.randint(1, 101)
    p = random.randint(1, 50)
    sell_orders_lst.append({"order_id" : 500 + i,
                            "stock_name" : x,
                            "quantity" : n,
                            "price" : p,
                            "order_side" : "SELL",
                            "order_status" : "None"
                           })
    
orders_lst.extend(sell_orders_lst)




##### Creating files for buy orders and sell orders #####

import csv

# csv header
header = ['order_id', 'stock_name', 'quantity', 'price', 'order_side', 'order_status']

# csv data
with open('orders.csv', 'w', encoding='UTF8', newline='') as orders:
    try:
        writer = csv.DictWriter(orders_lst, fieldnames=header)
        writer.writeheader()
        writer.writerows(orders_lst)
    except:
        print("Cannot find the object 'orders_lst'!")
    finally:
        print("File successfully created")

    

##### Set the index of the DataFrame to the order ID #####
import pandas as pd
orders = pd.read_csv('orders.csv')




##### Create a list called orderBooks which contains order books for each stock #####
orderBooks = []
for i in stock_names:
    orderBook = orders[orders.stock_name == i]
    orderBooks.append(orderBook)
