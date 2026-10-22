from Menu import menu_item,Menu



class OrderItem:

    def __init__(self,menu_item,quantity) :
        self.menu_item = menu_item
        self.__quantity = quantity 
        self.__locked_price = menu_item.get_price()
 

    def get_quantity (self):
        return self.__quantity 

    def set_quantity(self,quantity):
        self.__quantity = quantity 

    def get_locked_price(self):
        return self.__locked_price

    def sub_total(self):
        return float(self.__locked_price*self.__quantity)








