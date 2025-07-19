def countdown(n):

    if n == 0:
        print('blast off')
        return

    print(n)
    countdown(n-1)


countdown(3)