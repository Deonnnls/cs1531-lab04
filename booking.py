from customer import *
from car import *

class booking():
    def __init__(self, booking_ID, car, customer,location, period):
        self._booking_ID = booking_ID
        self._customer_ID = customer.customer_ID
        self._car_ID = car._car_id
        self._pickup_location = location
        #self._insurance = insurance
        self._period = period
        self._netprice = self._period * car._daily_fee
        #add self.bookingtime

    def get_netprice(self):
        return self.netprice
