# n=5
# num1=0
# num2=1
# for i in range(n):
#     for j in range(n):
#         if i>=j:
#             print(num1,end=" ")
#             num1,num2=num1+num2,num1
#         else:
#             print(" ",end=" ")
#     print()
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def add(self,ele):
        if self.head==None:
            self.head=node(ele)
            return
        tem=self.head
        while tem.next:
            tem=tem.next
        tem.next=node(ele)
        return
    def dis(self):
        tem=self.head
        while tem:
            print(tem.data,'->',end="")
            tem=tem.next
        return
    
    def length(self):
        tem=self.head
        count=0
        while tem:
            count+=1
            tem=tem.next
        return count
    

    # def mid(self):
    #     tem=self.head
    #     mid=self.length()
    #     count=0
    #     while tem:
    #         count+=1
    #         if(count==mid//2+1):
    #             print(tem.data)
    #         tem=tem.next
    def mid(self):
        fast=self.head
        slow=self.head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        return slow.data
h1=linkedlist()
h1.add(23)
h1.add(24)
h1.add(25)
h1.add(26)
h1.add(27)
h1.add(28)
print(h1.length())
print(h1.mid())
h1.dis()
        
