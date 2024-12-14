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


# Developer Function Below:
# System_Connection:
import sys
import os
from teacher import Teachers

#--------------------------------

class School:
    def __init__(self,school_name,school_location):
        self.teachers={}
        self.classrooms={}
    
    
    @abstractmethod
    def add_classroom(self,classroom_obj):
        self.classrooms[self.class_name]=classroom_obj
        pass
    
    def add_teacher(self,teacher_obj):
        self.teachers[teacher_obj.teacher_id]=teacher_obj
        
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
    def get_teacher_obj(self):
        return self.teachers

def teacher_lst():
    
    
        