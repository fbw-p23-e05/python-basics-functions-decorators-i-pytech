greet = 'Hello, World!'

def make_bold(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper

@make_bold
def get_html_greeting():
    return greet


print(get_html_greeting())
