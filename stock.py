def stock_portfolio():
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "AMZN": 120
    }

    print(" Welcome to Stock Portfolio Tracker")
    num_stocks = int(input("How many stocks do you have? "))
    total = 0
    portfolio = {}

    for _ in range(num_stocks):
        stock = input("Enter stock symbol: ").upper()
        quantity = int(input(f"Enter quantity of {stock}: "))
        price = stock_prices.get(stock, 0)
        value = price * quantity
        total += value
        portfolio[stock] = (quantity, price, value)

    print("\n Portfolio Summary:")
    for stock, data in portfolio.items():
        print(f"{stock}: Quantity={data[0]}, Price={data[1]}, Value={data[2]}")
    
    print("Total Investment Value:", total)

if __name__ == "__main__":
    stock_portfolio()
