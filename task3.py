def make_paragraph(funk):
    def inner(*name, **last):
        return f"<p>{funk(*name, **last)}</p>"
    return inner

def make_italics(funk):
    def inner(*name, **last):
        return f"<em>Hello, {funk(*name, **last)}</em>"
    return inner

def make_bold(funk):
    def inner(*name, **last):
        return f"<strong>{funk(*name, **last)}</strong>"
    return inner

@make_bold
def get_full_name(first, last):
    return first + " " + last

@make_paragraph
@make_italics
def get_custom_html_greeting(first, last):
    return get_full_name(first, last)


print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))