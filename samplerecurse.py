def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)


def compareTo(s1, s2):
    # compare first character
    # Make sure to handle the end of the string
    # if they are the same, recurse
    pass


def hanoi_tower_move(rings, start_pin, end_pin, aux):
    if rings == 1:
        print(f"{start_pin} -> {end_pin}")
    else:
        hanoi_tower_move(rings - 1, start_pin, aux, end_pin)
        print(f"{start_pin} -> {end_pin}")
        hanoi_tower_move(rings - 1, aux, end_pin, start_pin)


if __name__ == "__main__":
    hanoi_tower_move(4, 1, 3, 2)
