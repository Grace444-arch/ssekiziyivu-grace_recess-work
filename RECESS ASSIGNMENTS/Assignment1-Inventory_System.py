#dictionary to store the available stock
stock={"Oner":"600","Glasses":"50","Spoons":"50","Bread":"100 loaves"}

#the first function called in the program
def main():
    print()
    print()
    print("______Alex's Supermarket Inventory System________")
    print()
    print("Select option:")
    print("1.Display all available stock")
    print("2.Search for an item")
    print("3.Add new item")
    print("4.Update stock levels")
    choice=int(input("Enter option:"))
    while choice<0 or choice>4:
          choice=main()
    
    handle_input(choice)   
       

#adds a new item to the stock
def add(item,amount):
    stock.update({f"{item}":f"{amount}"})

#gets all items from the dictionary using a for loop
def get_all():
    print("Item  Stock level")
    for key,value in stock.items():
        print(f"{key}____{value}")

#gets a specific item
def get_item(item):
    if stock.get(f"{item}"):
        print(f"Stock level:{stock.get(f"{item}")}")    
    else: 
        print("Item not found") 
        
#used to update the stock level of an item       
def update(item,amount):
    if stock.get(f"{item}"):
        stock.update({f"{item}":f"{amount}"}) 
        print("Update successful!")
    else: 
        print("Item not found")         

#this function handles user input
def handle_input(input1):
    if input1==1:
        get_all()
        exit()
    elif input1==2: 
        item=input("Enter item name:")
        get_item(item)
        exit() 
    elif input1==3:
         choice="no"
         while choice=="no":
             item=input("Enter item name:")
             amount=input("Enter stock level:")
             add(item,amount) 
             choice=input("Enter yes to exit:")
         main()    
             
    elif input1==4:
        item=input("Enter item name:")
        amount=input("Enter stock level:")
        update(item,amount) 
        exit()
               
    
#this function is used to call the main function inside other functions  
def exit():
     choice=input("Enter yes to exit:")
     if choice.lower()=="yes":
      main()
    
main()   
