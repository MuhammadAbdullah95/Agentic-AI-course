from calculate import add, subtract, multiply, divide

sum = add(5, 10)
diff = subtract(10, 5)


print("Addition:", sum)
print("Subtraction:", diff)


try:
    quotient = divide(10, 0) 
except ZeroDivisionError as e:
    quotient = None
product = multiply(5, 10)
 

     
print("Multiplication:", product)
print("Division:", quotient)    
