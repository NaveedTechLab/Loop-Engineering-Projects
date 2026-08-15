import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from strings import slugify


def test_slugify_basic():
    assert slugify("Hello World") == "hello-world"


def test_slugify_strips_punctuation():
    assert slugify("  Pest Control!  ") == "pest-control"


def test_slugify_keeps_numbers():
    assert slugify("Karachi 2026") == "karachi-2026"


def test_slugify_multiple_spaces():
    assert slugify("too   many   spaces") == "too-many-spaces"
