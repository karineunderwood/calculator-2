"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

# Define method calculator
def calculator():

    user_input = input("Enter your equation >")
    tokens = user_input.split(' ')
    
    operator = tokens[0]
    num1 = tokens[1]
    num2 = tokens[2]


    if operator == "q":
        print("Goodbye!")
    
    elif operator == "pow":
        result =  power(float(num1), float(num2)) 
    
    elif operator == "+":
        result = add(float(num1), float(num2))
    
    elif operator == "*":
        result = multiply(float(num1), float(num2))
    
    elif operator == "-":
        result = subtract(float(num1), float(num2))

    elif operator == "/":
        result = divide(float(num1), float(num2))

    elif operator == "square":
        result = square(float(num1))

    elif operator == "cube":
        result = cube(float(num1))
    
    elif operator == "mod":
        result = mod(float(num1), float(num2))

    
    print(result)  
    return result

    

calculator()

