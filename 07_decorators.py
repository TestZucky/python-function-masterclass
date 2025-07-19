'''
Syntax:

def decorator(original_function):
    def wrapper():
        print('before call')

        original_function()

        print('after call)
    return wrapper

@decorator
def say_hello():
    print('hello')

say_hello()


'''

def modify_greet(func):

    def wrapper():
        print('before greet')
        func()
        print('after greet')
    return wrapper


@modify_greet
def greet():
    print('hello youtube...') 
    # greet = modify_greet(greet) 
    # greet = modify_greet(greet) --> wrapper()


print('entry point')
greet()
