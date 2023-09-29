def get_html_greeting():
    return 'Hello, World!'

def make_bold(func):
    def inner():
        print('<strong>'+ func()+ '</strong>')
    return inner

dec = make_bold(get_html_greeting)
dec()