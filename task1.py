
# def make_bold(func):
#     def wrapper(*args, **kwargs):
#         result="<strong>" + func(*args, **kwargs) + "</strong>"
#         print(result)
#         return result
#     return wrapper

# @make_bold
# def get_html_greeting():
#     return "Hello, World!"

# get_html_greeting()

# @make_bold
# def get_html_greeting_with_name(name):
#     return f"Hello, {name}!"

# get_html_greeting_with_name("Alice")  


def bald_txt(func): 
    def wrapper(*arg,**kwargs):
        result= func(*arg,**kwargs)
        if isinstance(result,dict): 
            return{key:value for key,value in result.items()}
        else:
            return result
    return wrapper 

@bald_txt
def hello(name):
    if name == "Alex":
        return {"greeting": "Hello", "name": name}
    else:
        return f"Hello {name}"

result1 = hello("Alex")
result2 = hello("Jack")

print(result1) 
print(result2) 





# def wrap_with_html(tag):
#     def decorator(func):
#         def wrapper():
#             result = f"<{tag}>" + func()+ f"</{tag}>"
#             return result
#         return wrapper
#     return decorator

# @wrap_with_html("strong")
# def get_html_greeting():
#     return "Hello, World!"

# @wrap_with_html("em")
# def get_emphasized_greeting():
#     return "Greetings!"

# @wrap_with_html("p")
# def get_paragraph_text():
#     return "This is a paragraph of text."

# @wrap_with_html("h1")
# def get_heading_text():
#     return "This is a heading."
# print(get_html_greeting())  
# print(get_emphasized_greeting())  
# print(get_paragraph_text())
# print(get_heading_text())

#def wrap_with_html(tag):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             result = f"<{tag}>" + func(*args, **kwargs) + f"</{tag}>"
#             return result
#         return wrapper
#     return decorator

# @wrap_with_html("div")
# def get_div_content(*args, **kwargs):
#     # print(args, "args is here ")
#     print(kwargs, "kwargs is here ")
#     content = " ".join(args)
#     # print(content, "content is here")
#     options = " ".join(f"{key}='{value}'" for key, value in kwargs.items())
#     print(options, "options is here ")
#     return f"This is a <div {options}>{content}</div>."

# print(get_div_content("Some text"))
# print(get_div_content("Text with options", id="my-div", class_name="highlight"))


# @make_bold
# def get_html_greeting_with_name(**kwargs):
#     name = kwargs["name"] if "name" in kwargs else "World"
#     return f"Hello, {name}!"

# get_html_greeting_with_name(name="Alice")  # Custom name provided.
# get_html_greeting_with_name() 


# #  here how to use * and ** 
# def print_arguments(*args, **kwargs):
#     print("Positional arguments:")
#     for arg in args:
#         print(arg)

#     print("Keyword arguments:")
#     for key, value in kwargs.items():
#         print(f"{key}: {value}", end="")

# print_arguments("Hello", "World", name="John ", age=25, city=" Berlin")
