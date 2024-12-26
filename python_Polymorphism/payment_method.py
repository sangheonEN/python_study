class PaymentMethod:
    def pay(self, amount):
        raise NotImplementedError("Subclasses must implement this method")

class CardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} using Card.")

class CashPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid {amount} in Cash.")


def process_payment(payment_method, amount):
    payment_method.pay(amount)

# 다형성 사용
card = CardPayment()
cash = CashPayment()

process_payment(card, 100)  # Paid 100 using Card.
process_payment(cash, 50)  # Paid 50 in Cash.