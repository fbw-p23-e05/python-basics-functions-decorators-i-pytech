

"""Task 1"""

    


# def make_bold(func):
    
#     def inner():
        
#         return f'<strong>{func()}</strong>'
    
#     return inner


# @make_bold
# def get_html_greeting():
    
#     return 'Hello, World!'

# print(get_html_greeting())


# print(make_bold(get_html_greeting)())



"""Task 2"""

# def make_bold(func):
    
#     def inner(*a,**b):
        
#         return f'<strong>{func(*a,**b)}</strong>'
    
#     return inner


# @make_bold
# def get_html_greeting():
    
#     return 'Hello, World!'

# @make_bold
# def get_custom_html_greeting(first, last):
    
#     return f'Hello, {first} {last}!'


# print(get_custom_html_greeting("James", "Brown"))
# print(get_custom_html_greeting(first="James", last="Brown"))
# print(get_html_greeting())




"""Task 3"""


# def make_italics(func):
    
#     def inner_italics(*a, **b):
        
#         return f'<em>{func(*a, **b)}</em>'
    
#     return inner_italics

# def make_paragraph(func):
    
#     def inner_parapraph(*a, **b):
        
#         return f'<p>{func(*a, **b)}</p>'
    
#     return inner_parapraph


# def make_bold(func):
    
#     def inner(*a,**b):
        
#         return f'<strong>{func(*a,**b)}</strong>'
    
#     return inner



# @make_bold
# def get_full_name(a, b):
    
#     return a + ' ' + b


# @make_bold
# def get_html_greeting():
    
#     return 'Hello, World!'

# @make_paragraph
# @make_italics
# def get_custom_html_greeting(first, last):
    
#     return f'Hello, {get_full_name(first, last)}!'



# print(get_custom_html_greeting("James", "Brown"))
# print(get_custom_html_greeting(first="James", last="Brown"))



"""Task 4"""

def wrap_with(tag = 'strong'):
    
    def decorator(func):
    
        def inner_wrap(*a, **b):
            
            return f'<{tag}>{func(*a,**b)}</{tag}>'
        
        return inner_wrap
    
    return decorator



@wrap_with(tag='strong')
def get_full_name(a, b):
    
    return a + ' ' + b


def get_html_greeting():
    
    return 'Hello, World!'

@wrap_with(tag='p')
@wrap_with(tag='em')
def get_custom_html_greeting(first, last):
    
    return f'Hello, {get_full_name(first, last)}!'


print(get_custom_html_greeting("James", "Brown"))
print(get_custom_html_greeting(first="James", last="Brown"))


