if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    set_items = set(arr)
    sorted_set = sorted(set_items, reverse=True)
    print(sorted_set[1])