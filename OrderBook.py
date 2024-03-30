##### Create a class that manages orders (add new orders, cancel, or replace orders) #####
##### dealing with 1 order at a time!!!!! #####

from order_book import orders

class OrderBook:
    def __init__(self, input_order, orders):
        self.input_order = input_order
        self.orders = orders
        self.id = input_order["order_id"]
    
    # Create a function that enables users to add new orders, one at a time
    def newOrder(self):
        # add the new order into the order book
        self.orders.append(input_order, ignore_index=True)
        self.orders.to_csv("orders_data.csv", index=False) # write into file
        print("Your order ID is: " + str(input_order["order_id"])) # print the order ID
        
    # Create a funcion that enables users to cancel a specific order according to the order ID inputed
    def cancelOrder(self):
        index = self.orders[self.orders['order_id'] == self.id].index
        self.orders.drop(index, inplace=True)
        self.orders.to_csv("orders_data.csv", index=False) # write into file
        print("You have cancelled your order")
    
    # Create a funcion that enables users to amend a specific order according to the order ID inputed
    def replaceOrder(self):
        # get the order
        index = self.orders[self.orders['order_id'] == self.id].index
        # amend the order
        data.loc[index, 'stock_name'] = input("Please enter the stock name:")
        data.loc[index, 'quantity'] = int(input("Please enter the quantity:"))
        data.loc[index, 'price'] = int(input("Please enter the price:"))
        # does not allow to change order side
        print("You have updated your order")
        
    # Create a funcion that enables users to view the orders buy inputing the order ID
    def viewOrder(self):
        index = self.orders[self.orders['order_id'] == self.id].index
        print(data.loc[index])
    # can be improved by putting this into Login System

        
##### Create a fuction that take different order details from user depend on the choice #####
def inputOrder():
    # Present the Menu to the users for them to choose the actions
    print("***** Menu ***** \n1. New orders \n2. Cancel orders \n3. Replace orders \n4. Exit")
    
    # require input depend on the choice
    choice = 1
    while choice != 4:
        # Require choice
        choice = int(input("Please enter your choice:"))
        
        # Exit
        if choice == 4:
            print("You have exit the system.")
            break
        
        # New order
        elif choice == 1:
            input_order = {"order_id" : orders.iloc[-1,0]+1, # set the new id as the id of the last order plus 1
                           "stock_name" : input("Please enter the stock name:"),
                           "quantity" : int(input("Please enter the quantity:")),
                           "price" : int(input("Please enter the price:")),
                           "order_side" : input("SELL or BUY:"),
                           "order_status" : "None"}
        # Cancel order
        elif choice == 2:
            input_order = {"order_id" : int(input("Please enter your order ID:"))}
        
        # Replace order
        elif choice == 3:
            input_order = {"order_id" : int(input("Please enter your order ID:"))}
    
    return input_order
