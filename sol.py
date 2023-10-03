# #Task 1

# def make_bold(func):
#     def go_on():
#         return "<strong>" + func() + "</strong>"
#     return go_on

# @make_bold
# def get_html_greeting():
#     return "Moin moin und Herzlich Wilkommen"

# print(get_html_greeting())


#Task 2


# def make_bold(func):
#     def go_on(*args, **kwargs):
#         return "<strong>" + func(*args, **kwargs) + "</strong>"
#     return go_on

# @make_bold
# def get_html_greeting():
#     return "Moin moin und Herzlich Wilkommen"

# @make_bold
# def get_custom_html_greeting(first, last):
#     return f" Hallo, {first} {last}!"

# print(get_custom_html_greeting("James", "Brown"))
# print(get_custom_html_greeting(first="James", last="Brown"))
# print(get_html_greeting())


# #Task 3


# def get_full_name(first="", last=""):
#     return f"{first} {last}"  

# def make_italics(func):
#     def closing(*args, **kwargs):
#         stepback = func(*args, **kwargs)
#         return f"<em>{stepback}</em>"
#     return closing

# def make_paragraph(func):
#     def closing_closing(*args, **kwargs):
#         stepback = func(*args, **kwargs)
#         return f"<p>{stepback}</p>"
#     return closing_closing

# def make_bold(func):
#     def go_on(*args, **kwargs):
#         stepback = func(*args, **kwargs)
#         return f"<strong>{stepback}</strong>"
#     return go_on


# @make_paragraph
# @make_italics
# @make_bold
# def get_html_greeting(i):
#     return  i


# @make_paragraph
# @make_italics
# @make_bold
# def get_custom_html_greeting(first=" ", last=""):
#     full_name = get_full_name(first, last)
#     return f"Hello, {full_name}!" 

# print(get_custom_html_greeting("James", "Brown"))
# print(get_custom_html_greeting(first="James", last="Brown"))



#Task 4

def wrap_with(tag):
    def decoration(func):
        def wrap(*args, **kwargs):
            result = func(*args, **kwargs)
            wrap_result = f"<{tag}>{result}</{tag}"
            return wrap_result
        return wrap
    return decoration



@wrap_with(tag="strong")
def get_full_name(first="", last=""):
    return f"{first} {last}"  


@wrap_with(tag="em")
def get_html_greeting(i):
    return  i

@wrap_with(tag="p")
@wrap_with(tag="em")
def get_custom_html_greeting(first=" ", last=""):
    full_name = get_full_name(first, last)
    return f"Hello, {full_name}!" 

print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))