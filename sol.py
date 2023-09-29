

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

""" def make_bold(func):

    def inner(*arg,**kwargs):
     return f"<strong>{func(*arg,**kwargs)} </strong>"
    return inner

@make_bold
def get_html_greeting():

    return 'Hello World'

@make_bold
def get_custom_html_greeting(first,last):

    return f"Hello, {first} {last} !"


print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))
print(get_html_greeting())   """


### Task 3


def make_bold(func):

    def inner_bold(*arg,**kwargs):
     return f"<strong>{func(*arg,**kwargs)} </strong>"
    return inner_bold


def make_italics(func):

    def inner_ital(*arg,**kwargs):
     return f"<em>{func(*arg,**kwargs)} </em>"
    return inner_ital

def make_paragraph(func):

    def inner_para(*arg,**kwargs):
     return f"<p>{func(*arg,**kwargs)} </p>"
    return inner_para

@make_bold
def get_full_name(first_name,last_name):
   
   return f"{first_name} {last_name}"


@make_paragraph
@make_italics
def get_custom_html_greeting(first,last):

    return f"Hello, {get_full_name(first,last)} !"


print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))