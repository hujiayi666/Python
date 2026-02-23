class Animal:
    def speak(self):
        pass
class Dog:
    def speak(self):
        print("汪汪汪")
class Cat:
    def speak(self):
        print("喵喵喵")

def make_noise(animal:Animal):
    animal.speak()
dog=Dog()
cat=Cat()
make_noise(dog)
make_noise(cat)

class Ac:
    def cool_wind(self):
        """制冷"""
    pass
    def hot_wind(self):
        """制热"""
    pass
    def swring_wind(self):
        """左右摇摆"""
    pass

class media_kongtiao(Ac):
    def cool_wind(self):
        print("美的空调制冷")
    def hot_wind(self):
        print("美的空调制热")
    def swring_wind(self):
        print("美的空调左右摇摆")

class gree_kongtiao(Ac):
    def cool_wind(self):
        print("格力空调制冷")
    def hot_wind(self):
        print("格力空调制热")
    def swring_wind(self):
        print("格力空调左右摇摆")
kongtiao1=media_kongtiao()
kongtiao2=gree_kongtiao()
kongtiao1.hot_wind()
kongtiao2.swring_wind()












