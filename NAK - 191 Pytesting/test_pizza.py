class Customer:
    """Customer Class Is Created"""
    queue = []
    print(" Greetings! Here is your menu options and pricing. We serve pizzas and pastas.");
    def main():
        res = int(input("Is customer ready for placing order?true/false"))

    def order(self):
        while True:
            choice = int(input("Input 1. for Pizza or 2. Pasta."))
            if choice == 1:
                print("For pizza lovers available:\n 3 sizes (cost 'x' times)-- x=1. Small 2. Medium 3. Large; \n 2 crusts (no charge) -- 1. Thin or 2. Thick; \n 3 flavors -- 1. veg (20x USD) 2. non-veg (25x USD) 3. vegan (15x USD); \n toppings (1 USD each)-- 1.Cheese,2.Mushroom,3.Tomato,4.Jalapeno,5.Spinach \n")
                print("")
                size = int(input("Pizza size 1. Small 2. Medium 3. Large"))
                crust = int(input("Crust 1. Thin or 2. Thick"))
                flavor = int(input("Flavors 1. veg or 2. non-veg or 3. vegan "))
                n = int(input("How Many toppinga"))
                topping = []
                for i in range(n):
                   topping.append(int(input("Input choice for topping 1.Cheese,2.Mushroom,3.Tomato,4.Jalapeno,5.Spinach")))

            if choice == 2:
                print("For pasta lovers available:\n 2 flavors-- 1. White sauce or 2. Red Sauce (10 USD); \n 2 types (no charge) -- 1. Penne or 2. Ditalini")
                print("")
                print("Pasta sauce 1. White sauce or 2. Red Sauce")
                sauce = int(input("Type 1. Penne or 2. Ditalini"))   
                type = int(input("Type 1. Penne or 2. Ditalini"))

OBJ = Customer()
OBJ.order()
                


