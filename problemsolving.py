'''n=eval(input("enter the number:"))
if n>0:
    print("p")
elif(n<0):
    print("n")
else:
    print("zero")'''
'''n=int(input("enter the number: "))
if n%2==0:
    print("even number")
else:
    print("odd number")'''
'''n=int(input("enter the number: "))
if n%5==0:
    print("n divisble by 5")
else:
    print("not divisble by 5")'''
'''n=int(input("enter the number: "))
if n>=10:
    print("the given number greter than 10")
else:
    print("not greter than 10")'''
'''n1=int(input("enter the number: "))
n2=int(input("enter the number: "))
if n1> n2:
    print("n1 is greater than n2")
else:
    print("n2 is greater than n1")'''

'''n=['a','e','i','o','u']
char='u'
if char in n:
        print("vowel is present")
else:
        print("not present")'''
'''n=int(input("enter the number: "))
if 90<=n<=100:
    print("a grade")
elif(75<=n<=90):
    print("b grade")
elif(50<=n<=75):
    print(" c grade")
else:
    print("fail")'''
'''''n=input("type of the traingle:")
n1="All sides equal "
n2=" Two sides equal"
n3="All sides different"
if n==(n1):
    print("equilateral")
elif(n==n2):
    print("Isosceles ")
elif(n==n3):
    print("Scalene")
    pass'''
'''n=int(input("enter the number:"))
if n==1:
    print("monday")
elif(n==2):
    print("tuesday ")
elif(n==3):
    print("wednesday")
elif n==4:
    print("trauesday")
elif n==5:
    print("friday")
elif n==6:
    print("saturday")
elif n==7:
    print("sunday")'''
'''n=eval(input("enter the number: "))
if n<0:
    print("less than zero")
elif n==0:
    print("equal to o")
elif n<=100:
    print(" between 1 and 100")
elif n>100:
    print("greater than 100")'''
'''n=int(input("enter your choice"))
n1=10
n2=20
add=0
if n==1:
    print(n1+n2)
elif(n==2):
    print(n1-n2)
elif(n==3):
    print(n1*n2)
elif(n==4):
    print(n1//n2)'''
'''n=int(input("enter the number: "))
if 10<=n<70:
    print("true")
else:
    print("false")'''
'''n=int(input("enter the number:"))
n1=int(input("enter the number1: "))
n2=int(input("enter the number2"))
if n==1:
    print(n1+n2)
elif n==2:
    print(n1-n2)
elif n==3:
    print(n1*n2)
elif n==4:
    if n2!=0:
        print(n1//n2)
    else:
        print("can not divisble by zero:")
elif n==5:
    if n!=0:
        print(n1%n2)
    else:
        print("can not divisble by zero:")
else:
    print("invalid choice")'''
'''n1=int(input("enter the number1:"))
n2=int(input("enter the number2:"))
n3=int(input("enter the number3:"))
if n1>n2 and n1>n3:
    print("n1 is greater than n2 and n3")
elif n2>n1 and n2>n3:
    print("n2 is greater than n1 and n3")
else:
    print("n3 is grater than n1 and n2")'''
'''char=input("enter the character: ")
if char.isupper():
    print("upper case")
elif char.islower():
    print("lower case")
elif char.isdigit():
    print("digit")
else:
    print("specail symbols")
'''
'''year=int(input("enter the number: "))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("leap year")
        else:
            print("not leap year")
    else:
        print("leap year")
else:
    print("not leap year ")'''
'''for i in range(1,11):
    print(i)'''
'''for i in range(0,10,2):
    print(i)'''
'''for i in range(1,10,2):
    print(i)'''
'''for i in range(-10,0):
    print(i)'''
'''for i in range(-10,0,2):
    print(i)'''
'''n=int(input("enter the number:"))
for x in range(1,10):
    if n>x:
        break
        print(n)'''
 

    
'''sum=0
for i in range(10,20,2):
    sum=sum+i
print(sum)'''
'''n="vamshi"
for i in n:
    print(i)'''
'''username=input("enter the username")
password=int(input("enter the password"))
if username=="vamshi":
    if password==123456:
        print("registration succesfully completed")
    else:
        print("invalid data")
else:
    print("invalid data")'''
'''n=int(input("enter the numbeer: "))
for i in range(0,10):
    print(n,'*',i,'=',n*i)'''
'''for i in range(1,5):
    print("*"*i)'''
'''i=10
while i<20:
    print(i)
    i=i+2'''
'''name="vamshi"
count=0
for i in name:
    if i==i:
        count=count+1
print(count)'''
'''n=11
while n<=20:
    n=n+2
    print(n)'''
'''a=20
b=10
a=a-b
b=a+b
print(a,b)'''
'''primenumber = []

for i in range(2, 101):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        primenumber.append(i)

print(primenumber)'''
'''n=5
for i in range(n):
    print(i*" ",end="")
    for j in range(i,n):
        print("* ",end="")
    print()'''
'''n=5
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()'''
'''n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()'''
'''n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print("$",end=" ")
    print()'''
'''n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()'''
'''n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()'''
'''n=5
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print() '''
'''n=5
for i in range(n):
    for j in range(i,n):
        print("",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()'''
'''n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()'''
'''n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()'''
'''n=5
for i in range(n):
    for j in range(i,n):
        print("*",end=" ")
    print()'''
'''n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()'''
'''n=5
for i in range(n):
    for j in range(i,n):
        print("",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i,n-1):
        print("  ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()'''
'''n=5
for i in range(n):
    for j in range(i+1):
        print("",end=" ")
    for j in range(i,n):
        print(" *",end="")
    print()'''
'''n=5
for i in range(n):
    for j in range(i,n):
        print("",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        print("",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()'''
'''n=4
for i in range(n):
    for j in range(i+1):
        print("",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i+1):
        print("*",end=" ")
    print()'''
'''from array import*'''

'''a=array('i',[1,2,3,4,5])
a.append(5)
print(a)'''
'''a=array('i',[])
n=int(input("enter the length: "))
for i in range(n):
    x=int(input("enter the number: "))
    a.append(x)
print(a)'''
'''a=array("i",[])

n=int(input("enter the length:"))
for i in range(n):
    x=int(input("enter the number: "))
    a.append(x)
print(a)
s=int(input("search the value: "))
k=0
for e in a:
    if e==s:
        print(k)
        break
    k+=1
print(a.index())'''
'''arr=[1,2,3,4,5,6,7]
print(max(arr),min(arr))'''
'''arr=[1,2,3,4,5,6,7]
n=len(arr)
sum=0
avg=0
for i in arr:
    sum=sum+i
    avg=sum/n
print(sum,avg)'''
'''arr=[1,2,3,4,5,6,7]
even=0
odd=0
for i in arr:
    if i%2==0:
        even=even+1
    else:
        odd+=1
print("even",even)
print("odd",odd)'''
'''arr=[1,2,3,4,5,6,7]
arr.reverse()
print(arr)'''
''''n=int(input("enter the number: "))
arr1=array('i',[1,2,3,4,5,6,7])
for i in arr1:
   if i==n:
    print("the number is present")
    break
else:
    print("not present ")'''
'''arr1=array('i',[1,2,3,4,5,6,7])
print(arr1[-2])'''
'''arr1=array('i',[1,2,-3,4,5,-6,7])
for i in arr1:
    if i<0:
        print(i)'''
'''arr1=array('i',[1,2,-3,4,5,-6,7,7,2,3])
arr2=array('i',[1,2,-3,4,5,-6,7,7,2,3])
arr3=array('i',[])
for i in arr1:
    for j in arr1:
        arr3.append(i+j)
        break
print(arr3)'''
'''arr1=array('i',[1,2,-3,4,5,-6,7,7,2,3])
c=set()
uniqueelement=array('i',[])
for i in arr1:
    if i not in c:
        c.add(i)
        uniqueelement.append(i)
print(uniqueelement)'''
'''arr1=array('i',[1,2,3,4,5,6,7,7,2,3])
count=0
for i in arr1:
    if i in arr1:
        count=count+1
print(i,count)'''
'''def hello(a,b,c):
    return a+b+c
print(hello(10,20,20))'''
'''arr1=array('i',[1,2,3,4,5,6,7,8])
freq={}
for i in arr1:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
for key in freq:
    print("frequency",{key},"appears",{freq[key]},"times")'''
'''arr=array('i',[1,2,3,4,5,6,7])
k=int(input("enter the k times: "))
rotate=arr[k:]+arr[:k]
print(rotate)'''
'''arr=array('i',[1,2,3,4,5,6,7])
k=int(input("enter the number:"))
rotate=arr[-k:]+arr[:-k]
print(rotate)'''
'''arr=array('i',[1,2,-1,4,5,-2,7])
product=sorted(arr)

for i in product:
    n=product[0]*product[1]
    m=product[-1]*product[-2]
k=max(n,m)
print(k)'''
'''arr1=array('i',[1,2,-1,4,5,-2,7])
if arr1==arr1[::-1]:
    print("palindrome")
else:
    print("not palindrome")
'''
'''arr1=array('i',[1,2,-1,4,5,2,7,7])
arr2=array('i',[1,2,3,4,5,6,7])
common=set()
for i in arr1:
    for j in arr2:
        if i==j:
            common.add(i)
print(common)'''
'''arr2=array('i',[1,0,3,4,0,0,7])
for i in arr2:
    if i==0:
        arr2.remove(i)
        arr2.append(i)
print(arr2)'''
'''def add(a,b):
    return a+b
#print(add(20,30))
print(add(b=30,a=20))'''
'''def name():
    return "Hello"
print(name(),"Alice!")'''

'''def square():
    return 5**2
print(square())'''
'''def check_even_odd():
    if 7%2==0:
        return "even"
    else:
        return "odd"
print(check_even_odd())'''
'''def list_of_numbers(a=1,b=5,c=8):
    if a>b and a>c:
        return a
    elif b>c and b>a:
        return b
    else:
        return c
print(list_of_numbers())'''
'''n="10 20 30 40".split()
c=map(int,n)
print(list(c))'''
'''input="user@example.com"
word=input.split('@')
print(word[1])'''
'''input="jhon,25,new york"
words=input.split(",",1)
print(list(words))'''
'''input="doe,jhon"
word=input.split(',')
output=word[1]+" "+word[0].strip()
print(output)'''
'''s="  vamshi#  "
c=s.rstrip()
print(c)'''
# n=int(input("Enter the year: "))
# product_cost=2000
# discount1=20/100*product_cost
# final_if_laep_year=product_cost-discount1
# discount2=10/100*product_cost
# final_if_not_laep_year=product_cost-discount2
# if (n%4==0 and n%100!=0) or (n%400==0):
#     print(f"leap year thats why we are giving 20% discount :{final_if_laep_year}")
# else:
#     print(f"not leap year thats why we are giving 10% discount :{final_if_not_laep_year}")

# import copy
# s={a: 1, b: {c: 2}}
# k=copy.deepcopy(s)
# print(k)
# def vamshi(a,store=""):
#     dici={}
#     for i,j in a.items():
#         k=f"{store}.{i}" if store else i
#         if isinstance(j,dict):
#             dici.update(vamshi(j,k  ))
#         else:
#             dici[k]=j
#     return dici
# li={'a': {'b': {'c': 1}}}
# print(vamshi(li))

# Largest ,smallest ,second smallest ,second largest ,third smallest ,third largest in an array
# li=[1,3,4,6,89,8,4,9,10]
# max_val=float('-inf')
# sec_max=0
# third_max=0
# for i in li:
#     if i>max_val:
#         print(i)



# for i in li:
#     if max_val<i:
#         sec_max=max_val
#         max_val=i
#     else:
#         if sec_max<max_val and i>sec_max:
#             third_max=sec_max
#             sec_max=i
#         else:
#             if third_max<sec_max and i>third_max:
#                 third_max=i
# print(sec_max)
# print(third_max)




import logging
logging.basicConfig(
    filename='app.log',
    level='INFO',
    format="%(asctime)s-%(levelname)s-%(message)s"
)
logging.debug("started")
a=int(input("enter the number a:"))
b=int(input("enter the number b:"))
op=input("enter the operator:")
if(op=='+'):
    print(a+b)
    logging.info("sucessfully ")
elif(op=='/'):
    try:
        c=a/b
    except:
        logging.warning("division by 0 Error")
else:
    logging.critical("invalid operator")