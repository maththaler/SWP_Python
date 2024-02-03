import Poker as p
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        func(*args, **kwargs)
        end_time = time.perf_counter()
        return f"Time passed in Function {func.__name__}: {(end_time - start_time) * 1000}ms"
    return wrapper


#Damit Poker so bleibt, wie es ist...
@timer
def pair(cards):
    p.pair(cards)

@timer
def two_pairs(cards):
    p.two_pairs(cards)

@timer
def three_of_a_kind(cards):
    p.three_of_a_kind(cards)

@timer
def straight(cards):
    p.straight(cards)

@timer
def flush(cards):
    p.flush(cards)

@timer
def full_house(cards):
    p.full_house

@timer
def four_of_a_kind(cards):
    p.four_of_a_kind(cards)

@timer
def straight_flush(cards):
    p.straight_flush(cards)

@timer
def royal_flush(cards):
    p.royal_flush(cards)

if __name__ == "__main__":
    cards = [12,23,32,1,2]
    print(pair(cards))
    print(two_pairs(cards))
    print(three_of_a_kind(cards))
    print(straight(cards))
    print(full_house(cards))
    print(four_of_a_kind(cards))
    print(straight_flush(cards))
    print(royal_flush(cards))
