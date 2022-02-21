from code_for_testing import Human


class TestHuman:

    def setup(self):
        print("\nbefore each test")
        self.human = Human("John", 30, "male")

    def setup_class(self):
        print("\nbefore class")

    def teardown_class(self):
        print("\nteardown class")

    def teardown(self):
        print("\nafter each test")

    def test_age(self):
        self.human.grow()
        assert self.human.age == 31

    def test_name_changed(self):
        self.human.change_name("Jack")
        assert self.human.name == "Jack"
