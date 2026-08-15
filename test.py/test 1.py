#Section A - MCQ
#(Q-1)Which of the following is a valus variable name in python?
#(A) 2value             (B) value_2
#(C)value-2             (D)value 2
#correct option (B)

#(Q-2)what is the data type of the value 3.14 in python?
#A)int                   B) float
#C)complex               D)str
#correct option (B)

#(Q-3)Which operator is used to find the reminder in python ?
#A)//                    B) %
#C)**                     D) /
#correct option (B

#(Q-4)which function is used to take input from the user in python ?
#A)scant()                B)input()
#C)get()                  D)read()
#correct option  (B)

#(Q-5)which statment is used to make a decision in python?
#A)for                    B)while
#C)if                     D)del
#correct option (C
# )
#(Q-6)which loop is best suited when the number of iteration is known in advance?
#A)for loop               B)while loop
#C)do while loop          D)none of these
# #correct option (A) 

# #(Q-7)which keyword is used to define a function in python?
# #A)function           B)fun
# #C)def                D)define
# #correct option (c)

# #(Q-8)which mode is to open aq file for appending data in python?
# #A)"r"                B)"w"
# #C)"a"                D)"x"
# #correct option (a)

# #(Q-9)which block is used to handel exception in python?
# #A)try-execpt         B)catch-throw
# # #C)error-handel       D)check-fix
# # #corect option(a)
# # #C)what will print (type(10))output?
# # #A0<class'float'>      B)<class'str'>
# # #C)<class'int'>        D)<class'bool'>
# # # #correct opotion (c)

# # # #(Q-11)write in python programthat takes the length and breath of a rectangle as input and calculate its area and perimeter?
# # # a= float(input("enter your length"))
# # # b= float(input("enter your breath"))
# # # print(a*b)
# # # print(2*(a+b))

# # # #(Q-12)write a python program to check whether a number entered by the user is Positive ,Negative,or Zero using if elif
# # # num = float(input("enter your number:"))
# # # if num > 0:
# # #     print("the number is positive.")
# # # elif num < 0:
# # #     print("the number is negative.")
# # # else:
# # #     print("the number is zero.")

# # #(Q-13)write a python program using a while loop to print all even number between 1and50?
# # num = 2
# # while num <=50:
# #     print(num)
# #     num += 2

# #(Q-14)write a python function is_prime(n) thet return whether n is prime. call it wuth a sample value and print return/
# def is_prime(n):
#     if n<=1:
#         return False
# #     for i in range(2,int(n**0.5)+1):
# #         if n%1==0:
# #             return False
# #         return True
# #     num= int(input("enter your number:"))
# #     print(is_prime(num))

# #(Q-15)write a python programme that divides two user-entered number ,using try-execpt to handel division by zero?
# try :
#     num1 = float(input("enter your number:"))
#     num2 = float(input("enter your number:"))
    
#     result = num1 / num2
#     print("result = ",result)
# except ZeroDivisionError:
#     print("Error : Division by zero is not allowed.")  
      
# #(Q-16)write a python using nested loops to print the following star pattern for rows?              
# for i in range(1,6):
#     for j in range(i):
#         print ("*",end=" ")
#     print()

# #(Q-17)write a python program using nested loops to printthe pprint the following 
# for i in range(1,6):
#     for j in range(i):
#         print(i, end=" " )
#     print()    
 
 
#  #(Q-18)write a python program to creat a text file STUDENT .txt write three student names into it (one per line) then read and display its contents?
# file = open("student.txt","w")
# file.write("Shivani/n")
# file.write("Tamanna/n")
# file.write("Himanshi/n")
# file.close()

# file = open("student.txt","r")
# print("content of student.txt:")
# print(file.read())
# file.close()
 #(Q-19)write a python program that accept 5 number from the user and calculates their average , using try-execpt-finnally to handel invalid (non-numeric) input?  
# num1 = float(input("enter your first number:")) 
# num2 = float(input("enter your second number:"))
# num3 = float(input("enter your third number:"))
# num4 = float(input("enter your fourth number:"))
# num5 = float(input("enter your five number:"))
# average = (num1+num2+num3+num4+num5)/5
# print("Average=",average)
