class BuildingError(Exception):

    def __str__(self):
        return f"Whitch so much material the house cannot build!"


def check_material(amout_of_material, limit_material):
    if amout_of_material > limit_material:
        return  "enogh material"
    else:
        raise BufferError

material = 323
check_material(material, 300)