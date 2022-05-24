class Card:
    def __init__(self, value, suit) -> None:
        values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        suits = {"s":"spade", "c":"club", "h":"heart","d":"diamond"}
        shapes = {"s":"♠","c":"♣","h":"♥","d":"♦"}

        assert str(value) in values, "Value must be in [A, 2-10, J, Q, K]"
        assert suit in suits, "Suit must be in [s, c, h, d]"

        self.value = str(value)
        self.suit  = suits[suit]
        self.shape = shapes[suit]

    def __repr__(self) -> str:
        return f"Card({self.value}, {self.suit})"

    def __str__(self) -> str:
        return f"{self.value} of {self.suit}"
    
    def show(self):
        print('┌───────┐')
        print(f'| {self.value:<2}    |')
        print('|       |')
        print(f'|   {self.shape}   |')
        print('|       |')
        print(f'|    {self.value:>2} |')
        print('└───────┘') 


# card = Card(3, 'd')
# print(card)
# card.show()
