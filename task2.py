def make_bold(funk):
    def inner(*name, **last):
        return f"<strong>{funk(*name, **last)}<\strong>"
    return inner

@make_bold
def get_custom_html_greeting(first, last):
    return f"Hello, {first} {last}!"

@make_bold
def get_html_greeting():
    return "Hello World!"

print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))
print(get_html_greeting())