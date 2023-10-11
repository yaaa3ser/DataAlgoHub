from abc import ABC, abstractmethod

class IPayment(ABC):  # I for Interface
    @abstractmethod
    def set_user_info(self, user_info):
        pass
    
    @abstractmethod
    def set_card_info(self, card_info):
        pass
    
    @abstractmethod
    def pay_money(self, money):
        pass

# paypal
class PayPalCreditCard:
    def __init__(self, name = None, address= None,
          id= None, expire_date= None, ccv= None):
        self.name = name
        self.address = address
        self.id = id
        self.expire_date = expire_date
        self.ccv = ccv


class PayPalOnlinePaymentAPI:
    def __init__(self, card_info : PayPalCreditCard = None):
        self.card_info = None

    def pay_money(self, money):
        print(f'PayPalOnlinePaymentAPI request')
        return True # Call PayPal backend
    

# stripe
class StripeUserInfo:
    def __init__(self, name = None, address = None):
        self.name = name
        self.address = address


class StripeCardInfo:
    def __init__(self, id = None, expire_date = None):
        self.id = id
        self.expire_date = expire_date


class StripePaymentAPI:
    @staticmethod
    def withdraw_money(user_info, card_info, money):
        print(f'StripePaymentAPI request')
        return True # Call Stripe backend
    


class Paypal(IPayment):
    def __init__(self):
        self.paypal = PayPalOnlinePaymentAPI()
        self.user = PayPalCreditCard()
    
    def set_user_info(self, name, address):
        self.user.name = name
        self.user.address = address
    
    def set_card_info(self, id, expire_date, ccv):
        self.user.id = id
        self.user.expire_date = expire_date
        self.cvv = ccv
    
    def pay_money(self, money):
        return self.paypal.pay_money(money)

class Stripe(IPayment):
    def __init__(self):
        self.user = StripeUserInfo()
        self.card = StripeCardInfo()
        self.api = StripePaymentAPI()
    
    def set_user_info(self, name, address):
        self.user.name = name
        self.user.address = address
    
    def set_card_info(self, id, expire_date, ccv):
        self.card.id = id
        self.card.expire_date = expire_date
        self.cvv = ccv
    
    def pay_money(self, money):
        return self.api.withdraw_money(self.user, self.card, money)


class TransactionInfo:
    def __init__(self, required_money_amount, name, address, id, expire_date, ccv):
        self.required_money_amount = required_money_amount
        self.name = name
        self.address = address
        self.id = id
        self.expire_date = expire_date
        self.ccv = ccv

# polymorphism
class Payment:
    def __init__(self, payment_method: IPayment):
        self.payment_method = payment_method
    
    def pay(self, transaction_info):
        self.payment_method.set_user_info(transaction_info.name, transaction_info.address)
        self.payment_method.set_card_info(transaction_info.id, transaction_info.expire_date, transaction_info.ccv)
        return self.payment_method.pay_money(transaction_info.required_money_amount)
    

# test
test1 = Payment(Paypal())
test2 = Payment(Stripe())

print(test1.pay(TransactionInfo(100, 'name', 'address', 'id', 'expire_date', 'ccv')))

print(test2.pay(TransactionInfo(100, 'name', 'address', 'id', 'expire_date', 'ccv')))