fib_input_user = int(input('Input Fibonnachi number: '))


def fib(fib_input_user):
    if fib_input_user == 0:
        return 0
    if fib_input_user == 1:
        return 1
    else:
        return fib(fib_input_user - 1) + fib(fib_input_user - 2)


print(fib(fib_input_user))
