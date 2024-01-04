def add(*arg):
    # *arg sẽ là 1 tuple
    sum = 0
    for number in arg:
        sum += number
    return sum


# print(add(1, 2, 3, 4, 5, 6))
def calculate(n, **kwargs):
    # kwargs là 1 dictonary
    # for key, value in kwargs.items():
    #     print(key, value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        # Dùng get nếu khóa không tồn tại thì trả về None. Và không báo lỗi
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
print(my_car.seats)
