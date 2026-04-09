# from abc import ABC,abstractmethod
# class paybills(ABC):
#     @abstractmethod
#     def pay(self,amount):
#         pass
#     def details(self):
#         print("abstract method is created")
# class upipay(paybills):
#     def pay(self,amount):
#         print(amount,"total bill is payed")
# class internet(paybills):
#     def pay(self,amount):
#         print(amount,"total bill is payed")
# h1=internet()
# h1.pay(89)

# from abc import ABC,abstractmethod
# class vehicle(ABC):
#     @abstractmethod
#     def mileage(self):
#         pass
#     @abstractmethod
#     def fuelcapacity(self):
#         pass
#     def vamshi(self):
#         print("kudhkskd")

# class car(vehicle):
#     def mileage(self):
#         print("mileage is 20km/hr")
#     def fuelcapacity(self):
#         print("fuel capacity is 40ltr")
# c1=car()
# c1.mileage()
# c1.fuelcapacity()

# from abc import ABC,abstractmethod
# class car(ABC):
#     @abstractmethod
#     def car_number(self):
#         pass
# class vam_car(car):
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         return self.a+self.b
#     def car_number(self):
#         return "12345"
# h=vam_car(1,3)
# print(h.add())
# print(h.car_number())


# from abc import ABC,abstractmethod
# class car(ABC):
#     @abstractmethod
#     def car1(self):
#         pass
# class car2(car):
#     def car1(self):
#         return "TATA"
# h1=car2()
# print(h1.car1())

# class A:
#     def dog(self):
#         return 'bow bow'
#     def cat(self):
#         return 'meow meow'

# class C:
#     def dog(self):
#         return 'yadav'
    
# class B(C,A):
#     def cat(self):
#         return 'vamshi yadav'

# h1=B()
# print(h1.dog())

# class A:
#     def __init__(self,name,rollNumber):
#         self.name=name
#         self.rollNumber=rollNumber
#     def dog(self):
#         return 'bow bow'
#     def cat(self):
#         return 'meow meow'

# class C(A):
#     def __init__(self, name, rollNumber,section):
#         super().__init__(name, rollNumber)
#         self.section=section
#     def details(self):
#         return self.rollNumber
# h1=C('vamshi',1234,'A')
# print(h1.details())

class car:
    def __init__(self,carName,carRollNumber,carPrice):
        self.__carName=carName
        self.carRollNumber=carRollNumber
        self._carPrice=carPrice

    def geter(self):
        return self.carName,self.carRollNumber,self.carPrice
    
    def seter(self,new_car_price):
        self.carPrice=new_car_price
        return self.__carName
h1=car('TATA',1234,99999)
print(h1.seter(5555))
print(h1._carPrice)
# print(h1.__carName)
# print(h1.geter())
# print(h1.seter(20000))
# print(h1.geter())


    
    