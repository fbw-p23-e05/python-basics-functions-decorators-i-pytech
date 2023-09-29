# Function decorators I
## Task 1

def make_bold(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper

@make_bold
def get_html_greeting():
    return "Hello, World!"
print(get_html_greeting())

## Task 2

def make_bold(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper
def emphasis(func):
    def wrapper(*args, **kwarg):
        return '<strong>' + func(*args, **kwarg) + '</strong>'
    return wrapper
@make_bold
def get_html_greeting():
    return "Hello, World!"
# print(get_html_greeting())

@emphasis
def get_custom_html_greeting(first="James", last="Brown"):
    return f"Hello, {first} {last}!"
# print(get_custom_html_greeting())

print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))
print(get_html_greeting())

## TASK 3

def emphasis(func):
    def wrapper(*args, **kwarg):
        return "<p>" + "<em>" + "Hello," + " " + "<strong>" + func(*args, **kwarg) + "</strong>!" + "</em>" + "</p>"
    return wrapper
@emphasis
def get_custom_html_greeting(first="James", last="Brown"):
    return f"{first} {last}"

print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))


## TASK 4
    
def wrap_with(func):
    def wrapper(*args, **kwargs):
        return "<p>" + "<em>" + "Hello," + " " + "<strong>"  + func(*args, **kwargs) + "</strong>!" + "</em>" + "</p>"
    return wrapper
@wrap_with
def get_custom_html_greeting(first="James", last="Brown"):
    return f"{first} {last}"
print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))