"""
strings.py — module B. One function, one bug.
"""


def slugify(text: str) -> str:
    """Convert text into a URL-friendly slug.

    - lowercase everything
    - replace spaces with hyphens
    - strip anything that isn't a letter, digit, or hyphen

    slugify("Hello World")      -> "hello-world"
    slugify("  Pest Control!  ") -> "pest-control"
    slugify("Karachi 2026")      -> "karachi-2026"
    """
    import re

    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    text = re.sub(r"[\s-]+", "-", text)
    return text.strip("-")
