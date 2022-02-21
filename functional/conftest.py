import pytest

from code_for_testing import Human, Action


@pytest.fixture()
def action():
    action = Action("jumping")
    yield action


@pytest.fixture()
def second_human(action):
    human = Human("Jack", 30, "male", action)
    yield human


@pytest.fixture()
def human(action):
    human = Human("John", 35, "male", action)
    yield human


