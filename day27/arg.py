def add(*arg):
    # *arg sẽ là 1 tuple
    print(type(arg))
    print(arg)
    sum = 0
    for number in arg:
        sum += number

    return sum


print(add(1, 2, 3, 4, 5, 6))
