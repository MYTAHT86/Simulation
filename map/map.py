import random
class Map:
    free_slots = [(vertical, horizontal) for vertical in range(16) for horizontal in range(16)]
    collection = {}
    @classmethod
    def herbivore_eat_on_map(cls, instance, nearest_grass):
        current_location = Map.find_current_slot(instance)
        Map.map[current_location[0]][current_location[1]] = '.'
        Map.add_free_slot(current_location)
        Map.delete_on_map(current_location)
        Map.collection[instance.nearest_grass[0]] = instance
        Map.map[instance.nearest_grass[0][0]][instance.nearest_grass[0][1]] = instance.herbivore
    @classmethod
    def herbivore_move_on_map(cls, instance, current_location, step_to_make):
        Map.map[current_location[0]][current_location[1]] = '.'
        Map.add_free_slot(current_location)
        Map.delete_on_map(current_location, step_to_make)
        Map.map[step_to_make[0]][step_to_make[1]] = instance.herbivore
        Map.collection[step_to_make] = instance
    @classmethod
    def predator_move_on_map(cls, instance, current_location, step_to_make):
        Map.map[current_location[0]][current_location[1]] = '.'
        Map.add_free_slot(current_location)
        Map.delete_on_map(current_location, step_to_make)
        Map.map[step_to_make[0]][step_to_make[1]] = instance.predator
        Map.collection[step_to_make] = instance
    @classmethod
    def delete_on_map(cls, current_location, step_to_make=None):
        if step_to_make:
            del Map.collection[current_location]
            Map.free_slots.remove(step_to_make)
        else:
            del Map.collection[current_location]
    @classmethod
    def find_current_slot(cls, instance):
        return next(k for k, v in Map.collection.items() if v == instance)
    @classmethod
    def isinstance_check(cls, current_slot, vertical, horizontal, classname):
        return isinstance(Map.collection.get((current_slot[0] + vertical, current_slot[1]  + horizontal)), classname)
    @classmethod
    def slots_check(cls, current_slot, vertical, horizontal):
        return (current_slot[0] + vertical, current_slot[1]  + horizontal) not in Map.collection.keys()
    @classmethod
    def find_instance(cls, location):
        return Map.collection[location]
    @classmethod
    def change_instance_on_map(cls, instance, value=None):
         Map.collection[instance.nearest_grass[0]] = value
    @classmethod
    def delete_instance_on_map(cls, location):
        Map.map[location[0]][location[1]] = '.'
    @classmethod
    def check_location(cls, location):
        return location in Map.collection.keys()
    @classmethod
    def add_free_slot(cls, location):
        Map.free_slots.append(location)
    @classmethod
    def setup_map_obj(cls, name, attr):
        position = random.choice(Map.free_slots)
        Map.collection[position] = name
        Map.map[position[0]][position[1]] = attr
        Map.free_slots.remove(position)