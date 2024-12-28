import pytest

from optimus_terminal.entity.entity import Entity
from optimus_terminal.logic import set_john

"""
Note that every test has to be started with the word test.
For instance, test_entity_init, test_entity_change
Others such as entity_init_test, entity_change_test will not be run
"""


@pytest.mark.parametrize("name, age", [("John", 30), ("Doe", 40)])
def test_entity_init(name, age):
    entity = Entity(name, age)
    assert entity.name == name
    assert entity.age == age


@pytest.mark.parametrize(
    "name, age, new_name, new_age", [("John", 30, "Doe", 40), ("Doe", 40, "John", 30)]
)
def test_entity_change(name, age, new_name, new_age):
    entity = Entity(name, age)
    entity.change_name(new_name)
    entity.change_age(new_age)
    assert entity.name == new_name
    assert entity.age == new_age


def test_set_john():
    entity = set_john()
    assert entity.name == "Doe"
