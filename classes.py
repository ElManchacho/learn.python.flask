from enum import Enum
from sqlalchemy.orm import relationship
import datetime
import uuid


class Event(Enum):
    RECEIVE = 'receive'
    SALE = 'sale'
    LOSS = 'loss'

class Status(Enum):
    CANCELLED = 'cancelled'
    VALIDATED = 'validated'
    INPROCESS = 'in process'

class Car :
    def __init__(self, id:int, brand:str,model:str,power:int):
        self.id = id
        self.brand = brand
        self.model = model
        self.power = power

class Customer :
    def __init__(self, id:uuid.UUID, email:str, phone:str,orders:list):
        self.id = id
        self.email = email
        self.phone = phone
        self.orders = orders

class Order:
    def __init__(self, id:int, buyer:Customer, car:Car, status:Status, createdAt:datetime.date):
        self.id = id
        self.buyer = buyer
        self.car = car 
        self.status = status 
        self.createdAt = createdAt

class StockHistory:
    def __init__(self, car:Car, event:Event, timestamp:datetime.date):
        self.car = car
        self.event = event
        self.timestamp = timestamp
