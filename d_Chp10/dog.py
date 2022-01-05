
class Dog():

    species = "Canis familiaris"

    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


buddy = Dog("Buddy", 9, "black")
miles = Dog("Mile", 4, "green")

print(buddy)
print(miles.speak("'Woof'"))
print(f"{buddy.name}'s coat is {buddy.coat_color}.")
