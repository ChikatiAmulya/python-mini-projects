stocks={
    "AAPL":190,
    "TSLA":230,
    "GOOG":320,
    "MSFT":140,
    "AMZN":150
}
total_amount=0
n=int(input("enter the number of stocks:"))
for i in range(n):
    stock_name=input("enter stock name:").upper()
    quantity=int(input("enter quantity:"))

    if stock_name in stocks:
        investment = stocks[stock_name]*quantity
        total_amount += investment
        print("investment in",stock_name,"=",investment)
    else:
        print("stock not available in the portfolio")
print("Total Investment Value =",total_amount)

file = open("portfolio.txt",'w')
file.write("Total Investment Value =" + str(total_amount))
file.close

print("Result saved succesfully in portfolio.txt")
