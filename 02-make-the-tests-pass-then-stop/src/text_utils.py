"""
text_utils.py — a small text-processing library.

Five functions live here. Some of them have bugs. Your job (or the agent's
job, once you hand this to /goal) is to make every test in
tests/test_text_utils.py pass, without changing the tests.
"""


def reverse_words(sentence: str) -> str:
    """Reverse the ORDER of the words in a sentence (not the letters).

    "the quick brown fox" -> "fox brown quick the"
    """
    words = sentence.split()
    return " ".join(reversed(words))


def count_vowels(text: str) -> int:
    """Count vowels (a, e, i, o, u), counting both upper and lower case."""
    vowels = "aeiou"
    return sum(1 for ch in text.lower() if ch in vowels)


def is_palindrome(text: str) -> bool:
    """True if the text reads the same forwards and backwards.

    Ignore case, spaces, and punctuation. "A man a plan a canal Panama"
    should count as a palindrome.
    """
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


def capitalize_each_word(text: str) -> str:
    """Capitalize the first letter of EVERY word, not just the first word.

    "the quick brown fox" -> "The Quick Brown Fox"
    """
    return " ".join(word.capitalize() for word in text.split(" "))


def truncate(text: str, max_length: int) -> str:
    """Truncate text to at most max_length characters.

    If truncation actually happened, the result must end in "..." and the
    TOTAL length (including the "...") must not exceed max_length.
    If the text already fits, return it unchanged.
    """
    if len(text) <= max_length:
        return text
    return text[: max_length - 3] + "..."
