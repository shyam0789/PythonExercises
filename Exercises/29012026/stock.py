import statistics
stock_dict = {
    "info" : [600,630,620],
    "ril":[1430,1490,1567],
    "mtl":[234,180,160]
}

def get_input():
    user_input = input("Choose one of the below: \n1. Print \n2. Add\n").lower()
    if user_input == "print":
        print_dict()
    elif user_input == "add":
        add_dict()
    else:
        print("Enter valid input.")

def print_dict():
    for comp,price in stock_dict.items():
        # avg = sum(stock_dict[comp])/len(stock_dict[comp])
        avg = statistics.mean(stock_dict[comp])
        print(f"{comp} ==> {stock_dict[comp]} ==> avg: {round(avg,2)}")

def add_dict():
    comp = input("Enter the Stock ticker: ")
    price = int(input("Enter the stock price: "))
    if comp in stock_dict:
        stock_dict[comp].append(price)
    else:
        stock_dict[comp] = [price]
    print_dict()

get_input()