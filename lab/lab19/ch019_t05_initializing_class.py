class Car(object):

    def __init__(self, model: str, color: str , mpg: int):
        self.condition = "new"
        model = "DeLorean"
        color = "silver"
        mpg = 88


my_car = Car()
print(my_car.condition)
