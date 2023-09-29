def make_bold(func):
    def adapt(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<strong>{result}</strong>"
    return adapt

@make_bold
def get_html_greeting():
    return "Hello, World!"

@make_bold
def get_custom_html_greeting(first, last):
    return f"Hello, {first} {last}!"

print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))
print(get_html_greeting())