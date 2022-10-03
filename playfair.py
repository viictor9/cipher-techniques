def playfair(pt, key):
    pt = pt.replace(" ", "").upper()
    key = key.upper()
    alphabet = "abcdefghiklmnopqrstuvwxyz".upper()

    # GRID CREATION
    grid = [[0 for _ in range(5)] for _ in range(5)]
    key_list = list(dict.fromkeys(key))
    alphabet_list = list("".join([letter for letter in alphabet if letter not in key]))
    for i in range(5):
        for j in range(5):
            if key_list:
                grid[i][j] = key_list.pop(0)
                continue
            grid[i][j] = alphabet_list.pop(0)
    # print(grid)

    # SEPARATING LETTERS
    i = 0
    while i < len(pt):
        if i == len(pt)-1:
            pt += "X"
            i += 2
            continue
        if pt[i] == pt[i+1]:
            pt = pt[:i+1] + "X" + pt[i+1:]
        i += 2
    # print(pt)

    # ENCRYPTION
    enc = ""
    i = 0
    while i < len(pt):
        row1, col1 = [(index, row.index(pt[i])) for index, row in enumerate(grid) if pt[i] in row][0]
        row2, col2 = [(index, row.index(pt[i+1])) for index, row in enumerate(grid) if pt[i+1] in row][0]

        if row1 == row2:
            enc += grid[row1][(col1+1) % 5] + grid[row1][(col2+1) % 5]
        elif col1 == col2:
            enc += grid[(row1+1) % 5][col1] + grid[(row2+1) % 5][col1]
        else:
            enc += grid[row1][col2] + grid[row2][col1]
        i += 2

    print("Encrypted Text: ", enc)