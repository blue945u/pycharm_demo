from unittest import TestCase
from my_module import hello_module


class TestDemo(TestCase):
    def test_hello_world(self):
        demo = hello_module.Demo()
        self.assertEqual('PyLadies!', demo.hello_world())

    def test_quadratic_formula_correct(self):
        demo = hello_module.Demo()
        self.assertEqual((0.0, -2.0), demo.quadratic_formula(2, 4, 0))

    def test_quadratic_formula_exception(self):
        demo = hello_module.Demo()
        self.assertRaises(Exception, demo.quadratic_formula, 2, 2, 2)
