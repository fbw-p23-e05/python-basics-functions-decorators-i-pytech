
def make_bold(func):
    def wrapper(*args, **kwargs):
        return '<strong>' + func(*args, **kwargs) + '</strong>'
    return wrapper

def make_italics(func):
    def wrapper(*args, **kwargs):
        return f"<em>{func(*args, **kwargs)}</em>"
    return wrapper

def make_paragraph(func):
    def wrapper(*args, **kwargs):
        return f"<p>{func(*args, **kwargs)}</p>"
    return wrapper

@make_bold
def get_full_name(first, last):
    return f"{first} {last}"

def get_custom_html_greeting(first, last):
    full_name = get_full_name(first, last)
    return f"Hello, {full_name}!"

@make_paragraph
@make_italics
def decorated_greeting(first, last):
    return get_custom_html_greeting(first, last)

print(decorated_greeting("James", "Brown"))
print(decorated_greeting(first="James", last="Brown"))