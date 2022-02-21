

class Action:
    def __init__(self, name):
        self.name = name


class Human:
    def __init__(self, name: str, age: int, gender: str, action: Action):
        self.name = name
        self.age = age
        self.gender = gender
        self.action = action

    def grow(self):
        self.age += 1

    def change_name(self, new_name):
        self.name = new_name
