class Animal:
    def __init__(self, animal, name):
        self.animal = animal
        self.name = name

    def __str__(self):
        return f"On my farm, the {self.animal} is called {self.name}"

    def speak(self, sound):
        return f"The {self.animal} goes {sound}"

class Chicken(Animal):
    def __init__(self, animal, name, appearance):
        super().__init__(animal, name)
        self.appearance = appearance

    def description(self):
        return f"{self.name} has {self.appearance}"

    def by_product(self):
        return f"{self.name} lays eggs"

class Cow(Animal):
    def __init__(self, animal, name):
        super().__init__(animal, name)

    def by_product(self):
        return f"{self.name} produces milk"

class Donkey(Animal):
    def __init__(self, animal, name):
        super().__init__(animal, name)

    def task(self, burden="small children"):
        return f"{self.name} the {self.animal} carries {burden}"

    def speak(self, sound="hee-haw"):
        return super().speak(sound)


chicken = Chicken("chicken", "Delilah", "green eyes and feathers")
cow = Cow("cow", "Daisy")
donkey = Donkey("donkey", "Elif")

print(chicken)
print(chicken.description())
print(chicken.by_product(), "\n")

print(cow)
print(cow.speak("mooooo"))
print(cow.by_product(), "\n")

print(donkey)
print(donkey.task())
print(donkey.speak())