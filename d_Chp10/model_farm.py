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

    def fun_fact(self):
        return f"Did you know? Chickens are the closest living relative to the T-Rex"

class Cow(Animal):
    def __init__(self, animal, name, hobby):
        super().__init__(animal, name)
        self.hobby = hobby

    def by_product(self):
        return f"{self.name} produces milk"

    def free_time(self):
        return f"In her free time, {self.name} likes to {self.hobby}"

    def fun_fact(self):
        return f"Did you know? A cow will chew for up to eight hours a day"

class Donkey(Animal):
    def __init__(self, animal, name, fave_food):
        super().__init__(animal, name)
        self.fave_food = fave_food

    def speak(self, sound="hee-haw"):
        return super().speak(sound)

    def task(self, burden="small children"):
        return f"{self.name} the donkey carries {burden}"

    def eat(self):
        return f"{self.name} the donkey likes to eat {self.fave_food}"

    def fun_fact(self):
        return f"Did you know? The smallest donkey recorded is only 19 inches tall"



chicken = Chicken("chicken", "Delilah", "green eyes and feathers")
cow = Cow("cow", "Daisy", "go bungee-jumping")
donkey = Donkey("donkey", "Elif", "cheese burgers")

print(chicken)
print(chicken.description())
print(chicken.by_product(), "\n")

print(cow)
print(cow.by_product())
print(cow.free_time())
print(cow.fun_fact(), "\n")

print(donkey)
print(donkey.eat())
print(donkey.speak())