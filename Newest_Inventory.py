import sqlite3
dbfilename = "inventory.sqlite"
con = sqlite3.connect(dbfilename)
#Functions and Declarations
def addItem(): #Function to Add Items to the Inventory System. Each Variables name is representative of the value it holds
    c = con.cursor() #Create a cursor object to perform functions within the database
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
    print("Width: " + N)
    print("Weight: " + N)
    print("Price: " + N)
    confirm = input("Are all of the fields entered correctly? (Enter Y for Yes or N for No) ")
    if confirm == "Y": #Function to confirm the adding of the new item to the database
        c.execute(' ' 'INSERT INTO items(Name, Quantity, Description, Height, Width, Weight, Length, Price) VALUES(?,?,?,?,?,?,?,?)' ' ', (N,Q,D,H,W,Lb,L,P))
        con.commit()
        print("Inventory Updated!")

def browseItems(): #Browse the Items already stored in the database
    c = con.cursor()
    c.execute("SELECT * FROM items")
    items = c.fetchall()
    for row in items:
        print(row)
        
def mainMenu():
    print("PyInv Version 0.1")
    print("Please enter the number for the function you'd like to perform")
    print("Add Item ------------- 1")
    print("Search For Item ------ 2")
    print("Browse Inventory ----- 3")
    print("Place an Order ------- 4")
    choice = input("Your choice: ")
    print("You chose option ", choice)
    if choice == "1":
         addItem()
    elif choice == "2":
        searchItem()
    elif choice == "3":
        browseItems()
    elif choice == "4":
        placeOrder()
    else:
        print("Please choose the number(1-4) of the function you'd like to perform")
        mainMenu()

#Main Program
mainMenu()
con.close()
