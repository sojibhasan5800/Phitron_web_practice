from abc import ABC,abstractmethod
class Classroms_Shape(ABC):
    @abstractmethod
    def __init__(self,class_name,student_obj):
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
import sys
import os

from private_connection_class import recive_sub_list

#--------------------------------

class Classrooms(Classroms_Shape):
    def __init__(self, class_name):
        self.class_names = class_name
        self.class_students_info=[]
        self.class_subjects= []
        self.student_cls_subjects= []
   
    def add_student(self,student_obj):
        student_obj.set_student_id()
        student_obj.get_student_roll = (len(self.class_students)+1)
        student_cls_details = f"Student_Id : {student_obj.get_student_id()} Name : {student_obj.student_names} Roll_No : {student_obj.get_student_roll()} Class :{self.class_names} "
        self.class_students_info.append(student_cls_details)
                                        
    
    def add_cls_subject(self):
        for subjects in recive_sub_list(self.class_names):
            self.class_subjects.append(subjects)
    

    def add_cls_student_subject(self,subject_obj):
        self.student_cls_subjects.append(subject_obj)
    
    def take_semester_final(self):
        for subject in self.student_cls_subjects:
            subject.exam(self.class_students_info)

        for student in self.class_students_info:
            student.calculate_final_grade()

        
        