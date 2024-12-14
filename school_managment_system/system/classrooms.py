from abc import ABC,abstractmethod
class Classroms_Shape(ABC):
    @abstractmethod
    def __init__(self,class_name):
        self.class_names = class_name
        self.class_subjects= []
        self.class_students=[]
    @abstractmethod
    def add_student(self):
        pass
    @abstractmethod
    def add_subject(self):
        pass
    @abstractmethod
    def take_semester_final(self):
        pass
    @abstractmethod
    def get_top_students(self):
        pass

# Developer Function Below:
# System_Connection:

#--------------------------------

class Classrooms(Classroms_Shape):
    def __init__(self, class_name):
        self.class_names = class_name
        self.class_subjects= []
        self.class_students=[]
   
    def add_student(self):
        pass
    
    def add_subject(self):
        
        