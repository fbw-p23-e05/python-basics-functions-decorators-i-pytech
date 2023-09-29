def make_bold(func):
    def inner(*x, **y):
        return f'<strong>{func(*x, **y)}</strong>'
    return inner

def make_italics(func):
    def inner(*x, **y):
        return f'<em>{func(*x, **y)}</em>'
    return inner

def make_paragraph(func):
    def inner(*x, **y):
        return f'<p>{func(*x, **y)}</p>'
    return inner

@make_bold
def get_full_name(x, y):
    return f'{x} {y}'

@make_paragraph
@make_italics
def get_custom_html_greeting(first, last):
    full = get_full_name(first, last)
    return f'Hello, {full}!'

print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))
