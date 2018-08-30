#remember to implement as Abstract Class
from abc import ABC, abstractmethod

class Car(ABC):
    @abstractmethod
    def compute_fee():
        pass

class small_car(Car):
      def __init__(self,registration,model,car_ID):
         self._car_id = car_ID
         self._registration = registration
         self._model = model
         self._daily_fee = 1
      def compute_fee(self):
        return self._daily_fee

class medium_car(Car):
    def __init__(self,registration,model,car_ID):
         self._car_id = car_ID
         self._registration = registration
         self._model = model
         self._daily_fee = 2
    def compute_fee(self):
        return self._daily_fee
        
class large_car(Car):
    def __init__(self,registration,model,car_ID):
         self._car_id = car_ID
         self._registration = registration
         self._model = model
         self._daily_fee = 3
    def compute_fee(self):
        return self._daily_fee


class premium_car(Car):
    def __init__(self,registration,model,car_ID):
         self._car_id = car_ID
         self._registration = registration
         self._model = model
         self._daily_fee = 4
    def compute_fee(self):
        return self._daily_fee
