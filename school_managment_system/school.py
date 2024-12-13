from abc import ABC,abstractmethod
class school_Shape(ABC):
    @abstractmethod
    def __init__(self,school_name,school_location):
         self.school_name = school_name
         self.school_location = school_location
         pass
    @abstractmethod
    def add_classroom(self):
        pass
    @abstractmethod
    def add_teacher(self):
        pass
    @abstractmethod
    def student_admission(self):
        pass
    @abstractmethod
    def calculate_grade(self):
        pass
    @abstractmethod
    def grade_to_value(self):
        pass
    @abstractmethod
    def value_to_grade(self):
        pass
    @abstractmethod
    def __repr__(self):
        pass
class School:
    def __init__(self,school_name,school_location):
        self.teachers={}
        self.classrooms={}
    

    
        