# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 12:16:22 2023

@author: lufer
"""

import random


class Student:
    
    courseCounts = {}
    courseStats = {}
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.examList = {}
        self.courseNames = {}
        
    def takeExam(self, exam):
        grade = random.randint(1,5)
        self.examList[exam.course] = grade
        if exam.course in Student.courseCounts:
           Student.courseCounts[exam.course] += 1
           Student.courseStats[exam.course] += grade
        else:
            Student.courseCounts[exam.course] = 1
            Student.courseStats[exam.course] = grade
class Exam:
    def __init__(self, course):
        self.course = course
        
    def stats(self):
        average = Student.courseStats[self.course] / Student.courseCounts[self.course]
        print(f"{self.course} exam was taken by {Student.courseCounts[self.course]} students. Average score = {average}")
    
    
class University:
    def __init__(self, uni):
        self.uni = uni
        self.students = {} 
        
    def enroll(self, student):
        self.students[student.name] = student.examList
        
    def stats(self):
        for key,value in self.students.items():
            print(f"{key} took {len(value)} exams")
            for k,v in value.items():
                print(f"\t Got {v} in {k}")
        
            

s1= Student ("Sandy", "24.01.1992") # name, dob
s2= Student ("Spili", "14.10.1993") # name, dob
s3= Student ("Waile", "04.06.1994")


imc = University("FH Krems")

imc.enroll(s1)
imc.enroll(s2)
imc.enroll(s3)

e1 = Exam("ProgrammingII")
e2 = Exam("Software Eng")
e3 = Exam("Creativity")

s1.takeExam(e1)
s2.takeExam (e1)
s3.takeExam (e1)

s1.takeExam (e2)
s2.takeExam (e2)

s1.takeExam (e3)
s3.takeExam (e3)

imc.stats()

e1.stats()
e2.stats()
e3.stats()



# =============================================================================
# print(s1.name)
# 
# imc= University ("FH Krems")
# 
# imc.enroll(s1)
# imc.enroll(s2)
# imc.enroll(s2)
# imc.enroll(s3)
# 
# e1 = Exam("ProgrammingII")
# e2 = Exam("Software Eng")
# e3 = Exam("Creativity")
# 
# # assign a random value as grade
# 
# s1.takeExam (e1)
# s2.takeExam (e1)
# s3.takeExam (e1)
# 
# s1.takeExam (e2)
# s2.takeExam (e2)
# 
# s1.takeExam (e3)
# s3.takeExam (e3)
# 
# # printstatistics
# imc.stats()
# =============================================================================
