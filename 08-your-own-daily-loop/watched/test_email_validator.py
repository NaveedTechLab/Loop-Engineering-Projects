import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from email_validator import is_valid_email


def test_valid_email():
    assert is_valid_email("user@example.com") is True


def test_missing_at():
    assert is_valid_email("bad-email") is False


def test_missing_domain():
    assert is_valid_email("user@") is False


def test_missing_local_part():
    assert is_valid_email("@example.com") is False
