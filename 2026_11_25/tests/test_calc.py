import unittest
from calc import add, subtract, multiply, divide


class TestCalc(unittest.TestCase):
    """測試 calc 模組之功能。"""

    def test_add(self):
        """測試加法。"""
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

    def test_subtract(self):
        """測試減法。"""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(0, 5), -5)

    def test_multiply(self):
        """測試乘法。"""
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 3), -6)

    def test_divide(self):
        """測試正常除法。"""
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(5, 2), 2.5)
        self.assertEqual(divide(-6, 2), -3)

    def test_divide_by_zero(self):
        """測試除數為零時拋出 ValueError("除數不可為零")。"""
        with self.assertRaises(ValueError) as context:
            divide(10, 0)
        self.assertEqual(str(context.exception), "除數不可為零")


if __name__ == "__main__":
    unittest.main()
