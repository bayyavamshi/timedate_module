# Inheritance: Create a base class Person with attributes name and email. Derive
# classes Student and Teacher. Person should be an abstract class with fields name
# and id. It should have an abstract method return_role.
# ○ Should return ‘Student’ for student class
# ○ Should return ‘Teacher’ for teacher class

# from abc import ABC,abstractmethod
# class person(ABC):
#     def __init__(self,name,pid):
#         self.name=name
#         self.id=pid
#     @abstractmethod
#     def return_role(self):
#         pass
# class student(person):
#     def __init__(self, name, pid,course):
#         super().__init__(name, pid)
#         self.course=course
#     def return_role(self):
#         return 'student'
#     def display(self):
#         print(self.name,self.id,self.course)
# class teacher(person):
#     def __init__(self, name, pid,subject):
#         super().__init__(name, pid)
#         self.subject=subject
#     def return_role(self):
#         return "teacher"
#     def display(self):
#         print(self.name,self.id,self.subject)
# obj1=teacher("vamshi",898,'ece')
# obj1.display()

# class A:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         return self.a+self.b
#     def shiva(self):
#         print('i am shiva')
#     def raju(self):
#         print('i am raju')
# class B(A):
#     def __init__(self, a, b,c):
#         super().__init__(a, b)
#         self.c=c

#     def vam(self):
#         print('i am vamshi')
#     def raju(self):
#         super().raju()
#         print('i am child raju')
#     def add(self):
        
#         return self.a+self.b+self.c
# class c(B,A):
#     def mani(self):
#         print('i am mani')
# h1=c(2,3,3)
# print(h1.add())

# class Car:
#     def __init__(self,name,car_number):
#         self.name=name
#         self.__car_number=car_number
#     def seter(self,new_number):
#         self.__car_number=new_number
#         return self.__car_number
#     def geter(self):
#         return self.name,self.__car_number
# h1=Car('tata',1234)
# print(h1.geter())
# print(h1.seter('6789'))

# from abc import ABC,abstractmethod
# class Car(ABC):
#     @abstractmethod
#     def car_name(self):
#         pass
#     @abstractmethod
#     def car_number(self):
#         return 123
# class vam(Car):
#     def car_name(self):
#         print('vamshi anna car')
#     def car_number(self):
#         return super().car_number()
# h1=vam()
# h1.car_name()


# arr=['flower','flex','floor']
# k=arr[0]
# iso=True
# while len(k)>0:
#     for i in arr[1:]:
#         k=arr[:-1]
#         if i.startswith(k):
#             iso=True
# print(k)

# from abc import ABC,abstractmethod
# class greet(ABC):
#     @abstractmethod
#     def check_balance(self):
#         pass
#     @abstractmethod
#     def bank_name(self):
#         return 'vamshi bank'
# class A(greet):
#     def check_balance(self):
#         print('your balance is good')
#     def bank_name(self):
#         return super().bank_name()
# h=A()
# print(h.bank_name())


# arr=['flower','flex','floor']
# first_val=arr[0]
# n=len(first_val)
# iso=True
# while n>0:
#     for i in arr[1:]:
#         first_val=first_val[:-1]
#         if i.startswith(first_val):
#             iso=True
# print(first_val)
