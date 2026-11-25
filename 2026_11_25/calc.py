"""計算機模組，提供基礎數學運算功能。
"""


def add(a, b):
    """回傳 a 與 b 相加的結果。"""
    return a + b


def subtract(a, b):
    """回傳 a 減去 b 的結果。"""
    return a - b


def multiply(a, b):
    """回傳 a 與 b 相乘的結果。"""
    return a * b


def divide(a, b):
    """計算兩數相除。
    
    當除數 b 為 0 時，拋出 ValueError("除數不可為零")。
    """
    if b == 0:
        raise ValueError("除數不可為零")
    return a / b
