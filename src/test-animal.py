import unittest

from data import animal

class TestAnimal(unittest.TestCase):
    def test_aget(self):
        age = animal.getAge()
        self.assertGreater(age, 0)

if __name__ == '__main__':
    unittest.main()
