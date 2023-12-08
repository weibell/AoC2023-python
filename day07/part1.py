with open('input.txt', 'r') as f:
    input_data = f.read().splitlines()


def hand_type(hand: str) -> int:
    ordered_types = [
        [5],             # Five of a kind
        [4, 1],          # Four of a kind
        [3, 2],          # Full house
        [3, 1, 1],       # Three of a kind
        [2, 2, 1],       # Two pair
        [2, 1, 1, 1],    # One pair
        [1, 1, 1, 1, 1]  # High card
    ]
    label_counts = [hand.count(card) for card in set(hand)]
    label_counts.sort(reverse=True)
    return ordered_types.index(label_counts)


def cards_as_int(hand: str) -> tuple:
    ordered_labels = 'AKQJT98765432'
    return (ordered_labels.index(card) for card in hand)


hands = []  # (sortable) tuples of type, card values and bid
for line in input_data:
    hand, bid = line.split(' ')
    encoded_hand = (
        hand_type(hand),
        *cards_as_int(hand),
        int(bid)
    )
    hands.append(encoded_hand)

hands.sort(reverse=True)
winnings = sum(rank * hand[-1]  # rank * bid
               for rank, hand in enumerate(hands, start=1))

print(winnings)
