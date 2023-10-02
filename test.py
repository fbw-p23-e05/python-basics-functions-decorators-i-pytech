def get_html_greeting_with_args(**kwargs):
    name = kwargs["name"] if "name" in kwargs else "World"
    age = kwargs["age"] if "age" in kwargs else None
    city = kwargs["city"] if "city" in kwargs else None
    
    greeting = f"Hello, {name}!"
    
    if age is not None:
        greeting += f" You are {age} years old."
    
    if city is not None:
        greeting += f" You live in {city}."
    
    return greeting

# Call the function with multiple keyword arguments
greeting1 = get_html_greeting_with_args(name="Alice", age=30)
greeting1 = get_html_greeting_with_args()
greeting2 = get_html_greeting_with_args(name="Bob", city="New York")
greeting3 = get_html_greeting_with_args(name="Charlie", age=25, city="London")

print(greeting1) 
print(greeting2)  
print(greeting3)  


# def get_html_greeting_with_args(**kwargs):
#     greeting_data = {
#         "name": kwargs["name"] if "name" in kwargs else "World",
#         "age": kwargs["age"] if "age" in kwargs else None,
#         "city": kwargs["city"] if "city" in kwargs else None,
#         "education": kwargs["education"] if "education" in kwargs else None
#     }
    
#     greeting_data = {key: value for key, value in greeting_data.items() if value is not None}

#     return greeting_data


# greeting1 = get_html_greeting_with_args()
# greeting2 = get_html_greeting_with_args(name="Bob", city="New York")
# greeting3 = get_html_greeting_with_args(name="Charlie", age=25, city="London", education="programmer")

# print(greeting1) 
# print(greeting2)  
# print(greeting3)  


 