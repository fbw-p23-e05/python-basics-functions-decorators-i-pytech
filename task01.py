def make_bold(func):
    def inner():
        return '<strong>'+ func()+ '</strong>'
    return inner

@make_bold
def get_html_greeting():
    return 'Hello, World!'

print(get_html_greeting())

