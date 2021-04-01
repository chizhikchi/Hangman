cells_matrix = [[' ' for i in range(3)] for i in range(3)]
coordinates = []
x = 0
y = 0
count = 0


# printing empty grid
def printing_matrix():
    print("---------")
    for row in cells_matrix:
        print("| " + ' '.join(row) + " |")
    print("---------")


def finding_winner():
    global cells_matrix
    winner = ''
    if cells_matrix[0][0] == cells_matrix[1][1] and cells_matrix[0][0] == cells_matrix[2][2]:  # diagonal
        winner = cells_matrix[0][0]
    elif cells_matrix[0][2] == cells_matrix[1][1] and cells_matrix[0][2] == cells_matrix[2][0]:  # diagonal
        winner = cells_matrix[0][2]
    else:
        for i in range(0, 3):
            if cells_matrix[0][i] == cells_matrix[1][i] and cells_matrix[0][i] == cells_matrix[2][i]:  # vertical
                winner = cells_matrix[0][i]
        for row in cells_matrix:
            if row.count('X') == 3 or row.count('O') == 3:  # horizontal
                winner = row[0]
    if winner == "X" or winner == "O":
        print(winner + ' wins')
        return True
    else:
        empty_cells = 0
        for row in cells_matrix:
            empty_cells += row.count(" ")
        if empty_cells == 0:
            print("Draw")
            return True
        else:
            return False


# taking user's coordinates
def tanking_coords():
    global coordinates
    coordinates = input("Enter the coordinates: ")
    coordinates = coordinates.split()


# checking whether the user's coordinates are appropriate
def coord_check():
    global coordinates
    alphacheck = [coordinate.isalpha() for coordinate in coordinates]
    if any(alphacheck) is True:
        print("You should enter numbers!")
        return False
    elif len(coordinates) == 0:
        return False
    elif len(coordinates) > 2:
        print("You should enter only two numbers")
        return False
    else:
        global x
        global y
        y = int(coordinates[0])
        x = int(coordinates[1])
    if x > 3 or x < 1 or y > 3 or y < 1:
        print("Coordinates should be from 1 to 3!")
        return False
    elif not cells_matrix[y - 1][x - 1] == " ":
        print("This cell is occupied! Choose another one!")
        return False


#  updating the grid
def grid_upd():
    global x
    global y
    global count
    global cells_matrix
    x = int(x) - 1
    y = int(y) - 1
    row = cells_matrix[y]
    del row[x]
    if count % 2 == 0:
        row.insert(x, 'X')
        count += 1
    else:
        row.insert(x, "O")
        count += 1
    print("---------")
    for row in cells_matrix:
        row = " ".join(row)
        print("| " + row + " |")
    print("---------")


printing_matrix()
while finding_winner() is False:
    if coord_check() is False:
        tanking_coords()
    else:
        grid_upd()
        if finding_winner() is False:
            tanking_coords()
        else:
            break
