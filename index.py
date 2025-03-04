# 1.write a code to get odd digits in numbers

# num = 1326
# add = 0
# while num>0:
#     digit = num%10
#     if digit%2!=0:
#         add+= digit
#     num = num//10
# print("sum of odd digit number was :",add) 


# write a code for non prime digits in a num
# num = 1436
# sum = 0
# while num>0:
#     digit = num%10
#     count = 0
#     dup = digit
#     for i in range(2,dup):
#         if dup%i==0:
#             count+=1
#             break      
#     num = num//10
#     if count!=0:
#         sum+= digit
# print(sum)

# code about armstrong number 153=sum of digit to the power of count

# num = int(input("enter the number"))
# value = num1
# value2 = num1
# count = 0
# while value>0:  
#     count+=1   
#     value = temp//10 
# # print(count)

# sum = 0
# while value2>0:
#     digit = value2%10    
#     power =1
#     for i in range(1,count+1):
#         power*=digit
#     sum+=power
#     value2= value2//10
# if sum == num1:
#     print(num,"is armstrong num")
# else:
#     print(num,"is not an armstrong num")
    


# code to find the Nearest prime.

# num = 20
# temp = num
# right_prime = 0

# while True :
#     temp +=1
#     count = 0
#     for i in range(2,temp):
#         if temp%i==0:
#             count+=1
#             break
#     if count!=0:
#         right_prime = temp
#         break
# print(temp)
# left_prime = 0
# temp2 = num
# while True:
#     temp2-=1
#     if temp2<1:
#         count = 0
#     for i in range(2,temp2):
#         if temp%i==0:
#             count+=1
#             break
#     if count!=0:
#         left_prime = temp2
#         break
# print(left_prime)

#code about check the prime or not using function

# num = int(input("enter any number"))
# num1 = num
# def check(num1):
#     if num1<1:
#         return False
#     for i in range(2,num1):
#         if num1%i==0:
#             return False
#     return True

# print(check(num1))
# print(num,"is prime",check(num1))

# 1. The Ticket Machine (If-Else & Number System)
# You are designing a self-service metro ticket machine. The machine asks the user to enter their age and determines the fare based on the following rules:
# •	Children (age < 10) ride for free.
# •	Teenagers (10 ≤ age < 18) get a 50% discount.
# •	Seniors (age ≥ 60) get a 30% discount.
# •	Everyone else pays the full price of $10.


# age = int(input("enter your age"))
# if age<10:
#     print("your got ride for free")
# elif (age>=10) and (age<18):
#     print("you are  get 50% discount")
# elif age >=60:
#     print("you are get 30% discount")
# else:
#     print("pays the full price of $10")
    
    

# 2 The Festival Discount (Number System & If-Else)
# During a festival, a store offers discounts based on the last digit of a customer’s phone number:
# •	If the last digit is even, they get a 10% discount.
# •	If the last digit is odd, they get a 15% discount.
# •	If the last digit is 0, they get a 20% discount.

# last_digit = int(input("enter your mobile num last digit"))
# if last_digit%2==0:
#   print("get a 10% discount.")
# elif last_digit%2!==0:
#     print("get a 15% discount.")
# else:
#     print("get a 20% discount.")

# 3 The Bank Account Pin (Number System & Loops)
# A bank has a PIN validation system where:
# •	A user is given 3 attempts to enter a 4-digit PIN.
# •	If they enter the correct PIN, they get access.
# •	If they fail all 3 attempts, their account is locked.

# pin = 1234
# count = 1
# while True:
#     if count<=3:
#         enter_pin = int(input("enter your pin here"))
#         if pin == enter_pin:
#             print("you are access")
#             break
#         else:
#             count+=1
#             if count <=3:
#                 print("you are remaining attemps ",count,"out of 3")
            
#     else:
#         print("your attemp are fail your account locked")
#         break 



