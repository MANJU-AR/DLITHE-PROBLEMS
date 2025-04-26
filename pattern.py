for i in range(5):
    for j in range(5):
        if i % 2 == 0:
            print(i + 1 if j < 4 else i + 2, end='')
        else:
            print(i + 2 if j == 0 else i + 1, end='')
    print()