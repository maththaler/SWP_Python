import Poker as p
import time
import numpy as np

times_per_function = {}

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        try:
            times_per_function[func.__name__].append((end_time - start_time) * 1000)
        except:
            times_per_function[func.__name__] = []
            times_per_function[func.__name__].append((end_time - start_time) * 1000)

        return f"Time passed in Function {func.__name__}: {(end_time - start_time) * 1000}ms"
    return wrapper


#Damit Poker so bleibt, wie es ist...
@timer
def pair(cards):
    return p.pair(cards)

@timer
def two_pairs(cards):
    return p.two_pairs(cards)

@timer
def three_of_a_kind(cards):
    return p.three_of_a_kind(cards)

@timer
def straight(cards):
    return p.straight(cards)

@timer
def flush(cards):
    return p.flush(cards)

@timer
def full_house(cards):
    return p.full_house(cards)

@timer
def four_of_a_kind(cards):
    return p.four_of_a_kind(cards)

@timer
def straight_flush(cards):
    return p.straight_flush(cards)

@timer
def royal_flush(cards):
    return p.royal_flush(cards)

def execute_testing(count):
    for _ in range(count):
        cards = p.create_cards()
        pair(cards)
        two_pairs(cards)
        three_of_a_kind(cards)
        straight(cards)
        full_house(cards)
        four_of_a_kind(cards)
        straight_flush(cards)
        royal_flush(cards)
    average_dict = {}
    for key in times_per_function.keys():
        average_dict[key] = np.average(times_per_function[key])
    return average_dict


if __name__ == "__main__":
    print(execute_testing(10))
