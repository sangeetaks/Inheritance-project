# Lessons on inheritance

class Animal:
    def __init__(self):
        self.eye_count = 2

    def breath(self):
        print("inhale, exhale")


#Fish class is inheriting from Animal class , so its mentioned inside closed braces and super() keyword is also used
class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        print("moving in water")

    def breath(self):
        super().breath()
        print("doing this inside water")


nemo = Fish()
print(nemo.eye_count)
nemo.breath()
nemo.swim()
