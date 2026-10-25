class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health = "good"

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def description(self):
        print(self.name)
        print(self.age)


hippo = Animal("Peter", 10)
sloth = Animal("Peteraa", 101)
ocelot = Animal("Peteraaa", 102)
print(hippo.description())
sloth.description())
print(ocelot.description())
