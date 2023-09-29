greet = 'Hello, World!'

def make_bold(func):
    def wrapper(*args, **kwargs):
        return '<strong>' + func(*args, **kwargs) + '</strong>'
    return wrapper

@make_bold
def get_html_greeting():
    return greet

@make_bold
def get_custom_html_greeting(first, last):
    return f'Hello, {first} {last}!'


print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))
print(get_html_greeting())