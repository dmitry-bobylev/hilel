import pytest

from code_for_testing import Action


@pytest.mark.smoke
def test_age_increment(human):
    human.grow()
    assert human.age == 36


@pytest.mark.regression
@pytest.mark.skip(reason="bug=123")
@pytest.mark.parametrize("name, expected", [("Jill", "bob"), ("Bob", "jack"), ("test", "aslkdj")])
def test_name_changed(human, name, expected):
    human.change_name(name)

    assert human.name == expected


def test_action(human, second_human):
    assert human.action.name == "jumping"
    assert second_human.name == "Jack"

