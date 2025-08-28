# # # Assigning a function to a variable
# def greet(n):
#     return f"Hello, {n}!"



# say_hi = greet 

# #  # Assign the greet function to say_hi
# # print(say_hi("Alice")) 

# # # Passing a function as an argument
# # def apply(f, v):
# #     return f(v)


# # res = apply(say_hi, "Bob")
# # print(res) 


# def apply(f, v):
#     return f(v)


# res = apply(say_hi, "Bob")
# print(res)


# # # Returning a function from another function
# # def make_mult(f):
# #     def mult(x):
# #         return x * f
# #     return mult
# # dbl = make_mult(2)
# # print(dbl(5))


# def make_mult(f):
#     def mult(x):
#         return x * f
#     return mult

# dbl = make_mult(2)

# print(dbl(5))


# def decorator_function(original_function):
#     def wrapper():
#         print("Before calling the function")
#         original_function()
#         print("After calling the function")
#     return wrapper

# @decorator_function
# def display():
#     print("Inside the display function")


# display()



def decorator_name(func):
    def wrapper(*args, **kwargs):
        print("Before execution")
        result = func(*args, **kwargs)
        print("After execution")
        return result
    return wrapper

@decorator_name
def add(a, b):
    return a + b

print(add(5, 3))




# def func(*args):
#     print(args)

# func(1, 2, 3, 4)
# # Output: (1, 2, 3, 4)


# # def function(*, name, age):
# #     print(f"Name: {name}, Age: {age}")

# # function(name="Alice", age=30)

# def fucntion_abd(**kwargs):
#     print(kwargs)


# fucntion_abd(name="Alice", age=30)

