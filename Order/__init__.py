
class Order:

    def __init__(self,order_id,order_status="Placed",discount_amount=0): 
        self.order_id = order_id 
        self.order_items = []



    def add_item(self,order_item):
        self.order_items.append(order_item)

    def remove_item(self,order_item):
        self.order_items.remove(order_item)

    def update_quantity(self,order_item,quantity) :
        order_item.set_quantity(quantity)

    def calculate_sub_total(self):
        sub_total = 0
        for order_item in self.order_items :
            sub_total  += order_item.sub_total()
        return sub_total 

    

