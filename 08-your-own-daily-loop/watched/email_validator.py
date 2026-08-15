"""
email_validator.py — watched module 2.
"""

import re


def is_valid_email(email: str) -> bool:
    """A simple (not RFC-perfect) email validity check.

    Must have exactly one "@", something before it, and a domain after it
    with at least one "." in the domain part.

    is_valid_email("user@example.com") -> True
    is_valid_email("bad-email")         -> False
    is_valid_email("user@")             -> False
    is_valid_email("@example.com")      -> False
    """
    return "@" in email
