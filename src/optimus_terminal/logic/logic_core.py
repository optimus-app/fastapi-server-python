from optimus_terminal.entity.entity_core import Entity

def set_john():
    entity = Entity("John", 30)

    entity.change_name("Doe")
    entity.change_age(40)

    return entity