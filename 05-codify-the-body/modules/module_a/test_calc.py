import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from calc import power


def test_power_basic():
    assert power(2, 3) == 8


def test_power_zero_exponent():
    assert power(5, 0) == 1


def test_power_one_exponent():
    assert power(3, 1) == 3


def test_power_larger():
    assert power(2, 10) == 1024
