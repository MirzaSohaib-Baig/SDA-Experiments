from abc import ABC, abstractmethod


class Payment(ABC):
    
    @abstractmethod
    def pay(self):
        pass


class Cash(Payment):
    
    def __init__(self, cash):
        self.cash = cash

    def pay(self, name):
        print(f'Payment by {self.cash} from {name}')


class Card(Payment):
    
    def __init__(self, card):
        self.card = card

    def pay(self, name):
        print(f'Payment by {self.card} from {name}')


class Person:
    
    def __init__(self, name, card, cash):
        self.name = name
        self.card = card
        self.cash = cash


class NotificationManager:
    
    def __init__(self, notification):
        self.notification = notification

    def send(self, name):
        self.notification.pay(name)


if __name__ == '__main__':
    p1 = Person('John Doe', 'Cash', 'Card')

    cash_payment = Cash(p1.cash)
    card_payment= Card(p1.card)

    notification_manager = NotificationManager(cash_payment)
    notification_manager.send(p1.name)

    notification_manager = NotificationManager(card_payment)
    notification_manager.send(p1.name)