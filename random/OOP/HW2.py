# expedia
from abc import ABC, abstractmethod

class Reservation(ABC):
    @property
    @abstractmethod
    def get_cost(self):
        pass
    

class Hotel(Reservation):
    def __init__(self, price_per_night, total_nights):
        self.price_per_night = price_per_night
        self.total_nights = total_nights
    
    @property
    def get_cost(self):
        return self.price_per_night * self.total_nights

class Flight(Reservation):
    def __init__(self, cost):
        self.cost = cost
    
    @property
    def get_cost(self):
        return self.cost

class ItineraryReservation(Reservation):
    def __init__(self):
        self.itinerary = []
    
    def add(self, item):
        self.itinerary.append(item)
    
    @property
    def get_cost(self):
        total = 0
        for item in self.itinerary:
            total += item.get_cost
        return total
    
res = ItineraryReservation()
    
res.add(Hotel(200,1))
res.add(Hotel(200,1))

res.add(Flight(300)) 
res.add(Flight(300))    
res.add(Flight(300))    
res.add(Flight(300))    

print(res.get_cost) # 1600