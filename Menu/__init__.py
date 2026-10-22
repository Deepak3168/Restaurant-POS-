

class Menu:
    items = [] 

    @classmethod
    def add_item(cls,menu_item):
        cls.items.append(menu_item)

    @classmethod
    def remove_item(cls,menu_item):
        cls.items.remove(menu_item)

    @classmethod
    def get_available_items(cls):
        return cls.items 



# biriyani = FoodItem("Biriyani",300,True)
# thumbs_up = DrinkItem("Thumbs Up", 50, True)


# rest_menu = Menu()

# rest_menu.add_item(biriyani)
# rest_menu.add_item(thumbs_up)

# for i in rest_menu.get_available_items() : 
#     print(str(i))

    
