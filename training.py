# str1='abcabcdab'
# n=len(str1)
# l=0
# for i in range(n):
#     for j in range(i,n):
#         s=''
#         for k in range(i,j+1):
#             if str1[k] not in s:
#                 s+=str1[k]
#     if len(s)==4:
#         print(s)
#         l=max(l,len(s))
# li=[[1,2,3,4],
#     [5,6,7,8],
#     [9,10,11,12],
#     [13,14,15,16]]
# n=len(li)

# for i in range(n):
#     for j in range(n):
#         if i==0 and j==j:
#             print(li[i][j])
#         elif(i and j==n-1):
#             print(li[i][n-1])
#         elif(i==n-1 and j==j):
#             print(li[n-1][n-j-1])
#         elif(i==n-i-1 and j==0):
#             print(li[n-j-1][j])
li = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

n = len(li)

# Top row
for j in range(n):
    print(li[0][j], end=" ")

# Right column
for i in range(1, n):
    print(li[i][n-1], end=" ")

# Bottom row (reverse)
for j in range(n-2, -1, -1):
    print(li[n-1][j], end=" ")

# Left column (reverse)
for i in range(n-2, 0, -1):
    print(li[i][0], end=" ")

for j in range(n//2):
    print(li[1][j+1],end=" ")

for j in range(1,n//2):
    print(li[i+j][n//2])
for k in range(1):
    print(li[n//2][1],end=" ")
# --------------------------------------
def first_unique_char(s):
    freq = {}

    # Count frequency of each character
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    # Find first character with frequency 1
    for i in range(len(s)):
        if freq[s[i]] == 1:
            return i,s[i]

    return -1
s="leetcode"
print(first_unique_char(s))

# -------------------------------------------------
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()
print("Number of words:", len(words))

# -----------------------------------------------------
sentence = input("Enter a sentence: ")

count = 0
in_word = False

for ch in sentence:
    if ch != ' ' and not in_word:
        count += 1
        in_word = True
    elif ch == ' ':
        in_word = False


