from datetime import datetime
import sys
import os
from vechicle_sys.vechicles import Car,Bike

class rideSharing_company:
     def __init__(self, company_name) :
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rides = []
     def add_rider(self, rider_obj):
         self.riders.append(rider_obj)
     def add_driver(self, driver_obj):
         self.drivers.append(driver_obj)
     def __str__(self):
         return f"Company Name {self.company_name} with riders : {len(self.riders)} and Drivers : {len(self.drivers)}"
    
class ride:
    def __init__(self,start_location,end_location,vechile_obj):
        self.__start_location = start_location
        self.__end_location = end_location
        self.vechile = vechile_obj
        self.driver = None
        self.rider = None
        self.start_tiem = None
        self.end_tiem = None
        self.estimated_fare = self.calculate_fare(vechile_obj.vehicle_type)

    
    def set_driver(self,driver_obj):
        self.driver= driver_obj

    def start_ride(self):
        self.start_tiem = datetime.now()

    def end_ride(self):
        self.end_tiem = datetime.now()
        self.rider.wallet -= self.estimated_fare
        self.driver.wallet+= self.estimated_fare

    def calculate_fare(self, vehicle):
        print(vehicle)
        distance = 10
        fare_per_km = {
            'car' : 30,
            'bike' : 20,
            'cng' : 25
        }
        return distance*fare_per_km.get(vehicle)


    def __repr__(self):
        return f"Ride details : Started Location{self.start_tiem} to Ended Location {self.end_tiem} Total Time Spend{self.end_tiem-self.start_tiem}"
         
        
    
class rideRequest:
    def __init__(self,rider_obj,end_location):
        self.rider = rider_obj
        self.end_location = end_location
    
class rideMatching:
    def __init__(self, drivers_lst) -> None:
        self.available_drivers = drivers_lst

    def find_driver(self, rideRequest_obj, vehicle_type):
        if len(self.available_drivers) > 0:
            print("Looking for drivers.....")
            driver = self.available_drivers[0]
            
            if vehicle_type == 'car':
                vechicle_obj = Car('car', "ABC456", 30)
            elif vehicle_type == 'bike':
                vechicle_obj = Bike("bike", "1234BH", 50)
            
            ride_process = ride(rideRequest_obj.rider.current_location,rideRequest_obj
                                .end_location,vechicle_obj)
            driver.accept_ride(ride_process)
            return ride_process
    
