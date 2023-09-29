

### Task 1


""" def make_bold(func):

    def inner():
     return f"<strong>{func()} </strong>"
    return inner

@make_bold
def get_html_greeting():

    return 'Hello World'


print(get_html_greeting()) """


### Task 2

def make_bold(func):

    def inner(*arg,**args):
     return f"<strong>{func(*arg,**args)} </strong>"
    return inner

@make_bold
def get_html_greeting():

    return 'Hello World'

@make_bold
def get_custom_html_greeting(first,last):

    return f"Hello, {first} {last} !"


print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))
print(get_html_greeting())   