order = "AKQT98765432J"

f = open("input.txt", "r")
line = f.readline()

hands = []

while line and line != "":
    hand, bid = line.split()
    bid = int(bid)
    cards = {
        "A": 0,
        "K": 0,
        "Q": 0,
        "J": 0,
        "T": 0,
        "9": 0,
        "8": 0,
        "7": 0,
        "6": 0,
        "5": 0,
        "4": 0,
        "3": 0,
        "2": 0,
    }

    score = []
    for card in hand:
        cards[card] += 1
        score.append(order[::-1].index(card))

    numJ = cards.pop("J")
    nums = [v for k, v in cards.items() if v > 0]
    nums = sorted(nums, reverse=True)
    val = 0
    if numJ == 5:
        val = 6
    else:
        high = nums[0] + numJ

        if high == 5:
            val = 6
        elif high == 4:
            val = 5
        elif high == 3:
            nums.pop(0)
            if max(nums) == 2:
                val = 4
            else:
                val = 3
        elif high == 2:
            nums.pop(0)
            if max(nums) == 2:
                val = 2
            else:
                val = 1

    hands.append((val, score, bid))
    line = f.readline()

sorted_hands = sorted(hands, key=lambda tup: (tup[0], tup[1][:]))
scores = [(i + 1) * x[2] for i, x in enumerate(sorted_hands)]
print(sum(scores))
