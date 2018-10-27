import math


class Demo:

    def hello_world(self):
        return 'PyLadies!'

    def quadratic_formula(self, a, b, c):
        d = b ** 2 - 4 * a * c
        if d >= 0:
            disc = math.sqrt(d)
            root1 = (-b + disc) / (2 * a)
            root2 = (-b - disc) / (2 * a)
            return root1, root2
        else:
            raise Exception
