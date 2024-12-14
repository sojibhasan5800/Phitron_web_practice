
# Developer Function Below:
# System_Connection:
import sys
import os
import random
from school import School
#working_part

#--------------------------------
class common_data_get:
    teacher_id_number=set()
    student_id_number=set()
    def _generate_id(self,person_name="teacher"):
            """Generate a unique 4-digit ID."""
            if(person_name=="student"):
                  while True:
                    person_id = random.randint(100000,999999)
                    if person_id not in common_data_get.student_id_number:
                        common_data_get.student_id_number.add(person_id)
                        return person_id
            else:            
                while True:
                    person_id = random.randint(1000,9999)
                    if person_id not in common_data_get.teacher_id_number:
                        common_data_get.teacher_id_number.add(person_id)
                        return person_id
                    
    def daily_subjects(self,class_name):
    # Dictionary to store subjects for each class
        class_subjects = {
            "Six": ["Math", "Science", "English", "History"],
            "Seven": ["Math", "Biology", "English", "Geography"],
            "Eight": ["Math", "Physics", "English", "Civics"],
            "Nine": ["Advanced Math", "Chemistry", "English", "Economics"],
            "Ten": ["Advanced Math", "Physics", "English", "Accounting"]
        }
        
        return class_subjects[class_name]
                    


# send data :
def recive_id_teacher():
     id_number = common_data_get._generate_id(None)
     return id_number
def recive_id_student():
     id_number = common_data_get._generate_id(None,"student")
     return id_number
def recive_sub_list(class_name):
     sub_list=common_data_get.daily_subjects(None,class_name)
     return sub_list
     
                  

           

