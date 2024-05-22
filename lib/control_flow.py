#!/usr/bin/env python3

def admin_login(username, password):
    if (username == "admin" or  username == "ADMIN") and password == "12345":
        return "Access granted"
    else: 
        return "Access denied"
    # your code here

    pass

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature < 65 and temperature > 40:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else: 
        return "It's perfect out there!"
    # your code here
    pass

def fizzbuzz(num):
     quotientThree = num % 3
     quotientFive = num % 5
     
     if  quotientFive == 0 and quotientThree == 0:
         return "FizzBuzz"
     elif quotientFive == 0:
         return "Buzz"
     elif quotientThree == 0 :
         return "Fizz"
     else: return num
     # your code here
     pass

def calculator(operation, num1, num2):
    if operation == "+" :
      return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*" :
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid operation!")
        return None
   #your code here
    pass 

