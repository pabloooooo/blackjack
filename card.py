from enum import Enum


class ESuit(Enum):
    HEARTS = '♥'
    DIAMONDS = '♦'
    CLUBS = '♣'
    SPADES = '♠'

    # In Python, the `value` attribute is built-in for Enum members,
    # so we don't need a separate method to get it. However, if you
    # want to keep the method for clarity or consistency, you can add:
    def get_suit(self):
        return self.value


class Card:
    def __init__(self, suit: ESuit, value: int):
        self.suit = suit
        self.value = value

    def __str__(self):
        value_str = {
            1: 'A',
            11: 'J',
            12: 'Q',
            13: 'K'
        }.get(self.value, str(self.value))

        return f"Card{{ {self.suit.value} {value_str} }}"

    def __eq__(self, other):
        if not isinstance(other, Card):
            return False
        return self.value == other.value and self.suit == other.suit

    def __hash__(self):
        return hash((self.suit, self.value))

    def is_ace(self):
        return self.value == 1

    def get_value(self):
        return self.value
