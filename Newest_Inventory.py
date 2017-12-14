import sqlite3

DBFILENAME = "inventory.sqlite"
CON = sqlite3.connect(DBFILENAME)

#Functions and Declarations
def add_item(): #Function to Add Items to the Inventory System. Each Variables name is representative of the value it holds
    c = CON.cursor() #Create a cursor object to perform functions within the database
    N = input("Enter the name of the item to add:")
    Q = input("How many units would you like to add for " + N + ":")
    D = input("Enter a description for " + N + ":")
    H = input("Enter the height of " + N + ":")
    W = input("Enter the Width of " + N + ":")
    L = input("Please enter the length of " + N + ":")
    Lb = input("Enter the weight of " + N + ":")
    P = input("Enter the price of " + N + ": $")
    print("Name: " + N)
    print("Quantity: " + Q)
    print("Description: " + D)
    print("Height: " + H)
    print("Width: " + W)
    print("Length: " + L)
    print("Weight: " + Lb)
    print("Price: " + P)
    confirm = input("Are all of the fields entered correctly? (Enter Y for Yes or N for No) ")
    if confirm == "Y": #Function to confirm the adding of the new item to the database
        c.execute(' ' 'INSERT INTO items(Name, Quantity, Description, Height, Width, Weight, Length, Price) VALUES(?,?,?,?,?,?,?,?)' ' ', (N,Q,D,H,W,Lb,L,P))
        CON.commit()
        print("Inventory Updated!")

def browse_items(): #Browse the Items already stored in the database
    c = CON.cursor()
    c.execute("SELECT * FROM items")
    items = c.fetchall()
    for row in items:
        print(row)

def search_items():
    raise NotImplementedError("search_items")

def place_order():
    raise NotImplementedError("place_order")

def main_menu():
    print("PyInv Version 0.1")
    print("Please enter the number for the function you'd like to perform")
    print("Add Item ------------- 1")
    print("Search For Item ------ 2")
    print("Browse Inventory ----- 3")
    print("Place an Order ------- 4")
    print("Exit ----------------- 5")
    choice = input("Your choice: ")
    print("You chose option", choice)

    if choice == "1":
        add_item()
    elif choice == "2":
        search_items()
    elif choice == "3":
        browse_items()
    elif choice == "4":
        place_order()
    elif choice == "5":
        print("bye")
        return
    else:
        print("Please choose the number(1-5) of the function you'd like to perform")

    main_menu() # This will loop the menu unless they choose to exit.

# Main Program
# By default, Python starts executing the first "executable" statement it finds.
# This is the first one in this file:
print("this will be the the first thing that happens when you run this file")

# The if statement below is a trick that will only run the code if this file is
# The `__name__` identify is typically the name of the module,
# but when your program is being executed, it is assigned the `__name__` of "__main__".
if __name__ == "__main__":
    main_menu()
    CON.close()
