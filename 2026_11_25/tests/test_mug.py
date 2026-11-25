"""針對 mug 模組的單元測試。
"""

import math
import unittest
from mug import DEFAULT_MUG_CAPACITY_ML, Mug, calculate_cylinder_capacity


class TestMugModule(unittest.TestCase):
    """測試馬克杯模組功能。"""

    def test_calculate_cylinder_capacity_normal(self):
        """測試正常的圓柱體積計算。"""
        # 半徑 4 cm，高 7 cm -> pi * 16 * 7 = 112 * pi ≈ 351.86 ml
        expected = round(math.pi * (4 ** 2) * 7, 2)
        actual = calculate_cylinder_capacity(4.0, 7.0)
        self.assertEqual(actual, expected)

    def test_calculate_cylinder_capacity_invalid_input(self):
        """測試半徑或高為零或負數時引發 ValueError。"""
        with self.assertRaises(ValueError) as ctx1:
            calculate_cylinder_capacity(0, 10)
        self.assertEqual(str(ctx1.exception), "半徑與高度必須大於 0")

        with self.assertRaises(ValueError) as ctx2:
            calculate_cylinder_capacity(4, -5)
        self.assertEqual(str(ctx2.exception), "半徑與高度必須大於 0")

    def test_mug_initialization_default(self):
        """測試 Mug 預設容量初始化。"""
        mug = Mug()
        self.assertEqual(mug.capacity_ml, DEFAULT_MUG_CAPACITY_ML)
        self.assertEqual(mug.current_volume_ml, 0.0)
        self.assertTrue(mug.is_empty())
        self.assertFalse(mug.is_full())

    def test_mug_initialization_custom(self):
        """測試 Mug 自訂容量初始化。"""
        mug = Mug(500.0)
        self.assertEqual(mug.capacity_ml, 500.0)
        self.assertEqual(mug.current_volume_ml, 0.0)

    def test_mug_initialization_invalid_capacity(self):
        """測試無效容量初始化時拋出 ValueError。"""
        with self.assertRaises(ValueError) as ctx:
            Mug(0)
        self.assertEqual(str(ctx.exception), "馬克杯容量必須大於 0 ml")

        with self.assertRaises(ValueError) as ctx2:
            Mug(-100)
        self.assertEqual(str(ctx2.exception), "馬克杯容量必須大於 0 ml")

    def test_mug_fill_and_overflow(self):
        """測試注水與溢出狀況。"""
        mug = Mug(300.0)
        mug.fill(150.0)
        self.assertEqual(mug.current_volume_ml, 150.0)
        self.assertFalse(mug.is_empty())
        self.assertFalse(mug.is_full())

        mug.fill(150.0)
        self.assertEqual(mug.current_volume_ml, 300.0)
        self.assertTrue(mug.is_full())

        # 超過容量時拋出 OverflowError
        with self.assertRaises(OverflowError) as ctx:
            mug.fill(1.0)
        self.assertIn("水溢出來了", str(ctx.exception))

        # 倒入負值或 0 時拋出 ValueError
        with self.assertRaises(ValueError):
            mug.fill(0)

    def test_mug_drink(self):
        """測試喝水功能與倒空狀況。"""
        mug = Mug(350.0)
        mug.refill()
        self.assertTrue(mug.is_full())

        # 喝掉一部分
        drunk = mug.drink(100.0)
        self.assertEqual(drunk, 100.0)
        self.assertEqual(mug.current_volume_ml, 250.0)

        # 喝超過剩餘水量，應該只喝掉剩餘量
        drunk = mug.drink(300.0)
        self.assertEqual(drunk, 250.0)
        self.assertEqual(mug.current_volume_ml, 0.0)
        self.assertTrue(mug.is_empty())

        # 喝無效水量
        with self.assertRaises(ValueError):
            mug.drink(-10)

    def test_mug_empty(self):
        """測試手動倒空功能。"""
        mug = Mug(350.0)
        mug.fill(200.0)
        mug.empty()
        self.assertEqual(mug.current_volume_ml, 0.0)
        self.assertTrue(mug.is_empty())


if __name__ == "__main__":
    unittest.main()
