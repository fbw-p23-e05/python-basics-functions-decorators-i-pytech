def wrap_with(tag):
    def decorate(func):
        def wrap(*args, **kwargs):
            return f"<{tag}>{func(*args, **kwargs)}</{tag}>"
        return wrap
    return decorate


@wrap_with(tag="strong")
def get_full_name(first, last):
    return first + " " + last


@wrap_with(tag="p")
@wrap_with(tag="em")
def get_custom_html_greeting(first, last):
    return get_full_name(first, last)


print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))