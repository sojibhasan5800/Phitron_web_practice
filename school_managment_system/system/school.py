from abc import ABC,abstractmethod
class school_Shape(ABC):
    @abstractmethod
    def __init__(self,school_name,school_location):
         
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
    def calculate_grade(value):
        pass
    @abstractmethod
    def grade_to_value(grade):
        pass
    @abstractmethod
    def value_to_grade(gpa):
        pass
    @abstractmethod
    def __repr__(self):
        pass


# Developer Function Below:
# System_Connection:




#--------------------------------

class School:
    def __init__(self,school_name,school_location):
        self.school_name = school_name
        self.school_location = school_location
        self.teachers={}
        self.classrooms={}
    
    
    
    def add_classroom(self,classroom_obj):
        self.classrooms[classroom_obj.class_name]=classroom_obj
        pass
    
    def add_teacher(self,teacher_obj):
        self.teachers[teacher_obj.teacher_id]=teacher_obj
        
    
    def student_admission(self,student_obj):
        class_name = student_obj.classrooms.class_name
        self.classrooms[class_name].add_student(student_obj)
    @staticmethod
    def calculate_grade(marks):
          
        if marks>=80 and marks<=100:
            return 'A+'
        elif marks >= 70 and marks<80:
            return 'A'
        elif marks >= 60 and marks <70:
            return 'A-'
        elif marks >= 50 and marks <60:
            return 'B'
        elif marks >= 40 and marks < 50:
            return 'C'
        elif marks >= 33 and marks < 40:
            return 'D'
        else:
            return 'F'
  
      
    @staticmethod
    def grade_to_value(grade):
        grade_map = {
            'A+' : 5.00,
            'A' : 4.00,
            'A-' : 3.50,
            'B' : 3.00,
            'C' : 2.00,
            'D' : 1.00,
            'F' : 0.00
        }
        return grade_map[grade]
    
    @staticmethod
    def value_to_grade(value):
        if value >=4.5 and value<=5.00:
            return 'A+'
        elif value >= 3.5 and value <4.50:
            return 'A'
        elif value >= 3.0 and value < 3.5:
            return 'A-'
        elif value >= 2.5 and value < 3.0:
            return 'B'
        elif value >= 2.0 and value < 2.5:
            return 'C'
        elif value >= 1.0 and value < 2.0:
            return 'D'
        else:
            return 'F'
    
    def __repr__(self):
        pass
    


    
    
        