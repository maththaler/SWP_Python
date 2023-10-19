import random
#max --> Farbe*Symbol
#Farbe = max // zahl
#Symbol = max % zahl
def create_list (count_color, count_symbols):
    return [a for a in range(count_color*count_symbols)]

def swap_positions(pos1, pos2, list):
    list[pos1], list[pos2] = list[pos2], list[pos1]

def get_cards(list, numbers_to_draw):
    for i in range(numbers_to_draw):
        draw = random.randint(0, len(list) - 1 - i)
        swap_positions(draw, len(list) - 1 - i, list)
    return list[len(list) - numbers_to_draw:]



