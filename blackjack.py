from player import HumanPlayer, AutoPlayer, Player
from stack import Deck, HandBJ


class BlackjackGame:
    def __init__(self, players):
        self.deck = Deck()
        self.dealer_hand = HandBJ()
        self.players = players
        self.players_hands = {player: [] for player in players}
        for player in players:
            self.players_hands[player].append(HandBJ())

    def play(self):
        self.deck.shuffle()
        self.dealer_hand.add_card(self.deck.deal_card())
        print(f"Dealer hand: {self.dealer_hand.value()} {self.dealer_hand}")

        for player in self.players:
            for hand in self.players_hands[player]:
                hand.add_card(self.deck.deal_card())

        self.dealer_hand.add_card(self.deck.deal_card())
        if self.dealer_hand.value() == 21:
            print("Dealer has blackjack!")
            return

        for player in self.players:
            i = 0
            while i < len(self.players_hands[player]):
                hand = self.players_hands[player][i]
                hand.add_card(self.deck.deal_card())
                print(f"Player {self.players.index(player)}:{i} hand: {hand.value()} {hand}")
                if hand.can_split() and player.should_split(hand):
                    new_hand = HandBJ()
                    new_hand.add_card(hand.split())
                    self.players_hands[player].append(new_hand)
                    continue

                while hand.value() < 21:
                    if player.should_hit(hand):
                        hand.add_card(self.deck.deal_card())
                        print(f"Player {self.players.index(player)}:{i} hand: {hand.value()} {hand}")
                    else:
                        print(f"Player {self.players.index(player)}:{i} stands at {hand.value()}")
                        break
                if hand.value() == 21:
                    print(f"Player {self.players.index(player)}:{i} has blackjack!")

                if hand.value() > 21:
                    print(f"Player {self.players.index(player)}:{i} busts!")
                i += 1

        while self.dealer_hand.value() < 17:
            self.dealer_hand.add_card(self.deck.deal_card())

        print(f"Dealer hand: {self.dealer_hand.value()} {self.dealer_hand}")

        for player in self.players:
            hands_won = 0
            hands_pushed = 0
            if self.dealer_hand.value() > 21:
                print("Dealer busts!")
                hands_won = sum(1 for hand in self.players_hands[player] if hand.value() <= 21)
                hands_pushed = sum(1 for hand in self.players_hands[player] if hand.value() > 21)
            else:
                for i, hand in enumerate(self.players_hands[player]):
                    if hand.value() > 21:
                        print(f"Hand {i} loses!")
                    elif self.dealer_hand.value() < hand.value():
                        print(f"Hand {i} wins!")
                        hands_won += 1
                    elif hand.value() < self.dealer_hand.value():
                        print(f"Hand {i} loses!")
                    else:
                        print(f"Hand {i} pushes!")
                        hands_pushed += 1

            print(f"Player {self.players.index(player)} won {hands_won}/{hands_pushed}/{len(self.players_hands[player])} hands")


# Example usage
if __name__ == "__main__":
    player = HumanPlayer()  # Or AIPlayer()
    game = BlackjackGame(player)
    game.play()
