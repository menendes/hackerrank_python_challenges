if __name__ == '__main__':
    n, m = map(int, input().split())
    input_array = map(int, input().split())
    set_a = set(map(int, input().split()))
    set_b = set(map(int, input().split()))

    happiness = 0

    for number in input_array:
        if number in set_a:
            happiness += 1
        if number in set_b:
            happiness += 1

    print(happiness)
