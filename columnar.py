import math


def columnar(pt, key):
    pt = pt.replace(" ", "").lower()
    columns = len(str(key))
    rows = 1 + math.ceil(len(pt) / columns)

    # GRID CREATION
    grid = [["" for j in range(columns)] for i in range(rows)]

    index = 0
    for i in range(rows):
        for j in range(columns):
            if i == 0:
                grid[i][j] = int(str(key)[j])
            else:
                if index < len(pt):
                    grid[i][j] = pt[index]
                    index += 1
                else:
                    grid[i][j] = "x"
    # print(grid)

    # ENCRYPTION
    enc = ""
    for column in range(min(grid[0]), max(grid[0]) + 1):
        for j in range(1, rows):
            enc += grid[j][grid[0].index(column)]
    print("Encrypted: ", enc)

    # DECRYPTION
    rows = 1 + math.ceil(len(enc) / columns)

    # -- FILL THE GRID COLUMN WISE AND GET THE TEXT ROW WISE --
    grid = [["" for j in range(columns)] for i in range(rows)]
    for i in range(rows):
        for j in range(columns):
            if i == 0:
                grid[i][j] = int(str(key)[j])
    index = 0
    for column in range(min(grid[0]), max(grid[0]) + 1):
        for j in range(1, rows):
            grid[j][grid[0].index(column)] = enc[index]
            index += 1
    # print(grid)
    dec = ""
    for row in grid[1:]:
        dec += "".join(row)
    print("Decrypted: ", dec)