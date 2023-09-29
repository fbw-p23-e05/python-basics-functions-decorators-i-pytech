def make_bold(func):
    def wrapper(*args, **kwargs):
        return f"<strong>{func(*args, **kwargs)}</strong>"
    return wrapper

@make_bold
def get_html_greeting():
    return "Hello, World!"

@make_bold
def get_custom_html_greeting(first, last):
    return f"Hello, {first} {last}!"

# Test cases
print(get_custom_html_greeting("James", "Brown"))  
print(get_custom_html_greeting(first="James", last="Brown")) 
print(get_html_greeting())  
