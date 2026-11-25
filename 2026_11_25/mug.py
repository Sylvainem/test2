"""馬克杯容量計算與狀態管理模組。

提供幾何容積計算功能以及 Mug 類別以模擬水量狀態管理。
"""

import math

# 常見標準馬克杯容量常數（毫升 / ml）
DEFAULT_MUG_CAPACITY_ML: float = 350.0


def calculate_cylinder_capacity(radius_cm: float, height_cm: float) -> float:
    """以內徑半徑與內高（公分）計算圓柱形馬克杯的容積（毫升 / ml）。

    1 立方公分 (cm³) 等於 1 毫升 (ml)。
    
    Args:
        radius_cm: 圓柱內徑半徑（公分）。
        height_cm: 圓柱內高（公分）。

    Returns:
        float: 計算所得的容積（毫升），四捨五入至小數點後兩位。

    Raises:
        ValueError: 當半徑或高度小於或等於 0 時拋出。
    """
    if radius_cm <= 0 or height_cm <= 0:
        raise ValueError("半徑與高度必須大於 0")
    volume = math.pi * (radius_cm ** 2) * height_cm
    return round(volume, 2)


class Mug:
    """馬克杯類別，負責管理馬克杯容量與當前水量狀態。"""

    def __init__(self, capacity_ml: float = DEFAULT_MUG_CAPACITY_ML):
        """初始化馬克杯。
        
        Args:
            capacity_ml: 馬克杯總容量（毫升），預設為 350 ml。

        Raises:
            ValueError: 若容量小於或等於 0 時拋出。
        """
        if capacity_ml <= 0:
            raise ValueError("馬克杯容量必須大於 0 ml")
        self._capacity_ml: float = float(capacity_ml)
        self._current_volume_ml: float = 0.0

    @property
    def capacity_ml(self) -> float:
        """取得馬克杯總容量（毫升）。"""
        return self._capacity_ml

    @property
    def current_volume_ml(self) -> float:
        """取得當前水量（毫升）。"""
        return self._current_volume_ml

    def fill(self, amount_ml: float) -> None:
        """向馬克杯倒入指定毫升的水。
        
        Args:
            amount_ml: 倒入的水量（毫升）。

        Raises:
            ValueError: 若倒入水量小於或等於 0 時拋出。
            OverflowError: 若倒入後超過馬克杯容量時拋出。
        """
        if amount_ml <= 0:
            raise ValueError("倒入的水量必須大於 0 ml")
        if self._current_volume_ml + amount_ml > self._capacity_ml:
            raise OverflowError("水溢出來了！超出馬克杯容量")
        self._current_volume_ml += amount_ml

    def drink(self, amount_ml: float) -> float:
        """從馬克杯喝掉指定毫升的水。
        
        Args:
            amount_ml: 欲喝掉的水量（毫升）。

        Returns:
            float: 實際喝掉的水量（毫升）。

        Raises:
            ValueError: 若喝水量小於或等於 0 時拋出。
        """
        if amount_ml <= 0:
            raise ValueError("喝掉的水量必須大於 0 ml")
        actual_drunk = min(amount_ml, self._current_volume_ml)
        self._current_volume_ml -= actual_drunk
        return actual_drunk

    def refill(self) -> None:
        """將馬克杯注滿至上限。"""
        self._current_volume_ml = self._capacity_ml

    def empty(self) -> None:
        """將馬克杯倒空。"""
        self._current_volume_ml = 0.0

    def is_empty(self) -> bool:
        """檢查馬克杯是否為空。"""
        return self._current_volume_ml == 0.0

    def is_full(self) -> bool:
        """檢查馬克杯是否已滿。"""
        return self._current_volume_ml >= self._capacity_ml
