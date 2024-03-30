# sort the exchanges for each buy order from highest price to the lowest
# Execute the order with the highest price first
# record the trade into trade history
# update the quantity and the status of the order

from order_book import orderBooks, orders
from Exchange import Exchange

class SORT(Exchange): # Sort class inherit from Exchange class
    def __init__(self, orders, orderBooks):
        super().__init__(orderBooks) # used 'super' to inherit
        self.orders = orders
        self.exchanges = super().get_exchanges()
    
    # exchanges = [stock1:[buyorder1:[exchange1:{},exchange2:{}], buyorder2:[{},{}]], stock2:[buyorder1:[{},{}], buyorder2:[{},{}]]]    
    
    
    def executeTrade(self):
        exchanges = super().get_exchanges()
        trades = [] # create a list that stores trade records
        for stock in exchanges:
            for buyorder in stock:
                index = 0 # set the initial position of the exchange in 'buyorder'
                
                # while the buy order that we are looking at is not fully satisfied and there are still some possible exchanges
                # we break the loop when the order is fully satisfied or we have executed all the possible exchanges
                while self.orders.iloc[buy_id]["order_status"] != "Fully" and index != len(buyorder): 
                    
                    # get the exchange and the trade quantity
                    exchange = buyorder[index]
                    trade_quantity = exchange["quantity"]
                    
                    # add the trade record
                    UpdateTrades(exchange,trade_quantity)
                    
                    # update the quantity and status of orders
                    UpdateOrders(self.orders,exchange,trade_quantity)
                    
                    # increment the index
                    index += 1
                    

    # Create a function that stores trade records
    def UpdateTrades(exchange,trade_quantity):
        trades.append({"order_id" : exchange["order_id"],
                       "stock" : exchange["stock_name"],
                       "quantity" : trade_quantity,
                       "price" : exchange["price"]})
    
    
    # Create a function that updates trade records
    def UpdateOrders(orders,exchange,trade_quantity):
        # get the buy order ID and the sell order ID of the exchange
        buy_id = exchange["order_id"][0]
        sell_id = exchange["order_id"][1]

        # update the quantity
        orders.iloc[buy_id]["quantity"] -= trade_quantity
        orders.iloc[sell_id]["quantity"] -= trade_quantity

        # update the order status
        if orders.iloc[buy_id]["quantity"] != 0:
            orders.iloc[buy_id]["order_status"] = "Partially"
        else:
            orders.iloc[buy_id]["order_status"] = "Fully"

        if orders.iloc[sell_id]["quantity"] != 0:
            orders.iloc[sell_id]["order_status"] = "Partially"
        else:
            orders.iloc[sell_id]["order_status"] = "Fully"
