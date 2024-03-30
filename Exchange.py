##### Create a class that matches the buy orders with the sell orders #####

from order_book import orderBooks, stock_names


class Exchange:
    def __init__(self, orderBooks, stock_names):
        self.orderBooks = orderBooks
        self.stock_names = stock_names
    
    
    # Create a list called 'exchanges' that stores exchange books for each buy order
    # each exchange book contains all the possible exchanges for a buy order
    def set_exchanges(self):
        
        # initialize 'exchanges'
        exchanges = []
        
        # looking at one stock at a time
        for orderBook in self.orderBooks:
            
            # get the name of the stock
            index = self.orderBooks.index(orderBook)
            stock_name = self.stock_names[index]
            
            # initialize the exchange_book for the stock we are looking
            exchange_book = []
            
            # Seperating buy orders and sell orders
            buys = orderBook[orderBook.order_side == "BUY"]
            sells = orderBook[orderBook.order_side == "SELL"]
            
            # sort the buy orders in decending order and sell orders in acending order
            sorted_buys = sorted(buys, key=lambda x: x["price"], reverse=True)
            sorted_sells = sorted(sells, key=lambda x: x["price"], reverse=False)
            
            # Matching sell orders to a buy order
            for buy in sorted_buys:
                
                # initialize the exchange book for the buy order we are looking
                exchange_book_buy = []
                
                bq = buy["quantity"]
                bp = buy["price"]
                
                for sell in sorted_sells:
                    sq = sell["quantity"]
                    sp = sell["price"]
                    exchange(bq,bp,sq,sp,buy,sell,stock_name)
                
                # store the exchange book for a particular buy order into the exchange_book
                exchange_book.append(exchange_book_buy)
            
            # store the exchange book for a particular stock into 'exchanges'
            exchanges.append(exchange_book)
        
        self.exchanges = exchanges
        
    
    def get_exchanges(self):
        return self.exchanges
    
    
    # Create a function that checks whether the sell shares is 0 
    # and the buy price is not less than the sell price
    def Check(bp,ss,sp):
        if ss != 0:
            if bp >= sp:
                return True
        return False


    # create a function that records reasonable exchanges
    def exchange(bq,bp,sq,sp,buy,sell,stock_name):
        
        # check the conditions
        if Check(bp,sq,sp):

            # the records depend on quantity
            if bq > sq:
                exchange_book_buy.append({"order_id" : [buy["order_id"], sell["order_id"]],
                                          "stock_name" : stock_name,
                                          "quantity" : sq,
                                          "price" : bp})
            else:                                
                exchange_book_buy.append({"order_id" : [buy["order_id"], sell["order_id"]],
                                          "stock_name" : stock_name,
                                          "quantity" : bq,
                                          "price" : bp})

    
    
    # Create a fuction that calculate the total trade value generated today
    def set_todaysTradeValue(self,trades):
        
        todaysTradeValue = 0 # initialise the value
        
        for i in trades:
            todaysTradeValue += i["quantity"] * i["price"]
        
        self.todaysTradeValue = todaysTradeValue
        
    
    def get_todaysTradeValue(self, trades):
        return self.todaysTradeValue
    
    
    def feeLadder(self, exchange):
        if exchange["quantity"] >= 50:
            exchange["fee"] = 5
        else:
            exchange["fee"] = 10
