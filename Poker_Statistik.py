import Poker as pk
import matplotlib.pyplot as plt
def check_combinations(cards, dic):
    if pk.royal_flush(cards):
        dic["Royal Flush"] += 1
        return
    elif pk.straight_flush(cards):
        dic["Straight Flush"] += 1
        return
    elif pk.four_of_a_kind(cards):
        dic["Four of a kind"] += 1
        return
    elif pk.full_house(cards):
        dic["Full House"] += 1
        return
    elif pk.flush(cards):
        dic["Flush"] += 1
        return
    elif pk.straight(cards):
        dic["Straight"] += 1
        return
    elif pk.three_of_a_kind(cards):
        dic["Three of a kind"] += 1
        return
    elif pk.two_pairs(cards):
        dic["Two Pair"] += 1
        return
    elif pk.pair(cards):
        dic["Pair"] += 1
        return
    else:
        dic["High Card"] += 1
        return

def execute_testing(count=1, numbers_to_draw=5):
    dic = {
    "Royal Flush": 0,
    "Straight Flush": 0,
    "Four of a kind": 0,
    "Full House": 0,
    "Flush": 0,
    "Straight": 0,
    "Three of a kind": 0,
    "Two Pair": 0,
    "Pair": 0,
    "High Card": 0
    }
    propability = {
    "Royal Flush": 0,
    "Straight Flush": 0,
    "Four of a kind": 0,
    "Full House": 0,
    "Flush": 0,
    "Straight": 0,
    "Three of a kind": 0,
    "Two Pair": 0,
    "Pair": 0,
    "High Card": 0
    }
    for i in range(count):
        check_combinations(pk.get_cards(pk.create_cards(),numbers_to_draw), dic)
    print(dic)
    for i in dic:
        propability[i] = (dic[i] / count) * 100
    print(propability)
    ax = plt.subplot()
    ax.pie(list(propability.values()), labels=list(propability.keys()), autopct="%1.5f%%", radius=1.3)
    plt.show()

if (__name__ == "__main__"):
    execute_testing(1_000, 5)