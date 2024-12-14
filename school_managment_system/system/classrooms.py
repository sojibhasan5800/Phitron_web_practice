from abc import ABC,abstractmethod
class Classroms_Shape(ABC):
    @abstractmethod
    def __init__(self,class_name):
       pass
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
from private_connection_class import recive_sub_list
#--------------------------------

class Classrooms(Classroms_Shape):
    def __init__(self, class_name):
        self.class_names = class_name
        self.class_subjects= []
        self.class_students=[]
   
    def add_student(self,student_obj):
        student_cls_details = f"Name : {student_obj.student_names} 
                                Roll_No : {len(self.class_students)+1} Class :{self.class_names} "
                               
                                
                                

                                        
    
    def add_subject(self):
        for subjects in recive_sub_list(self.class_names):
            self.class_subjects.append(subjects)

        
        