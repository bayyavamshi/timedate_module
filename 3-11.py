import decimal
# integer = 10.30
# string = '12345'
# print(decimal.Decimal(string))
# print(type(decimal.Decimal(string)))


# vowel = ['a', 'e', 'i', 'o', 'u']
# word = "programming"
# count=0
# for i in word:
#     if i not in vowel:
#         count+=1
# print(count)

# word = "python"
# character = "p"
# count=0
# for i in word:
#     if i==character:
#         count+=1
# print(count)

# fib = [0,1]
# for i in range(5):
#     fib.append(fib[-2]+fib[-1])
# print(" ".join(str(e) for e in fib))


# numberList = [15, 85, 35, 89, 125,2]
# max_num=numberList[0]
# for i in numberList:
#     if max_num>i:
#         max_num=i
# print(max_num)


# numList = [1, 2, 3, 4, 5]
# print(numList[len(numList)//2])


# lst = ["P", "Y", "T", "H", "O", "N"]
# print("".join(lst))


# lst1 = [1, 2, 3]
# lst2 = [4, 5, 6]
# res_lst = []
# for i in range(0,len(lst1)):
#     res_lst.append(lst1[i]+lst2[i])
# print(res_lst)

# str1 = "Listen"
# str2 = "Silent"
# print(sorted(list(str1.upper()))==sorted(list(str2.upper())))

# str1 = "Kayak".lower()
# str2 = "kayak".lower()
# print(str1==str2)

# string = "P r ogramm in g "
# c=0
# for i in string:
#     if i==" ":
#         c+=1
# print(string.count(" "))
# print(c)

# import re

# name = 'Python is 1'

# digitCount = re.sub("[^0-9]", "", name)
# letterCount = re.sub("[^a-zA-Z]", "", name)
# spaceCount = re.findall("[ \n]", name)

# print(len(digitCount))
# print(len(letterCount))
# print(len(spaceCount))

# d=0
# l=0
# s=0
# for i in name:
#     if i.isalpha():
#         l+=1
#     elif(i.isdigit()):
#         d+=1
#     else:
#         s+=1
# print(d,l,s)



# import re

# string = "C O D E"
# spaces = re.compile(r'\s+')
# result = re.sub(spaces, '', string)
# print(result)


# floors = 3
# h = 2*floors-1
# for i in range(1, 2*floors, 2):
#     print('{:^{}}'.format('*'*i, h))

# row=4
# col=4
# for i in range(row):
#     for j in range(i,col):
#         print(' ',end=" ")
#     for j in range(i*2+1):
#         print('*',end=' ')
#     print()

# from random import shuffle
# lst = ['Python', 'is', 'Easy']
# shuffle(lst)
# print(lst)
