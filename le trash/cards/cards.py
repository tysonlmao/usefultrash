import json

def deck():
    with open('data.json') as f:
        cards = json.load(f)
    return cards

cards = deck()
# for i in range(len(deck())):
count = 0



for i in cards:
    # print(cards[i])
    color = cards[i]
    for suit in color:
        for card in color[suit]:
            count = count+1
            # print(str(cards[i]) + str(color[suit]))
print(cards[0][2][8])
print(count)

# print(deck())