import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from service_fee import calculate_late_fee


def test_no_fee_when_not_late():
    assert calculate_late_fee(0) == 0.0


def test_fee_scales_with_days():
    assert calculate_late_fee(3) == 15.0


def test_fee_capped_at_ten_days():
    assert calculate_late_fee(20) == 50.0
