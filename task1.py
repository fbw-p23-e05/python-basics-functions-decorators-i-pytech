def make_bold(func):
    def wrapper():
        return f"<strong>{func()}</strong>"
    return wrapper

@make_bold
def get_html_greeting():
    return "Hello, World!"

print(get_html_greeting())




