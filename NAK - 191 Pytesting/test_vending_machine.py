"""Python Program For Vending Machine"""
TOTALITEMS = [
        {
            "item_id": 0,
            "item_name": "Samosa",
            'item_price': 20,
        },
        {
            "item_id": 1,
            "item_name": "Sprite",
            'item_price': 90,
        },
        {
            "item_id": 2,
            "item_name": "Kurkure",
            'item_price': 10,
        },
        {
            "item_id": 3,
            "item_name": "Thumbs Up",
            'item_price': 90,
        },
        {
            "item_id": 4,
            "item_name": "Vada Pav",
            'item_price': 20,
        },
    ]

PURCHASEDITEMS = []
class VendingMachine():
    """
    Class Created
    """
    print("------- Vending Machine with Python-------\n\n")
    print("----------The Items In Stock Are----------\n\n")

    for i in TOTALITEMS:
        print(f"Item: {i['item_name']} - Price: {i['item_price']} - Item ID: {i['item_id']}")


    def vending_machine_method(self, TOTALITEMS, purchased_items):
        """Function"""
        while True:

            buy_item = int(input("\n\nEnter the item code of the product you wa0nt to buy: "))

            if buy_item < len(TOTALITEMS):
                PURCHASEDITEMS.append(TOTALITEMS[buy_item])
            else:
                print("THE PRODUCT ID IS WRONG!")
            more_items = str(input("press Y to add more items and press q for checkout. "))

            print("")

            if more_items == "Y":

                for i in TOTALITEMS:
                    print(f"Item: {i['item_name']} - Price: {i['item_price']} - Item ID: {i['item_id']}")
            elif more_items == "q":
                self.checkout_func(PURCHASEDITEMS)
                break

    def sum_func(self, PURCHASEDITEMS):
        """Sum Function"""
        item_sum = 0

        for i in PURCHASEDITEMS:
            item_sum += i["item_price"]

        return item_sum


    def checkout_func(self, PURCHASEDITEMS):
        """Checkout Fun"""
        print("Select Payment Method from below :")
        print("1. Cash")
        print("2. Card")
        choice = int(input("Enter Payment Option : "))
        total_sum = self.sum_func(PURCHASEDITEMS)
        if choice == 1:
            print("Your Total Amount is ", total_sum, " and you selected Cash Payment.")
            while True:
                cash_amount = int(input("Enter the Amount to pay : "))
                if cash_amount == total_sum:
                    print("Order Placed Successfully. Thankyou.")
                    break
                if cash_amount < total_sum:
                    print("Insufficient Balance ,Please enter Valid Amount")
                if cash_amount > total_sum:
                    print("Collect Your Remaining Money ", cash_amount - total_sum)
                    print("Order Placed Successfully. Thankyou.")
                    break
        if choice == 2:
            print("you selected Card payment method.\nYour Total amount is ", total_sum, "\n and Convinience Fees is ", total_sum)
            print("So you have to pay Total ", total_sum, " + ", total_sum, " = ", total_sum * 2)
            while True:
                card_amount = int(input("Enter the Amount to pay : "))
                if card_amount == total_sum * 2:
                    print("Order Placed Successfully. Thankyou.")
                    break
                if card_amount < total_sum * 2:
                    print("Insufficient Balance ,Please enter Valid Amount")
                if card_amount > total_sum * 2:
                    print("Collect Your Remaining Money ", card_amount - total_sum * 2)
                    print("Order Placed Successfully. Thankyou.")
                    break



OBJ = VendingMachine()
OBJ.vending_machine_method(TOTALITEMS, PURCHASEDITEMS)
