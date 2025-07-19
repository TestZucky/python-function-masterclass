# x = 10 # global variable

# def change():
#     global x
#     x = 20 # local variable
#     print(x)


# change()
# print(x)

# def outer():

#     x = 'hello'

#     def inner():
#         nonlocal x
#         x = 'world'

#     inner()
#     print(x)

# outer()

# PSRO --> Python scope resolution order (LEGB rule)

x = 'global'

def outer():

    # x = 'enclosing'

    def inner():
        # x = 'local'
        print(x)

    inner()

outer()