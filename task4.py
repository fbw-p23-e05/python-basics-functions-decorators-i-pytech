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

@wrap_with(tag="em")
@wrap_with(tag="p")
def get_custom_html_greeting(first, last):
    full_name = get_full_name(first, last)
    return f"Hello, {full_name}!"

print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))