class Investor:
    def __init__(self, name):
        self.name = name
        self.stocks = {}

    def update(self, stock, price):
        print(f"Notification for {self.name}: {stock.symbol} is now priced at {price}")
        self.stocks[stock.symbol] = price

    def display_stocks(self):
        print(f"{self.name}'s stock portfolio:")
        for symbol, price in self.stocks.items():
            print(f"{symbol}: {price}")

class Stock:
    def __init__(self, symbol, price):
        self.symbol = symbol
        self.price = price
        self.investors = []

    def register_investor(self, investor):
        if investor not in self.investors:
            self.investors.append(investor)
            investor.stocks[self.symbol] = self.price

    def unregister_investor(self, investor):
        if investor in self.investors:
            self.investors.remove(investor)
            investor.stocks.pop(self.symbol, None)

    def update_price(self, price):
        self.price = price
        for investor in self.investors:
            investor.update(self, self.price)

if __name__ == "__main__":
    apple_stock = Stock("AAPL", 150)
    google_stock = Stock("GOOGL", 2800)

    investor_1 = Investor("Alice")
    investor_2 = Investor("Bob")

    apple_stock.register_investor(investor_1)
    google_stock.register_investor(investor_2)
    apple_stock.register_investor(investor_2)

    apple_stock.update_price(155)
    google_stock.update_price(2850)

    investor_1.display_stocks()
    investor_2.display_stocks()

    apple_stock.unregister_investor(investor_2)
    apple_stock.update_price(160)

    investor_1.display_stocks()
    investor_2.display_stocks()
