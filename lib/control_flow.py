#!/usr/bin/env python3

def admin_login(username, password):
    if username.upper() == "ADMIN" and password == "12345":
        return "Access granted"
    
    return "Access denied"

def hows_the_weather(temperature):
    if temperature > 85:
        return "It's too dang hot out there!"
    elif 65 >= temperature >= 40:
        return "It's a little chilly out there!"
    elif temperature < 40:
        return "It's brisk out there!"

    return "It's perfect out there!"

def fizzbuzz(num):
    # your code here
    pass

def calculator(operation, num1, num2):
    # your code here
    pass
