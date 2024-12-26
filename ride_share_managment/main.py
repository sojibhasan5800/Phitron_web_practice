import sys
import os
sys.path.append(r"Phitron_web_practice/ride_share_managment")

from ride_sys.rides import ride,rideRequest,rideMatching,rideSharing_company
from users_sys.users import rider,driver
from vechicle_sys.vechicles import Car,Bike

niye_jao = rideSharing_company("Niye Jao")
rahim = rider("Rahim Uddin", "rahim@gmail.com", 1234, "Mohakhali", 1200)
niye_jao.add_rider(rahim)
kolimuddin = driver("Kolim Uddin", "kolim@gmail.com", 1256, "Gulshan")
niye_jao.add_driver(kolimuddin)
rahim.request_ride(niye_jao, "Uttara", "car")
kolimuddin.reach_destination(rahim.current_ride)
rahim.show_current_ride()
# print(niye_jao)
print("kk")
print("kk")
print("kksadfa")
print("kksadfa")