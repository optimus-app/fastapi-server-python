from typing import Optional

class Entity:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def change_name(self, new_name: Optional[str] = None):
        self.name = new_name

    def change_age(self, new_age: Optional[int] = None):
        self.age = new_age