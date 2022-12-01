# DATA TYPES IN PYTHON
# 1. integers
# 2. float
# 3. string
# 4. complex

# a = 255
# print(type(a))

#to know variable's datatype we use type function

# catination in python
# a="Rishav"
# b="Singh"
# print(a + b)
# to seperate the words we use empty string
# print(a+" "+b)

# if we have to seperate items in a variable we use sep function
 
# a = (1, 2, 3, "rishav",4.5)
# print (a,sep=",") 

#BOOLEAN
# a or b = a (if a is truly)
# a or b = b (if a is falsy)
# a and b = b (if a is truly)
# a and b = a ( is a is falsy)

#CONTROL FLOW / LOOPING STATEMENT
# in python flow/loop start when we use :(colon) in last of a expression
# we can write pass to pass that line 

# a = ("TATA","FORD","BMW")
# for i in a:
#      print(i)

# for i in range(5):
#      print(i)
#      if i==3:
#          break

#WHILE LOOP
# a = 1
# while a<10:
#     print(a)
#     a+=1

# n=5
# for i in range(n):
#     for j in range(n):
#         print(i,end=" ")
# NOTE - it will print in one line
         
# n = 5
# for i in range(n):
#     for j in range(n):
#         print(i, end=" ")
#     print() 
# NOTE - using empty string it will make seperate line for different digits  
# 
# n=5
# for i in range(n):
#     for j in range(n):
#         print(n-j-i,end=" ")  
#      print()

# QUESTION - we have to make 3 3 3
#                            3 2 3
#                            3 3 3

# answer
n = 5
for i in range(n):
    for j in range(n):
         print(max(i+1,j+1,n-i,n-j),end=" ")
    print()
#
#