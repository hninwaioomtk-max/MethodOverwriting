class food:
    def price(self):
        print("Food price!")
        

class pizza(food):
    def price(self):
        print("Pizza-7000 MMK")
  

class buger(food):
    def price(self):
        print("Buger-3000 MMK")
        
        
class sandwich(food):
    def price(self):
        print("Sandwich-5000 MMK")
        
        
Food = food()
Pizza = pizza()
Buger = buger()
Sandwich = sandwich()

Food.price()
Pizza.price()
Buger.price()
Sandwich.price()
        


