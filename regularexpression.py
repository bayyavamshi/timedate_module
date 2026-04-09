import re
# text="i am the vamshi"
# ch=re.search(r'am',text)
# print(ch.group())
# text1="90this 123vamshi789 this"
# ch=re.search(r'\d',text1)#it return the single number
# ch=re.search(r'\d+',text1)#all numbers in the string
# print(ch.group())
# ch=re.findall(r'\d+',text1)#it returns in the list and if the value not found it return none
# print(ch)
# ch=re.match(r"this",text1)
# ch=re.match(r"\d",text1)
# ch=re.sub(r'this','This',text1)
# ch=re.sub(r'\d+','x',text1)
# ch=re.split(r'\d+',text1)
# ch=re.findall(r't..s',text1)
# print(ch)

str1 = "vamshi aa2736486934 yadav"
ch = re.findall(r'[abc]|[csk]', str1)
print(ch)