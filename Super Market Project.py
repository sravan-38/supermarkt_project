from datetime import datetime
print(25*"*","SRAVAN SUPER MARKET",25*"*")
name = input("Enter the name:")
address = input("Enter the address:")
lists = '''
salt Rs 30/kg
sugar Rs 35/kg
rice Rs 40/kg
oil Rs 100/liter
Boost Rs 90/each
colgate RS 50/each
dal Rs 70/kg
'''
price = 0
price_list = []
total_price = 0
Final_amount = 0
slist = []
mlist = []
klist = []
items = {"salt":30,"sugar":35,"rice":40,"oil":100,"Boost":90,"colgate":50,"dal":70}
option = int(input("list of items press 1 "))
if option == 1:
    print(lists)
    for i in range(len(items)):
        inp1 = int(input("if you want to buy press 1 or press 2 for exit: "))
        if inp1 == 2:
            break
        if inp1 == 1:
            item = input("Enter your item: ")
            quantity = int(input("enter the quantity: "))
            if item in items.keys():
                price = quantity * (items[item])
                price_list.append((item,quantity,items,price))
                total_price += price
                # print(total_price)
                slist.append(item)
                mlist.append(quantity)
                klist.append(price)
                gst = (total_price*6)/100
                Final_amount = gst + total_price
            else:
                price("sorry your entered item is not available")
        else:
             print("you entered worng number")
        inp = input("can i bill the items yes or no:")
        if inp == "yes":
            pass
        if Final_amount != 0:
            print(25*"=","SRAVAN SUPERMARKET",25*"=")
            print(28*" ","chittor")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"_")
            print("sno",8*" ","items",8*" ","quantity",4*" ","price")
            for i in range(len(price_list)):
                print(i,8*" ",8*" ",slist[i],6*" ",mlist[i],11*" ",mlist[i])
                print(75*"_")
                print(50*" ","total_amount:","Rs",total_price)
                print("gst amount",50*" ",gst)
                print(75*" ")
                print(50*" ","Final_amount:","Rs",Final_amount)
                print(75*"-")
                print(50*" ","Thanks for visiting")
                print(75*"-")
