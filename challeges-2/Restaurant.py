
class Menu :
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.is_available = True


class Restaurant : 
    def __init__(self):
        self.menu = []
    
    def add_item(self,item):
        self.menu.append(item)
    
    def show_menu(self):
        for m in self.menu:
            status = "Available" if m.is_available else "Not available"
            print(f" name {m.name}  -- price {m.price} status : {status}")
    
    def order_item(self, name):
        for men in self.menu:
            if men.name.lower() == name.lower():
                men.is_available = False
                return f"You have ordered '{name}'."
        return f"'{name}' is not found in our menu."

    def restock_item(self, name):
        for men in self.menu:
            if men.name.lower() == name.lower():
                men.is_available = True
                return f"'{name}' has been restocked."
        return f"'{name}' is not found in our menu."


    
menu1  = Menu("Basto", 19.99)
menu2  = Menu("Caano", 42.99)
menu3 = Menu("Baris", 25.99)

restraurent = Restaurant()

restraurent.add_item(menu1)
restraurent.add_item(menu2)
restraurent.add_item(menu3)



restraurent.show_menu()


"order"
restraurent.order_item("Basto")
restraurent.show_menu()


"restock"

restraurent.restock_item("Basto")
restraurent.show_menu()



            
        

        