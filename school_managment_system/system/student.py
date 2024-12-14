from abc import ABC,abstractmethod
class Studnets_Shape(ABC):
    @abstractmethod
    def __init__(self,student_name,student_classroom,student_mark,student_SubGrade,grade):
        pass
    @abstractmethod
    def calculate_final_grade(self):
        pass
    @abstractmethod
    def student_id(self):
        #getter_setter_use
        pass

       
