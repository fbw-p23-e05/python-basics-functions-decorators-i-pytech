
def get_html_greeting():
    return "Hello, World!"

# print(get_html_greeting())

def make_bold(func):
    def wrapper():
        result="<strong>" + func() + "</strong>"
        print(result)
        return result
    return wrapper

# result= make_bold(get_html_greeting)
# print(result)

@make_bold
def get_html_greeting():
    return "Hello, World!"

# print(get_html_greeting())

get_html_greeting()

# #  here how to use * and ** 
# def print_arguments(*args, **kwargs):
#     print("Positional arguments:")
#     for arg in args:
#         print(arg)

#     print("Keyword arguments:")
#     for key, value in kwargs.items():
#         print(f"{key}: {value}", end="")

# print_arguments("Hello", "World", name="John ", age=25, city=" Berlin")
