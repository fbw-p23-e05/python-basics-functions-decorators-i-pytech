def wrap_with(tag):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"<{tag}>{result}</{tag}>"
        return wrapper
    return decorator

@wrap_with(tag="strong")
def get_full_name(first, last):
    return f"{first} {last}"

def get_custom_html_greeting(first, last):
    full_name = get_full_name(first, last)
    return f"Hello, {full_name}!"

@wrap_with(tag="p")
@wrap_with(tag="em")
def decorated_greeting(first, last):
    return get_custom_html_greeting(first, last)

print(decorated_greeting("James", "Brown"))
print(decorated_greeting(first="James", last="Brown"))