def make_bold(funk):
    def inner():
        return f"<strong>{funk()}<\strong>"
    return inner

@make_bold
def get_html_greeting():
    return "Hello World!"

print(get_html_greeting())