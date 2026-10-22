from abc import ABC
class Entity(ABC):
    def __init__(self, name):
        self.name = name
    def __init_subclass__(cls):
        cls.obj_collection = []
    def __repr__(self):
        return f'{self.name}'
    def delete_instance(self):
        self.__class__.obj_collection.remove(self)