"""Just pure, general-purpose functions for MotD"""
import random


def random_quote(messages):
    pick_one = random.randint(0, len(messages) - 1)
    return messages[pick_one]
