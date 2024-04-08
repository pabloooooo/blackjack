from abc import ABC, abstractmethod


class Player(ABC):
    @abstractmethod
    def should_hit(self, hand):
        pass

    @abstractmethod
    def should_split(self, hand):
        pass


class HumanPlayer(Player):
    def should_hit(self, hand):
        return input("Do you want to hit? (y/n) ").strip().lower() == 'y'

    def should_split(self, hand):
        return input("Do you want to split? (y/n) ").strip().lower() == 'y'


class AIPlayer(Player):
    def should_hit(self, hand):
        return hand.value() < 17

    def should_split(self, hand):
        return hand.can_split()
