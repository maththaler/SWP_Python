import random
import collections
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