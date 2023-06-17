from datetime import datetime

name = input("Enter your name:")

#list of items
lists = '''
rice               Rs: 40/kg
toor dal           Rs: 80/kg
sugar              Rs: 40/kg
salt               Rs: 8/kg
sunflower oil      Rs: 85/kg
ragi               Rs: 60/kg
wheat flour        Rs: 30/kg
colgate            Rs: 85/each
horlicks           Rs: 300/each
gulab jamoon       Rs: 300/kg
garlic mixture     Rs: 200/kg
maza 2ltr bottle   Rs: 190/each
'''
print(list)

#declaration
price = 0
total_price = 0
final_price = 0
price_list = []
p_list = []
item_list = []
quantity_list = []

#rates for item
items = {'rice':40, 
'toor dal':80, 
'sugar':40, 
'salt':8, 
'sunflower oil':85, 
'ragi':60, 
'wheat flour':30, 
'colgate':85, 
'horlicks':300, 
'gulab jamoon':300, 
'garlic mixture':200, 
'maza 2ltr bottle':190}
#options for items
option = int(input("for list of items press 1:"))
if option == 1:
    print(lists)
for i in range(len(items)):
    input_1 = int(input("if you want to buy above the list items press 1 or press 2 for exit:"))
    if input_1 == 2:
        break
    if input_1 == 1:
        item = input("enter your item name:")
        quantity = int(input("enter quantity:"))
        if item in items.keys():
            price = quantity*(items[item])
            price_list.append((item,quantity,items,price))
            total_price+=price
            item_list.append(item)
            quantity_list.append(quantity)
            p_list.append(price)
            gst = (total_price*5/100)
            final_price = gst + total_price
        else:
            print("sorry you entered item is not available")
    else:
        print("you entered wrong number") 

    inp = input("can i bill the items yes or no:")
    if inp == 'yes':
        pass
        if final_price != 0:
            print(26*"*","rajshekar super market",25*"*")
            print("hyderabad",32*" ","Date:",datetime.now())
            print("Name:",name, 30*" ")
            print("Sno", 8*" ", "items", 8*" ","quantity", 3*" ","price")
            for i in range(len(price_list)):
                print(i,10*" " ,item_list[i] ,9*" " ,quantity_list[i], 10*" ",p_list[i])
            print(75*"-")
            print(50*" ","Total_amount:","Rs",total_price)
            print("gst amount",50*" ",2*" ", "Rs",gst)
            print(75*"-")
            print(50*" ","final_amount:","Rs",final_price)
            print(75*"-")
            print(23*" ", ">>> thanks for visiting <<<")
            print(75*"*")