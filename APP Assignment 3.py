#parent class from which every payment strategy inherits the pay() method, basically a guideline for all payment classes
class PaymentStrategy: 
    def pay(self, amount):
        raise NotImplementedError("Subclasses must implement this method")

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid Rs. {amount} using Credit Card.") # Credit Card Payment Strategy

class PayPalPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid Rs. {amount} using PayPal.") # PayPal Payment Strategy

class BitcoinPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid Rs. {amount} using Bitcoin.") # Bitcoin Payment Strategy

class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy #this creates a blueprint for the payment method which takes in "mode of payment" as an argument

    def set_strategy(self, strategy):
        self.strategy = strategy #keeps updating the payment strategy according to which class method is called in what order

    def process_payment(self, amount):
        self.strategy.pay(amount) #calls the pay() method for the payment strategy which is set in the previous step

#Object creation
credit_card = CreditCardPayment() 
paypal = PayPalPayment()
bitcoin = BitcoinPayment()

processor = PaymentProcessor(credit_card) #begins with credit card then later switches control to another payment strategy

print("Using Credit Card:")
processor.process_payment(1500)
print("_____________________________________________________")

print("\nSwitching to PayPal:")
processor.set_strategy(paypal)
processor.process_payment(2000)
print("_____________________________________________________")

print("\nSwitching to Bitcoin:")
processor.set_strategy(bitcoin)
processor.process_payment(3500)
print("_____________________________________________________")