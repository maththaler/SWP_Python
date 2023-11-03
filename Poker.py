import random
import collections
import matplotlib.pyplot as plt
count_color = 4
count_symbols = 13
def create_cards ():
    return [a for a in range(count_color*count_symbols)]

def swap_positions(pos1, pos2, list):
    list[pos1], list[pos2] = list[pos2], list[pos1]
            

def get_cards(list, numbers_to_draw):
    for i in range(numbers_to_draw):
        draw = random.randint(0, len(list) - 1 - i)
        swap_positions(draw, len(list) - 1 - i, list)
    return list[-numbers_to_draw:]

def get_symbol_and_color(cards):
    symbols = []
    colors = []
    for card in cards:
        symbols.append(card % count_symbols)
        colors.append(card // count_symbols)
    return symbols, colors 

def pair(cards : list):
    symbols = get_symbol_and_color(cards)[0]
    return any(a == 2 for a in collections.Counter(symbols).values())

def two_pairs (cards : list):
    symbols = get_symbol_and_color(cards)[0]
    counter = 0
    for i in collections.Counter(symbols).values():
        if i == 2:
            counter += 1
    return counter == 2

def three_of_a_kind(cards : list):
    symbols = get_symbol_and_color(cards)[0]
    return any(a == 3 for a in collections.Counter(symbols).values())

def straight(cards):
    symbols = get_symbol_and_color(cards)[0]
    symbols.sort()
    if 0 in symbols and\
       12 in symbols and\
       11 in symbols and\
       10 in symbols and\
       9 in symbols:
        return True
    for i in range(len(cards) - 4):
        cards_straight = symbols[i:i+5]
        for a in range(1, 5):
            if cards_straight[a] - cards_straight[a - 1] != 1:
                break
        else: #Else bezieht sich auf die loop (Wenn kein Break)
            return True
    return False

def flush(cards):
    colors = get_symbol_and_color(cards)[1]
    return any(a >= 5 for a in collections.Counter(colors).values())

def full_house(cards):
    symbols = get_symbol_and_color(cards)[0]
    return any(a == 3 for a in collections.Counter(symbols).values())\
        and any(a == 2 for a in collections.Counter(symbols).values())

def four_of_a_kind(cards : list):
    symbols = get_symbol_and_color(cards)[0]
    return any(a == 4 for a in collections.Counter(symbols).values())

def straight_flush(cards):
    return flush(cards) and straight(cards)
    

def royal_flush(cards):
    symbols = get_symbol_and_color(cards)[0]
    return flush(cards) and straight(cards) and (0 in symbols and\
            12 in symbols and\
            11 in symbols and\
            10 in symbols and\
            9 in symbols)


def check_combinations(cards, dic):
    if royal_flush(cards):
        dic["Royal Flush"] += 1
        return
    elif straight_flush(cards):
        dic["Straight Flush"] += 1
        return
    elif four_of_a_kind(cards):
        dic["Four of a kind"] += 1
        return
    elif full_house(cards):
        dic["Full House"] += 1
        return
    elif flush(cards):
        dic["Flush"] += 1
        return
    elif straight(cards):
        dic["Straight"] += 1
        return
    elif three_of_a_kind(cards):
        dic["Three of a kind"] += 1
        return
    elif two_pairs(cards):
        dic["Two Pair"] += 1
        return
    elif pair(cards):
        dic["Pair"] += 1
        return
    else:
        dic["High Card"] += 1
        return

def execute_testing(count=1):
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
        check_combinations(get_cards(create_cards(),5), dic)
    print(dic)
    for i in dic:
        propability[i] = (dic[i] / count) * 100
    print(propability)
    ax = plt.subplot()
    ax.pie(list(propability.values()), labels=list(propability.keys()), autopct="%1.5f%%", radius=1.3)
    plt.show()


execute_testing(1_000_000)