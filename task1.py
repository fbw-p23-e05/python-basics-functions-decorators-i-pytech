def make_bold(funk):
    def inner():
        print("<strong>", end="")
        funk()
        print("<\strong>")
    return inner

@make_bold
def get_html_greeting():
    print("Hello World!", end="")

get_html_greeting()