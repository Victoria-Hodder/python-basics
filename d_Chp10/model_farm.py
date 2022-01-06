class Animal:
    def __init__(self, animal, name, sound, walk_style):
        self.animal = animal
        self.name = name
        self.sound = sound
        self.walk_style = walk_style

    def introduction(self):
        return f"On my farm, the {self.animal} is called {self.name}"

    def speak(self):
        return f"{self.name} the {self.animal} goes {self.sound}"

    def move(self):
        return f"{self.name} the {self.animal} walks {self.walk_style}"

chicken = Animal("chicken", "Delilah", "cluck", "quickly")
cow = Animal("cow", "Daisy", "moo", "slowly")
donkey = Animal("donkey", "Elif", "eeyore", "stubbornly")


print(chicken.introduction())
print(chicken.speak())
print(chicken.move())

print(donkey.introduction())
print(donkey.speak())
print(donkey.move())