#Find all vowels in the string "chaitanya"
'''name="chaitanya"
vowels=['a','e','i','o','u']
for i in name:
    if i in vowels:
        print(i,end=' ,')'''
#Find how many times the letter 'a' appears in "banana"
'''name="banana"
count=0
for i in name:
    if i=='a':
        count=count+1
print(count)'''
#Print all the characters in "education" that are not vowels
'''name="education"
vowels=['a','e','i','o','u']
for i in name:
    if i not in vowels:
        print(i,end=' ')'''
#Count how many times each character appears in "mississippi"
'''name="mississippi"
name1=set(name)
for i in name1:
    print(i,name.count(i))'''
#Print all characters at even indexes from "developer"
'''name="developer"
i=0
while i<len(name):
    if i%2==0:
        print(name[i])
    i+=1'''
#Check if the character 'z' is present in "amazing"
'''name= "amazing"
for i in name:
    if i in 'z':
        print("present")
        break'''
#Print all characters of "programming" that appear more than once
'''name="programming"
for i in name:
    count=0
    if i.count()<2:
        print(i)'''
#Replace all 'a' with '*' in "banana"
'''s="banana"
print(s.replace('a','*'))'''
#Remove all vowels from "chaitanya" and print the result
'''name="chaitanya"
vowels=['a','e','i','o','u']
for i in name:
    if i not in vowels:
        print(i)'''
# class car:
#     def __init__(self,input_color):
#         self.color=input_color
#     def start(self):
#         print("car start")
#     def color_change(self,input_color):
#         self.color=input_color
#         print("color change")
# h1=car("red")
# h2=car("black")
# h3=car("pink")
# h3.color_change("orege")
# # h3.color="orege"
# print(h3.color_change)
# class grand:
#     def k(self):
#         print("i am thata")
# class son(grand):
#     def m(self):
#         print("k is is my father")
# class child(son):
#     def v(self):
#         print("i am your child")
# d1=child()
# d1.k()
# print(child.mro())
# class grand:
#     def k(self):
#         print("i am thata")
#     def m(self):
#         print("iam not thata")
    
# class son:
#     def m(self):
#         print("k is is my father")
# class child(grand,son):
#     def v(self):
#         print("i am your child")
# d1=child()
# d1.m()
# print(child.mro())
# def vam(a,b):
#     return a+b
# def vam(a,b,c):
#     return a+b+c
# def vam(a,b,c,d):
#     return a+b+c+d
# vam(1,2)
# vam(1,2,3)
# print(8>9)

# class bankAccount:
#     def __init__(self,acc_num,acc_balance):
#         self.acc_num=acc_num
#         self.__acc_balance=acc_balance
#     def get_balance(self):
#         return self.__acc_balance
#     def set_balance(self,new):
#         self.__acc_balance=new
#         return self.__acc_balance
    
# b1=bankAccount("798",879)
# b2=bankAccount("809",908)
# b1.set_balance(10000)
# print(b1.get_balance())

# class parent1:
#     def a(self):
#         print("i am the parent1")
# class parent2:
#     def b(self):
#         print("i am the parent2")
#     def a(self):
#         print("i am the duplicate")
# class child(parent2,parent1):
#     pass
# ch=child()
# ch.a()
# nums = [-4,-1,0,3,10]
# li=[]
# for i in nums:
#     li.append(i**2)
# li.sort()
# print(li)
# li=[i**2 for i in nums]
# li.sort()
# print(li)
# s = "ca"
# s = "cabaabac"
# k=list(s)
# # s = "ca"
# k1=len(k)//2
# l=0
# r=len(k)
# for i in range(k1-1):
#     if k[i]==k[i+1]:
#         k.pop(0)
#     if k[0]==k[-1]:
#         k.pop(-1)
#         k.pop(0)
# print(k)
# print(len(k))
# haystack ="sadbutsad"
# needle = "sad"
# li=[]
# for i in range(len(haystack)-len(needle)+1):
#     k=""
#     for j in range(len(needle)):
#         k+=haystack[i+j]
#     li.append(k)
# print(li)
# l1=[1,3,4,2,4,6]
# l2=[10,9,0,2,3,4,2]
# l=set()
# n=len(l1)
# for i in l1:
#     for j in l2:
#         if i<j:
#             l.add(i)
#     for k in l2:
#         if j<i:
#             l.add(k)
# print(list(l))
# s = "a#b%*"
# s = "z*#"
# s="p##"
# result=[]
# l=""
# for i in s:
#     if i.isalpha():
#         result.append(i)
#         k=result[-1]
#     elif(i=="%"):
#         result.reverse()
#     elif(i=="#"):
#         result.append(k)
#     elif(i=="*"):
#         result.pop()
#     if len(result)==0:
#         k=""
# for j in result:
#     l+=j
# print(l)
# arr=[1,2,3,3,4,5]
# t=4
# for i in range(len(arr)):
#     if t==arr[i]:
#         print(i)
#         break 

# def rec(i,count):
#     if i==0:
#         return
#     if arr[i]==t:
#         count+=1
#         return count
#     return rec(i-1,count)
# t=3
# arr=[1,1,2,3,3,4,5]
# # count=0
# print(rec(len(arr)-1,1))
# def first(arr,target):
#     l=0
#     right=len(arr)-1
#     result=-1
#     while l<=right:
#         mid=(l+right)//2
#         if arr[mid]==target:
#             result=mid
#             right=mid-1
#         elif(arr[mid]<target):
#             l=mid+1
#         else:
#             right=mid-1
#     return result
# def second(arr,target):
#     l=0
#     right=len(arr)-1
#     result=-1
#     while l<=right:
#         mid=(l+right)//2
#         if arr[mid]==target:
#             result=mid
#             l=mid+1
#         elif(arr[mid]<target):
#             l=mid+1
#         else:
#             right=mid-1
#     return result
# arr = [1, 2, 3, 3, 3, 4, 5]
# target = 3
# f=first(arr,target)
# s=second(arr,target)
# print(s-f+1)
# word = "abbcccc"
# word = "abcd"
# word ="ere"
# d={}
# l=1
# for i in word:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# print(d)
# for j in d:
#     l+=d[j]-1
# print(l)
# import copy
# l=[1,2,3,4,5]
# l2=copy.deepcopy(l)
# l2.append(89)
# print(l2)
# print(l)


# import copy
# k=[12,34,56,78]
# k2=copy.copy(k)
# k2.append(687)
# k2.remove(12)
# print(k2)
# print(k)

# f=open("print(3+5).py",mode='r')
# # print(f.read())
# print(f.read(19))
# print(f.readline())
# print(f.readlines())
# f=open("vam.py",mode='w')
# f.write()
# f=open("vam.py",mode='x')
# f.write("vamshi")


# with open('insta.jpg',mode='rb') as f:
#     data=f.read()
# with open('vamshi.png',mode='wb') as f:
#     f.write(data)



import mysql.connector

con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vamshi@19",
    database="student_db"
)

cur=con.cursor()


# sql="update  employees set dept=%s where dept=%s"
sql="delete from employees where  emp_id=%s"
val=(1,)
cur.execute(sql,val)
con.commit()
print(cur.rowcount, "record inserted.")
print("Inserted ID:", cur.lastrowid) 