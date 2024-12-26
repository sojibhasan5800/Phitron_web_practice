from abc import ABC,abstractmethod
from ride_sys.rides import rideRequest,rideMatching
class forces(ABC):
    
    def __init__(self,name,email,number):
        self.__name=name
        self.__email =email
        self.__number = number
    @abstractmethod
    def display_profile(self):
        print(f"Name : {self.name} & Number : {self.__number}")
    
# For Rider -->:

class rider(forces):

    def __init__(self, name, email, number,current_location,intial_amount):
        super().__init__(name, email, number)
        self.current_location = current_location
        self.wallet = intial_amount
        self.current_ride=None

    def display_profile(self):
        print(f"Rider Name : {self.name} & Number : {self.__number}")
    
    def load_cash(self,amount):
        if amount >0:
            self.__wallet+=amount
        else:
            print(f"No Added! Place SirAmount are Added greater than 0")

    def update_location(self,update_current_location):
        self.current_location = update_current_location

    def request_ride(self, ride_sharing_cmp, destination, vehicle_type):
        ride_request = rideRequest(self, destination)
        ride_matching = rideMatching(ride_sharing_cmp.drivers)
        ride_fix = ride_matching.find_driver(ride_request, vehicle_type)
        ride_fix.rider = self
        self.current_ride = ride_fix
        print("YAY!! We got a ride")

    def show_current_ride(self):
        pass

# For Driver ---->:

class driver(forces):

    def __init__(self, name, email, number,current_location):
        super().__init__(name, email, number)
        self.current_location = current_location
        self.wallet = 0

    def display_profile(self):
        print(f"Driver Name : {self.name} & Number : {self.__number}")
    
    def accept_ride(self,ride_obj):
        ride_obj.start_ride()
        ride_obj.set_driver(self)
    
    def reach_destination(self, ride):
       ride.end_ride()

