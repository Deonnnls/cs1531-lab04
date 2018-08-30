from car import *
from admin import *
from admin_system import *
from customer import *
from booking import *
from insurance import *
from location import *
from rental_system import *

print("\n")
admin_1 = Admin("Steven","A001","iAmClaire","123456789")
print("Admin user name:",admin_1.get_user_name())
print("Admin password:",admin_1.get_pass_word())

AdminSystem = Admin_system()

AdminSystem.add_admin(admin_1)

print("password check:",AdminSystem.check_user_name("iAmClaire","123456789"))

print("\n")

print("The First Customer")
customer_1 = Customer("C001","abc","37","c1234567","abc123@gmail.com")
print("Customer ID:",customer_1.get_customer())
print("Customer Name:",customer_1.get_name())
print("Customer AgeL",customer_1.get_age())
print("Customer License:",customer_1.get_license())
print("Customer E-mail:",customer_1.get_email())

print("\n")

location_1 = Location("harbour bridge","darling harbour")
print("Pick up location:", location_1.get_pick_up())
print("Drop off location:", location_1.get_drop_off())

print("\n")

print("The Second Customer")
customer_2 = Customer("C002","Saber","44","c9999999","Saber666@gmail.com")
print("Customer ID:",customer_2.get_customer())
print("Customer Name:",customer_2.get_name())
print("Customer Age:",customer_2.get_age())
print("Customer License:",customer_2.get_license())
print("Customer E-mail:",customer_2.get_email())


print("\n")

location_2 = Location("The Star Sydney","The Crown Melbourne")
print("Pick up location:", location_2.get_pick_up())
print("Drop off location:", location_2.get_drop_off())



print("\n")

car_1 = small_car(1234,"TX5",514197)
car_2 = medium_car(5432,"Huracan",123456)
car_3 = large_car(8888, "Big",999000)
car_4 = premium_car(9999, "GloriousModel", 9988997766)

system_1 = rental_system()
booking_1 = booking(1, car_1, customer_1,"Somewhere", 12)
booking_2 = booking(2, car_2, customer_1,"25 Harbourne Road", 5)
booking_3 = booking(3, car_3, customer_1,"55 Central Park Avenue", 10)
booking_4 = booking(4, car_4, customer_2,"The Star Sydney", 14)

system_1.make_a_booking(booking_1)
system_1.make_a_booking(booking_2)
system_1.make_a_booking(booking_3)
system_1.make_a_booking(booking_4)

print("All the customer = " , system_1._customers)
print("All the bookings = " , system_1._bookings)
print("All the cars = ", system_1._cars)
print("All the unpaid = ", system_1._payment)

print("now let customer 2 (C002) pay")

system_1.accept_payment(customer_2.get_customer())

print("All the customer = " , system_1._customers)
print("All the bookings = " , system_1._bookings)
print("All the cars = ", system_1._cars)
print("All the unpaid = ", system_1._payment)

print("customer_2 (C002) has succesfully paid the booking")
