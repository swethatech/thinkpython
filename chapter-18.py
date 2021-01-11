#Exercise 18.1

'''class Time(object):
    def __init__(self, hour=0, minute=0):
        self.hour = hour
        self.minute = minute

    def __lt__(self, other):
      return (self.hour, self.minute) < (other.hour, other.minute)

    def __gt__(self, other):
      return (self.hour, self.minute) > (other.hour, other.minute)

    def __eq__(self, other):
      return (self.hour, self.minute) == (other.hour, other.minute)

    def __repr__(self):
      return '{}'.format((self.hour, self.minute))

a = Time(hour=3, minute=31)
b = Time(hour=4, minute=30)

print(a < b)'''



#Exercise 18.2

'''from random import shuffle


class Card(object):
    """Represents a standard playing card."""

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __repr__(self):
        return 'Card <{}, {}>'.format(self.rank_names[self.rank], self.suit_names[self.suit])

    # I'm using the following 'rich comparison' methods in place of __cmp__
    # https://docs.python.org/2/reference/datamodel.html#object.__lt__

    def __lt__(self, other):
        return self.rank < other.rank

    def __gt__(self, other):
        return self.rank > other.rank

    def __eq__(self, other):
        return self.rank == other.rank


class Deck(object):
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in range(4) for rank in range(1, 14)]

    def __str__(self):
        return '\n'.join([str(card) for card in self.cards])

    def __repr__(self):
        return "Deck <{}>".format(self.cards)

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        shuffle(self.cards)
        return "deck has been shuffled."

    def sort(self):
        self.cards.sort()
        return "deck has been sorted."


deck = Deck()
deck.shuffle()
deck
deck.sort()
print(deck)'''


#Exercise 18.3

'''from random import shuffle

class Card(object):
    """Represents a standard playing card."""

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                  '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank],
                             Card.suit_names[self.suit])

    def __repr__(self):
        return 'Card <{}, {}>'.format(self.rank_names[self.rank], self.suit_names[self.suit])

    # I'm using the following 'rich comparison' methods in place of __cmp__ 
    # https://docs.python.org/2/reference/datamodel.html#object.__lt__

    def __lt__(self, other):
        return self.rank < other.rank

    def __gt__(self, other):
        return self.rank > other.rank

    def __eq__(self, other):
        return self.rank == other.rank


class Deck(object):
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in range(4) for rank in range(1, 14)]

    def __str__(self):
        return '\n'.join([str(card) for card in self.cards])

    def __repr__(self):
        return "Deck <{}>".format(self.cards)

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        shuffle(self.cards)
        return "deck has been shuffled."

    def sort(self):
        self.cards.sort()
        return "deck has been sorted."

    def deal_hands(self, num_of_hands, cards_per_hand):
        if (num_of_hands * cards_per_hand) > len(self):
            msg = '\n{} hands with {} cards each is {} cards\
            \nTotal cards left in deck: {}'.format(num_of_hands, cards_per_hand, num_of_hands * cards_per_hand,
                                                   len(self))
            raise ValueError(msg)
        else:
            hands = []
            for h in range(num_of_hands):
                hand = Hand()
                for c in range(cards_per_hand):
                    hand.cards.append(self.cards.pop())
                hands.append(hand)
            return hands


class Hand(object):
    def __init__(self):
        self.cards = []

    def __repr__(self):
        return "Hand <{}>".format(self.cards)'''


