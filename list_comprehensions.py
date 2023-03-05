if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    result_list = [[i, h, k]
                   for i in range(x + 1)
                   for h in range(y + 1)
                   for k in range(z + 1)
                   if i + h + k is not n
                   ]

    print(result_list)

