class car:
    def __init__(self,input_color):
        self.color=input_color
    def start(self):
        print("car start")
    def color_change(self,input_color):
        self.color=input_color
        print("color change")
h1=car("red")
h2=car("black")
h3=car("pink")
h2.color_change("orege")
# h3.color="orege"
print(h2.color)
# li=[1,2,4,5,-32,3]
# k=3
# # print(li[k:]+li[:k])
# n=len(li)
# for i in range(k%n):
#     l=li.pop()
#     li.insert(0,l)
#     # l=li[-1]
# print(li)
# li=[[1,2,3]
#     ,[4,5,6]
#     ,[7,8,9]]
# for i in range(len(li)):
#     for j in range(len(li[i])):
#         if i>j:
#             li[i][j],li[j][i]=li[j][i],li[i][j]
# print(li)
l1=[1,2,3,4,5,6]
l2=[7,8,9,10,11]
l3=[]


