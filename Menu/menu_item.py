


class MenuItem:
    def __init__(self,name,price,availability_status=False):
        self.name = name 
        self.__price = price 
        self.__availability_status = availability_status 

    def __repr__(self):
        return f"{self.name} - {self.__price} - {self.__availability_status}"

    def __str__(self):
        return f"{self.name} - {self.__price} - {self.__availability_status}"

    
    def get_name(self):
        return self.name 

    def get_price(self):
        return self.__price 


    def is_available(self):
        return self.availability_status 


    def set_price(self,price):
        self.__price = price 


    def set_availability(self,availability):
        self.__availability_status = availability


class FoodItem(MenuItem):
    category = "Food"

class DrinkItem(MenuItem):
    category = "Drinks"




# food_item = FoodItem("Biriyani",300,True)

# drink_item = DrinkItem("Thumbs Up", 30 , True)


# print(food_item.get_name())
# print(food_item.get_price())
# print(type(food_item))
# print(drink_item.get_name())
# print(drink_item.get_price()) 
# food_item.set_price(400)
# print(food_item.get_price())



