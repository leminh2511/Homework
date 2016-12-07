import pymongo
uri = "mongodb://admin:admin@ds119598.mlab.com:19598/cafeteria"
client = pymongo.MongoClient(uri)
db = client.get_default_database()
# Get MENU collection
menu_items = db["menu"].find()
menu_items_length = db["menu"].count()
for i in range(menu_items_length):
    for k,v in menu_items[i].items():
        if k!="_id":
            print(k,v)

def price_find(name):
    for i in range(menu_items_length):
        if menu_items[i]["name"].lower()==str(name.lower()):
            price=menu_items[i]["price"]
            return price

menu_items_order = db["order"].find()
menu_items_order_length = db["order"].count()
bill=0
##for i in range(menu_items_order_length):
##    print(menu_items_order[i])

for i in range(menu_items_order_length):
    bill=[]
    for k in range(len(menu_items_order[i]["order"])):
        print(menu_items_order[i]["order"][k].lower())
        price_find(menu_items_order[i]["order"][k].lower())
        price=price_find(menu_items_order[i]["order"][k].lower())
        bill.append(price)
    print(bill)
    sum(bill)
    print("Hoa don la",sum(bill))
        
    
        
        
        





    
