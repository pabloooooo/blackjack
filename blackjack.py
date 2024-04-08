from player import HumanPlayer, AIPlayer, Player
from stack import Deck, HandBJ


class BlackjackGame:
    def __init__(self, playerr):
        self.deck = Deck()
        self.player_hands = [HandBJ()]
        self.dealer_hand = HandBJ()
        self.player = playerr

    def play(self):
        self.deck.shuffle()
        self.dealer_hand.add_card(self.deck.deal_card())
        print(f"Dealer hand: {self.dealer_hand.value()} {self.dealer_hand}")
        for hand in self.player_hands:
            hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())
        if self.dealer_hand.value() == 21:
            print("Dealer has blackjack!")
            return

        i = 0
        while i < len(self.player_hands):
            hand = self.player_hands[i]
            hand.add_card(self.deck.deal_card())
            print(f"Player {i} hand: {hand.value()} {hand}")
            if hand.can_split() and self.player.should_split(hand):
                new_hand = HandBJ()
                new_hand.add_card(hand.split())
                self.player_hands.append(new_hand)
                continue

            while hand.value() < 21:
                if self.player.should_hit(hand):
                    hand.add_card(self.deck.deal_card())
                    print(f"Player {i} hand: {hand.value()} {hand}")
                else:
                    print(f"Player {i} stands at {hand.value()}")
                    break

            if hand.value() > 21:
                print(f"Player {i} busts!")
            i += 1

        while self.dealer_hand.value() < 17:
            self.dealer_hand.add_card(self.deck.deal_card())

        print(f"Dealer hand: {self.dealer_hand.value()} {self.dealer_hand}")
        hands_won = 0
        if self.dealer_hand.value() > 21:
            print("Dealer busts!")
            hands_won = sum(1 for hand in self.player_hands if hand.value() <= 21)
        else:
            for i, hand in enumerate(self.player_hands):
                if hand.value() > 21:
                    print(f"Player {i} loses!")
                elif self.dealer_hand.value() < hand.value():
                    print(f"Player {i} wins!")
                    hands_won += 2
                elif hand.value() < self.dealer_hand.value():
                    print(f"Player {i} loses!")
                else:
                    print(f"Player {i} pushes!")
                    hands_won += 1

        print(f"Player won {hands_won} hands")


# Example usage
if __name__ == "__main__":
    player = HumanPlayer()  # Or AIPlayer()
    game = BlackjackGame(player)
    game.play()
