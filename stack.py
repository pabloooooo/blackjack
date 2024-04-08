from card import Card, ESuit


class HandBJ:
    def __init__(self):
        self.stack = []

    def add_card(self, card):
        self.stack.append(card)

    def can_split(self):
        return len(self.stack) == 2 and self.get_card_value(self.stack[0]) == self.get_card_value(self.stack[1])

    def value(self):
        temp_stack = sorted(self.stack, key=lambda card: card.get_value())
        value = 0
        aces_count = sum(1 for card in self.stack if card.is_ace())

        for card in temp_stack:
            value += self.get_card_value(card)

        while value > 21 and aces_count > 0:
            value -= 10
            aces_count -= 1

        return value

    @staticmethod
    def get_card_value(card):
        return 11 if card.get_value() == 1 else min(card.get_value(), 10)

    def split(self):
        return self.stack.pop(1)

    def __str__(self):
        return f"HandBJ{{ stack=[{', '.join(str(card) for card in self.stack)}] }}"


import random


class Deck:
    def __init__(self):
        self.cards = [Card(suit, value) for suit in ESuit for value in range(1, 14)]
        self.top_card_index = 0

    def shuffle(self):
        random.shuffle(self.cards)

    def deal_card(self):
        card = self.cards[self.top_card_index]
        self.top_card_index += 1
        return card

    def can_deal(self):
        return self.top_card_index < len(self.cards)
