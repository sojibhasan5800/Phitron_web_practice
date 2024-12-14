from abc import ABC,abstractmethod
class Teachers_Shape(ABC):
    @abstractmethod
    def __init__(self,teacher_name):
         #this name are inharite from person
        self.teacher_names = teacher_name
    @abstractmethod
    def teach(self):
        pass
    def evaluate_exam(self):
        pass

# Developer Function Below:
# System_Connection:
from person import Person
from private_connection_class import recive_id_teacher
import random
#--------------------------------
class Teachers(Teachers_Shape):
    
    def __init__(self, teacher_name):
        self.teacher_names= Person(teacher_name)
        self.teacher_teaches_sub=[]
        self.teacher_id = recive_id_teacher()
    def teach(self,*sub):
        #Not working
        for subject in sub:
            self.teacher_teaches_sub.append(subject)
        pass
    def evaluate_exam(self):
        get_random_subMark = random.randint(30,100)
        return get_random_subMark
    

        

        
        
