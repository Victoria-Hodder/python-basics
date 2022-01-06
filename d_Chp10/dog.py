
class Dog:

    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"

    def move(self, movement="run"):
        return f"{self.name} moves so {movement}"

class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound)

class GoldenRetriever(Dog):
    def speak(self, sound="Woof"):
        return super().speak(sound)

class Dachshund(Dog):
    species = "some latin word"

class Bulldog(Dog):
    pass

""" Instantiating dogs of different breeds """

miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = GoldenRetriever("Jim", 5)

print(miles.speak())
print(jim.move())
print(buddy.species)
