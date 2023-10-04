# Task 1

def make_bold(func):
    def wrap():
        return f"<strong>{func()}</strong>"
    return wrap

@make_bold
def get_html_greeting():
    return "Hello, World!"

print(get_html_greeting())

# Task 2 

def make_bold(func):
    def wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<strong>{result}</strong>"
    return wrap

@make_bold
def get_html_greeting():
    return "Hello, World!"

@make_bold
def get_custom_html_greeting(first, last):
    return f"Hello, {first} {last}!"

print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))
print(get_html_greeting())


# Task 3

def make_bold(func):
    def wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<strong>{result}</strong>"
    return wrap

def make_italics(func):
    def wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<em>{result}</em>"
    return wrap

def make_paragraph(func):
    def wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<p>{result}</p>"
    return wrap

@make_bold
def get_full_name(first, last):
    return f"{first} {last}"

@make_paragraph
@make_italics
def get_custom_html_greeting(first, last):
    full_name = get_full_name(first, last)
    return f"Hello, {full_name}!"

print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))

# Task 4

def wrap_with(tag):
    def decorator(func):
        def wrap(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"<{tag}>{result}</{tag}>"
        return wrap
    return decorator

@wrap_with(tag="strong")
def get_full_name(first, last):
    return f"{first} {last}"

@wrap_with(tag="p")
@wrap_with(tag="em")
def get_custom_html_greeting(first, last):
    full_name = get_full_name(first, last)
    return f"Hello, {full_name}!"

print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))