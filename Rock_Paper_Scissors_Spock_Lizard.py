import random
import json
from matplotlib import pyplot as plt

class Element:
    def __init__(self, strengths) -> None:
        self.strengths = strengths
        
class Rock(Element):
    def __init__(self) -> None:
        super().__init__([Scissors, Lizard])

class Paper(Element):
    def __init__(self) -> None:
        super().__init__([Rock, Spock])

class Scissors(Element):
    def __init__(self) -> None:
        super().__init__([Paper, Lizard])

class Spock(Element):
    def __init__(self) -> None:
        super().__init__([Scissors, Rock])

class Lizard(Element):
    def __init__(self) -> None:
        super().__init__([Paper, Spock])
        
def init_game(won_count, element_count):
    computer = computer_pick()
    player = player_pick()
    element_count[computer.__class__.__name__] += 1
    element_count[player.__class__.__name__] += 1
    print(f"Computer picked: {computer.__class__.__name__}")
    status = win(computer, player)
    if (status == None):
        print("Draw!")
        won_count["Draw"] += 1
    elif (status):
        print("Won!")
        won_count["Player"] += 1
    elif (not status):
        print("Lost!")
        won_count["Computer"] += 1

def element_factory(input: str):
    input = input.lower()
    if (input == "rock"):
        return Rock()
    if (input == "paper"):
        return Paper()
    if (input == "scissors"):
        return Scissors()
    if (input == "spock"):
        return Spock()
    if (input == "lizard"):
        return Lizard()
    return None

def player_pick():
    print("Enter your choice:")
    item = input()
    player_item = element_factory(item)
    while (player_item is None):
        print("Invalid entry")
        print("Enter your choice:")
        item = input()
        player_item = element_factory(item)
    return player_item

def computer_pick():
    return random.choice([Rock(), Paper(), Scissors(), Spock(), Lizard()])

def win(computer : Element, player : Element):
    if (type(computer) in player.strengths):
        return True
    
    if (type(player) in computer.strengths):
        return False
    
    return None
    

def write_file(dict, file_name):
    with open(f"D:\OneDrive\OneDrive - HTL Anichstrasse\HTL 5\Python\SWP_Python\{file_name}.json", "w") as file:
        file.write(json.dumps(dict))

def read_file(file_name):
    with open(f"D:\OneDrive\OneDrive - HTL Anichstrasse\HTL 5\Python\SWP_Python\{file_name}.json", "r") as file:
        return json.load(file)
    
def show_statistic(won_count: {}, element_count: {}):
    plt.bar(list(won_count.keys()),list(won_count.values()))
    plt.show()
    plt.bar(list(element_count.keys()),list(element_count.values()))
    plt.show()

if __name__ == "__main__":
    won_count = read_file("won_count")
    element_count = read_file("element_count")
    show_statistic(won_count, element_count)
    while (True):
        init_game(won_count, element_count)
        write_file(won_count, "won_count")
        write_file(element_count, "element_count")
