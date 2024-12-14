from abc import ABC,abstractmethod
class Person_Shape(ABC):
    @abstractmethod
    def __init__(self,person_name):
        self.persons_names = person_name
        pass
    
# Developer Function Below:
# System_Connection:
from person import*
#--------------------------------
class Person(Person_Shape):
    def __init__(self, person_name):
        super().__init__(person_name)
        
