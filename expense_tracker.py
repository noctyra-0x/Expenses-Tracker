                          #Expense Tracker
def format_line(item_name, price):
    return f"item: {item_name.title()} , Price: ${price:.2f}"

def get_valid_price():
    while True:
        try:
            return float(input("Enter item price: $"))
        except ValueError:
            print("Invalid price! Kindly enter numbers only (e.g. 34.4)")

expenses=[]
while True:
    print("\n--- EXPENSE TRACKER MENU ---")
    print("1. Add New Expense")
    print("2. View All Expenses")
    print("3. Save & Exit")
    
    choice = input("Choose an option (1-3): ")

    if choice =="1":
        name =input("Enter item name: ")
        cost =get_valid_price()
        expenses.append({"name":name, "price":cost})
        print(f"Added {name.title()} successfully")
    elif choice =="2":
        if not expenses:
            print("--Not Expenses Yet--")
        else:
            for item in expenses:
                print("--Current Expenses--")
                print(format_line (item["name"], item["price"]))
        
    elif choice =="3":
        with open("file.txt", "w" ) as f:
            f.write("--Final Receipt--")
            total=0
            for item in expenses:
                line=format_line(item["name"], item["price"])
                f.write(line + "\n")         
                total +=item["price"]
            f.write("\nTotal Spent: ${total:.2f}\n")
        print("\n Receipt saved to 'file.txt' Successfully!!")
        break
    else:
        print("invalid num, Kindly choice (1-3)")