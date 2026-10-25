class Car(object):

    def __init__(self, model: str, color: str, mpg: int):
        self.condition = "new"
        self.model = model
        self.color = color
        self.mpg = mpg

    def display_car(self):
        print("This is a % s % swith % s MPG." %
              (self.color, self.model, str(self.mpg)))

    def drive_car(self):
        self.condition = "used"

class ElectricCar(Car):
    def __init__(self, battery_type: str, model: str, color: str, mpg: int):
        # 使用 super() 调用父类 Car 的 __init__，初始化 model, color, mpg 和 condition
        super().__init__(model, color, mpg)
        # 为 ElectricCar 独有的属性赋值
        self.battery_type = battery_type
my_car = ElectricCar("molten salt", "DeLorean", "silver", 88)
