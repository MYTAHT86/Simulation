from map.map import Map
class MakeMapObjects:
    @classmethod
    def process(cls, classname):
        name_creator = f'{classname.__name__}{len(classname.obj_collection) + 1}'
        name = classname(name_creator)
        attr = getattr(name, classname.__name__.lower())
        Map.setup_map_obj(name, attr)
        classname.obj_collection.append(name)      