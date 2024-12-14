from abc import ABC,abstractmethod
class Studnets_Shape(ABC):
    @abstractmethod
    def __init__(self,student_name):
        pass
    @abstractmethod
    def calculate_final_grade(self):
        pass
    @abstractmethod
    def student_id(self):
        #getter_setter_use
        pass


# Developer Function Below:
# System_Connection:
import sys
import os
import random
from school import School
from person import Person
from private_connection_class import recive_id_student
#working_part

#--------------------------------
class Student(Studnets_Shape):
    def __init__(self, student_name,classroom_obj):
        self.student_names =  Person(student_name)
        self.classrooms = classroom_obj
        self.__student_id= None
        self.student_mark={}
        self.student_sub_grade={}
        self.final_grade=None

    
    def calculate_final_grade(self):
        #WK
        pass
    @property
    def get_student_id(self):
        return self.__student_id
    @get_student_id.setter
    def get_student_id(self):
        self.__student_id= recive_id_student()

    
    


       
