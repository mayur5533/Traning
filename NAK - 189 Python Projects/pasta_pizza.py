
class Pizza:
    """Class Is Created"""
    size = 0
    crust = 0
    flavour = 0
    toppings = []
    flavour_price = {1:50, 2:100, 3:70}
    def is_topping_valid(self):
        """is_topping_available method is created"""
        flag = True
        for i in self.toppings:
            if i not in range(1, 6):
                flag = False
                break
        return flag

    def is_available(self):
        if self.size in [1, 2, 3] and self.crust in [1, 2] and self.flavour in [1, 2, 3] and self.is_topping_valid():
            return True
        else:
            return False
    
    def __str__(self):
        return f"Pizza of size {self.size},  crust {self.crust},  flavour {self.flavour},  toppings {self.toppings}"

class Pasta:
    sauce = 0
    type = 0
    sauce_price = {1:70, 2:50}
    type_price = {1:30, 2:50}

    def isAvailable(self):
        if self.sauce in [1, 2] and self.type in [1, 2]:
            return True
        else:
            return False
    
    def __str__(self):
        return f"Pasta of sauce {self.sauce},  type {self.type}"

class Customer:
    """Customer Class Is Created"""
    print(" Greetings! Here is your menu options and pricing. We serve pizzas and pastas.")

    orderList = []
    total_bill = 0
    def order(self):
        while True:
            res = input("\n Is customer ready for placing order?true/false:- ").lower()
            if res == "true":
                choice = int(input("Input 1. for Pizza or 2. Pasta. :- "))
                if choice == 1:
                    print("For pizza lovers available:\n 3 sizes (cost 'x' times)-- x=1. Small 2. Medium 3. Large; \n 2 crusts (no charge) -- 1. Thin or 2. Thick; \n 3 flavors -- 1. veg (20x USD) 2. non-veg (25x USD) 3. vegan (15x USD); \n toppings (1 USD each)-- 1.Cheese, 2.Mushroom, 3.Tomato, 4.Jalapeno, 5.Spinach \n")
                    pizza = Pizza()
                    pizza.size = int(input("Pizza size 1. Small 2. Medium 3. Large :-"))
                    pizza.crust = int(input("Crust 1. Thin or 2. Thick :- "))
                    pizza.flavour = int(input("Flavors 1. veg or 2. non-veg or 3. vegan :- "))
                    n = int(input("How Many toppinga :- "))
                    topping = []
                    for i in range(n):
                        topping.append(int(input("Input choice for topping 1.Cheese, 2.Mushroom, 3.Tomato, 4.Jalapeno, 5.Spinach")))
                    pizza.toppings = topping.copy()

                    if pizza.is_available():
                        print("On our way to prepare ur order")
                        self.orderList.append(pizza)
                    else:
                        print('We cannot prepare ur order')
                elif choice == 2:
                    print("For pasta lovers available:\n 2 flavors-- 1. White sauce or 2. Red Sauce (10 USD); \n 2 types (no charge) -- 1. Penne or 2. Ditalini")
                    pasta = Pasta()
                    pasta.sauce = int(input("Pasta sauce 1. White sauce or 2. Red Sauce :- "))
                    pasta.type = int(input("Type 1. Penne or 2. Ditalini :- "))
                    if pasta.isAvailable():
                        self.orderList.append(pasta)
                        print("On our way to prepare ur order")
                    else:
                        print('We cannot prepare ur order')
                else:
                    print("Sorry! not in menu this time. Please try something else.")
                
                print("Your Order: ", end=" ")
                for i in self.orderList:
                    print(i, end=",  ")
            
            else: 
                break
    
    def totalbill(self):        
        for i in self.orderList:
            item_bill = 0
            if isinstance(i, Pizza):
                item_bill += i.size * 100
                item_bill += i.flavour_price[i.flavour]
                item_bill += len(i.toppings) * 20
            if isinstance(i, Pasta):
                item_bill += 100
                item_bill += i.sauce_price[i.sauce]
                item_bill += i.type_price[i.type]
            
            self.total_bill += item_bill
        print(f"Total bill: {self.total_bill}")
        print("")
        print("Select Payment Method from below :")
        print("1. Cash")
        print("2. Card")
        choice = int(input("Enter Payment Option : "))
        if choice == 1:
            print("Your Order: ", end=" ")
            for i in self.orderList:
                print(i, end=",  ")
            print("")    
            print("Your Total Amount is ", self.total_bill, " and you selected Cash Payment.")
            while True:
                cash_amount = int(input("Enter the Amount to pay : "))
                if cash_amount == self.total_bill:
                    print("Order Placed Successfully. Thankyou.")
                    break
                if cash_amount < self.total_bill:
                    print("Insufficient Balance , Please enter Valid Amount")
                if cash_amount > self.total_bill:
                    print("Collect Your Remaining Money ", cash_amount - self.total_bill)
                    print("Order Placed Successfully. Thankyou.")
                    break
        if choice == 2:
            print("")
            print("Your Order: ", end=" ")
            for i in self.orderList:
                print(i, end=",  ")
            print("you selected Card payment method.\nYour Total amount is ", self.total_bill, "\n and Convinience Fees is ", self.total_bill)
            print("So you have to pay Total ", self.total_bill, " + ", self.total_bill, " = ", self.total_bill * 2)
            while True:
                card_amount = int(input("Enter the Amount to pay : "))
                if card_amount == self.total_bill * 2:
                    print("Order Placed Successfully. Thankyou.")
                    break
                if card_amount < self.total_bill * 2:
                    print("Insufficient Balance , Please enter Valid Amount")
                if card_amount > self.total_bill * 2:
                    print("Collect Your Remaining Money ", card_amount - self.total_bill * 2)
                    print("Order Placed Successfully. Thankyou.")
                    break
   


c = Customer()
c.order()
c.totalbill()
