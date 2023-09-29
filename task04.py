def wrap_with(tag):
    def decorator(func):
        def inner(*arg, **kwarg):
            get = func(*arg, **kwarg)
            return f'<{tag}>{get}</{tag}>'
        return inner
    return decorator

@wrap_with(tag="strong")
def get_full_name(x, y):
    return f'{x} {y}'

@wrap_with(tag="p")
@wrap_with(tag="em")
def get_custom_html_greeting(first, last):
    full = get_full_name(first, last)
    return f'Hello, {full}!'

print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))
