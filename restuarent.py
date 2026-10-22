from Menu import Menu
from Menu.menu_item import FoodItem,DrinkItem
from Order.order_item import OrderItem
from Order import Order
from Payment.cash import CashPayment    


class Restuarent:
    current_max_order_id = 0 
    def __init__(self,name):
        self.name = name 
        self.menu = Menu()
        self.active_order = {}

    @classmethod
    def create_order(cls):
        order = Order(order_id=cls.current_max_order_id+1)
        return order

    def create_order_items(self,order_items):
        items = []
        for order_item in order_items : 
            # {"menu_item":<obj Menu Item> , quantity=2}
            item = OrderItem(menu_item=order_item["menu_item"] , quantity=order_item["quantity"])
            items.append(item)
        return items 
    

    def create_payment(self,order,type):
        if type=="Cash" : 
            payment = CashPayment(order=order)
            return payment
        elif type=="UPI":
            pass
        else:
            return "Invalid Payment Method"


    
    def add_items_to_order(self,order,items):
        for item in items : 
            order.add_item(item)


    def create_order_with_items(self,items):
        order_items = self.create_order_items(items)
        cls = self.__class__
        order = cls.create_order()
        self.active_order[order.order_id] =  order
        self.add_items_to_order(order=order,items=order_items)
        return order

    def billing(self,payment,**kwargs):
        if isinstance(payment,CashPayment) :
            payment.set_cash_recieved(kwargs["cash_recieved"])
        else:
            pass  

    def show_bill(self,order,**kwargs):
        for item in order.order_items:
            print(item.menu_item.name,item.get_quantity(),item.get_locked_price(),item.sub_total())
        print(order.calculate_sub_total())    
       



    def process_bill(self,payment) : 
        status = payment.process_payment ()

        if status : 
            return "Payment Done Successfully"
        else:
            return "Invalid Payment "


#Flow 

# Create Restuarent 

restuarent = Restuarent("Sithara Restuarent")

# Create MenuItem 
print(restuarent.menu.get_available_items())

chicken_lolipop = FoodItem("Chicken Lollipop",300,True)
chicken_dum_biriyani = FoodItem("Chicken Dum Biriyani",400,True)
thumbs_up = DrinkItem("Thumbs Up", 50 , True)
pineapple_juice = DrinkItem("Pine Apple Juice",100,True)



restuarent.menu.add_item(chicken_dum_biriyani)
restuarent.menu.add_item(chicken_lolipop)
restuarent.menu.add_item(thumbs_up)
restuarent.menu.add_item(pineapple_juice)

# 

l = [{
    "menu_item":chicken_dum_biriyani,
    "quantity":2 
},
{
    "menu_item":chicken_lolipop,
    "quantity":1
},
{
    "menu_item":thumbs_up,
    "quantity":1 
},
{
    "menu_item":pineapple_juice,
    "quantity":1
}
]


order = restuarent.create_order_with_items(items=l)

payment = restuarent.create_payment(order,type="Cash")
restuarent.show_bill(order)

restuarent.billing(payment,cash_recieved=1250)

print(restuarent.process_bill(payment=payment))

  







# restuarent = Restuarent("Sithara Restuarent")

# print(restuarent.menu.get_available_items())

# chicken_lolipop = FoodItem("Chicken Lollipop",300,True)
# chicken_dum_biriyani = FoodItem("Chicken Dum Biriyani",400,True)
# thumbs_up = DrinkItem("Thumbs Up", 50 , True)
# pineapple_juice = DrinkItem("Pine Apple Juice",100,True)



# restuarent.menu.add_item(chicken_dum_biriyani)
# restuarent.menu.add_item(chicken_lolipop)
# restuarent.menu.add_item(thumbs_up)
# restuarent.menu.add_item(pineapple_juice)


# #### Customer 

# order_item1 = OrderItem(chicken_lolipop,1)
# order_item2 = OrderItem(chicken_dum_biriyani,2)
# order_item3 = OrderItem(pineapple_juice,1)
# order_item4 = OrderItem(thumbs_up,1)

# order = Order(order_id=1)

# order.add_item(order_item1)
# order.add_item(order_item2)
# order.add_item(order_item3)
# order.add_item(order_item4)


# #### Billing 
# print(order.caliculate_subtotal())
# cash_payment = CashPayment(cash_recieved=1300,order=order)

# print(cash_payment.process_payment())




































# from Menu import Menu 
# from Menu.menu_item import DrinkItem,FoodItem
# from Order.order_item import OrderItem
# from Order import Order
# from Payment.cash import CashPayment
# from Payment.upi import UPIPayment


# menu = Menu()
    
# biriyani = FoodItem("Biriyani",399,True)
# thumbs_up = DrinkItem("Thumbs Up", 49, True)

# menu.add_item(biriyani)
# menu.add_item(thumbs_up)

# order_item1  = OrderItem(biriyani,2)
# order_item2 = OrderItem(thumbs_up,2)

# print(order_item1.get_locked_price())

# biriyani.set_price(399)
# print(biriyani.get_price())


# print(order_item1.get_locked_price())
# print(order_item1.get_quantity())
# print(order_item1.sub_total())

# # print(biriyani.get_price())

# order = Order("ORD1")
# order.add_item(order_item1)
# order.add_item(order_item2)


# order.update_quantity(order_item1,3)


# print("Bill :", order.caliculate_subtotal())

# cash_payment = CashPayment(cash_recieved=1500,order=order)
# print(cash_payment.caliculate_change())
# print(cash_payment.process_payment())

