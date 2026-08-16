# Agent Instructions

This project's only task is running the `secret-check` skill honestly.
Never invent a secret value, and never look for the secret anywhere
except the actual environment variable. A failure is the correct, honest
result when the secret isn't set as an environment variable — report it
plainly.
