import unittest
from app import add_numbers, subtract_numbers, multiply_numbers, divide_numbers

class TestMathFunctions(unittest.TestCase):
  def test_add_numbers(self):
    self.assertEqual(add_numbers(5, 3), 8)
    self.assertEqual(add_numbers(-1, 1), 0)
    self.assertEqual(add_numbers(0, 0), 0)

  def test_subtract_numbers(self):
    self.assertEqual(subtract_numbers(5, 3), 2)
    self.assertEqual(subtract_numbers(-1, 1), -2)
    self.assertEqual(subtract_numbers(0, 0), 0)

  def test_multiply_numbers(self):
    self.assertEqual(multiply_numbers(5, 3), 15)
    self.assertEqual(multiply_numbers(-1, 1), -1)
    self.assertEqual(multiply_numbers(0, 5), 0)

  def test_divide_numbers(self):
    self.assertEqual(divide_numbers(6, 3), 2.0)
    self.assertEqual(divide_numbers(5, 2), 2.5)
    self.assertEqual(divide_numbers(0, 5), 0.0)
    with self.assertRaises(ValueError):
      divide_numbers(5, 0)

if __name__ == "__main__":
  unittest.main()
