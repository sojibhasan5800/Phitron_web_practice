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
        self.__student_roll =None
        self.student_mark={}
        self.student_sub_grade={}
        self.final_grade=None

    
    def calculate_final_grade(self):
        sum=0
        for grade in self.student_sub_grade.values():
            point = School.grade_to_value(grade)
            sum+=point
        if sum==0:
            gpa=0.00
            self.final_grade='F'
        else:
            gpa = sum / len(self.student_sub_grade)
            self.final_grade = School.value_to_grade(gpa)
        return f"{self.student_names} Final Grade : {self.final_grade} with GPA = {gpa}"
        
    def set_student_id(self):
        self.__student_id =  recive_id_student()
    @property
    def get_student_roll(self):
        return self.__student_id
    @get_student_roll.setter
    def get_student_roll(self,roll_no):
        self.__student_roll= roll_no

    
    


       
