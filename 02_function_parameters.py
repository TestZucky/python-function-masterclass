# parameters
def greet(name):
    """
    This method is greeting the user.
    """
    print(f'hello {name}...')

greet('john')

# # postional arguments

# def greet(name: str, age: int):
#     print(f'hello {name} and your age is {age}')

# greet('John', 20)

# # keyword arguments

# def greet(name: str, age: int):
#     print(f'hello {name} and your age is {age}')

# greet(age=20, name='John')

# # deafult arguments

# def greet(name: str, age: int = 20):
#     print(f'hello {name} and your age is {age}')

# greet(name='John')

# # variable length arguments
# # *args

# def total(*args):
#     print(args)
#     res = sum(args)
#     print(res)

# total(10,20,30,50,100)


# # **kwargs

# def show_user(**kwargs):
#     for key, val in kwargs.items():
#         print(f'{key} --> {val}')

# # show_user(name='neeraj', age=10, city='delhi')

# def test(a, b=2, *args, **kwargs):
#     print(f'a = {a}, b = {b}')
#     print(f'args - {args}')
#     print(f'kwargs - {kwargs}')

# test(10, 20, 30, 40, x=100, y=200, z=300)


# # postional --> default --> *args --> keyword-only --> **kwargs 

def original(a, b, c):
    print(a,b, c)

def wrapper(*args, **kwargs):
    original(*args, **kwargs)

wrapper(10,20, 30)
