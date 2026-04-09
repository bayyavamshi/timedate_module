# s=open('text_file.txt',mode='w+')
# s.write(" r+ method")
# s.seek(0)
# print(s.read())
# s.close()
# print(2+3)
# try:
#     a=1

# except NameError:
#     print("type error")
# else:
#     print("all good")
# finally:
#     print("always")
# s=open('text_file.txt',mode='r')

# s1=open('text_file.txt',mode='w')

# for i in s:
#     s1.write(i)
#     # print(i)


# f=open("text_file.txt",'w')
# f.write("hii vamshi do work confidently\n")
# f.write("hlo")
# # print(f.tell())
# f.seek(0)
# print(f.readlines())
# f.close()
# f=open('text_file.txt','a+')
# f.write("hii every one")
# f.close()
# f=open('vamshi.png','rb')
# data=f.read()
# n=open("image.png",'wb')
# n.write(data)
# li=['vamshi',"yadav","good","boy"]
# with open("text_file.txt",'a') as a:
#     a.writelines([f"{i}\n" for i in range(0,6)])
# with open('text_file.txt','w') as f:
#     print(f.write('890'))

# with open('practice_file.py','a') as f:
#     data=f.write('practice_file.py')


# with open('text_file.txt','w') as f:
#     f.write("hii this is vamshi")
# with open('text_file.txt','r') as f:
#     text=f.read()
#     word=text.split()
#     for i in word:
#         print(i)

# Create a file for testing
with open('sample.txt', 'w') as f:
    f.write("""hii this is vamshi
vamshi is learning python
python is easy
this line does not have the word
vamshi likes coding""")

# Define the word to search for
word = "vamshi"
count = 0

# Open the file and count lines containing the word
with open('sample.txt', 'r') as f:
    for line in f:
        if word in line:       # check if word appears in the line
            count += 1

print(f"The word '{word}' appears in {count} line(s).")




