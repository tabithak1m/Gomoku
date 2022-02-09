"""
Starter code with starting functions written by Michael Guerzhoy with tests contributed by Siavash Kazemian.
Game functions written by Tabitha Kim
"""

def is_empty(board):
    x = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != " ":
                x += 1
    if x == 0:
        return True

def is_bounded(board, y_end, x_end, length, d_y, d_x):
    y_start = y_end - length * d_y
    x_start = x_end - length * d_x
    # print(y_start, x_start)

    if d_y == 1 and d_x == -1:
        if length != 1:
            if y_start < 0 or x_start > len(board):
                # print("a")
                return "CLOSED"
        elif y_end == x_end == 0 or y_end == x_end == len(board):
            return "CLOSED"
    if y_end + d_y >= len(board) or x_end + d_x >= len(board):
        if y_start < 0 or x_start < 0 or x_start >= len(board):
            return "CLOSED"
        # elif y_end == x_end == len(board) - 1 and d_y == 1 and d_x == -1:
        #     return "CLOSED"
        else:
            if board[y_start][x_start] != " ":
                return "CLOSED"
            elif board[y_start][x_start] == " ":
                return "SEMI-OPEN"
    elif x_end + d_x < 0:
        if board[y_start][x_start] == " ":
            return "SEMI-OPEN"
        else:
            return "CLOSED"
    elif y_start >= 0 and x_start >= 0:
        if board[y_end+d_y][x_end+d_x] != " " and board[y_start][x_start] != " ":
            return "CLOSED"
        elif board[y_end+d_y][x_end+d_x] == " " and board[y_start][x_start] == " ":
            return "OPEN"
        else:
            return "SEMI-OPEN"
    # elif y_start < 0 or x_start > min(x_end + 1, len(board) - x_end):
    #     return "CLOSED"
    elif y_start < 0 or x_start < 0:
        if board[y_end+d_y][x_end+d_x] != " ":
            return "CLOSED"
        else:
            return "SEMI-OPEN"
    else:
        # print("hi")
        return "SEMI-OPEN"


def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    R = [board[y_start][x_start]]
    y = d_y
    x = d_x
    if d_y + d_x > 1:
        for i in range((min(len(board)-y_start, len(board)-x_start))-1):
            R.append(board[y_start + d_y][x_start + d_x])
            d_y += y
            d_x += x
    elif d_y + d_x == 0:
        for i in range((min(len(board)-y_start, x_start + 1))-1):
            R.append(board[y_start + d_y][x_start + d_x])
            d_y += y
            d_x += x
    else:
        for i in range(len(board)-1):
            R.append(board[y_start + d_y][x_start + d_x])
            d_y += y
            d_x += x
    open_seq_count = 0
    semi_open_seq_count = 0
    # print(R)
    for i in range(len(R)-1):
        y = 0
        for j in range(len(R)-i):
            x = 0
            if i+j < len(R):
                for k in R[i:i+length]:
                    if k != col:
                        y = 1
                    if k == col:
                        x += 1
                # if R[i] == R[i+j] == col:
                #     #try to find a way to see if they are adjacent
                #     x += 1
            # print(x,y)
        if x == length and y == 0:
            # print(R[i-1], i, R[i+length])
            if i + length < len(R):
                if R[i+length] == " ":
                    if R[i-1] == " " and i != 0:
                        open_seq_count += 1
                    elif R[i-1] != col and i != 0:
                        semi_open_seq_count += 1
                    elif i == 0:
                        semi_open_seq_count += 1
                elif R[i-1] == " " and i != 0 and R[i+length] != col:
                    semi_open_seq_count += 1
            elif i + length == len(R):
                if R[i-1] == " ":
                    semi_open_seq_count += 1

    return open_seq_count, semi_open_seq_count

def show_row(board, y_start, x_start, d_y, d_x):
    R = [board[y_start][x_start]]
    y = d_y
    x = d_x
    # print(y,x)
    # print(999, y_start, x_start)
    if d_y + d_x > 1:
        for i in range((min(len(board)-y_start, len(board)-x_start))-1):
            R.append(board[y_start + d_y][x_start + d_x])
            d_y += y
            d_x += x
    elif d_y + d_x == 0:
        for i in range((min(len(board)-y_start, x_start + 1))-1):
            R.append(board[y_start + d_y][x_start + d_x])
            d_y += y
            d_x += x
    else:
        for i in range(len(board)-1):
            R.append(board[y_start + d_y][x_start + d_x])
            d_y += y
            d_x += x
            # print(d_y)
            # print(d_x)
    return R


def detect_rows(board, col, length):
    open_seq_count = 0
    semi_open_seq_count = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            if i == 0 and j == 0:
                open_seq_count += detect_row(board, col, i, j, length, 1, 0)[0]
                open_seq_count += detect_row(board, col, i, j, length, 0, 1)[0]
                open_seq_count += detect_row(board, col, i, j, length, 1, 1)[0]
                open_seq_count += detect_row(board, col, i, j, length, 1, -1)[0]
                # print(i,j,open_seq_count)
                semi_open_seq_count += detect_row(board, col, i, j, length, 1, 0)[1]
                semi_open_seq_count += detect_row(board, col, i, j, length, 0, 1)[1]
                semi_open_seq_count += detect_row(board, col, i, j, length, 1, 1)[1]
                semi_open_seq_count += detect_row(board, col, i, j, length, 1, -1)[1]
                # print(i,j,semi_open_seq_count)
            elif i == 0 and j != 0:
                open_seq_count += detect_row(board, col, i, j, length, 1, 0)[0]
                open_seq_count += detect_row(board, col, i, j, length, 1, 1)[0]
                open_seq_count += detect_row(board, col, i, j, length, 1, -1)[0]
                semi_open_seq_count += detect_row(board, col, i, j, length, 1, 0)[1]
                # print(i,j,semi_open_seq_count)
                semi_open_seq_count += detect_row(board, col, i, j, length, 1, 1)[1]
                # print(i,j,semi_open_seq_count)
                semi_open_seq_count += detect_row(board, col, i, j, length, 1, -1)[1]
                # print(i,j,open_seq_count)
                # print(i,j,semi_open_seq_count)
            elif j == 0 and i !=0:
                open_seq_count += detect_row(board, col, i, j, length, 0, 1)[0]
                open_seq_count += detect_row(board, col, i, j, length, 1, 1)[0]
                open_seq_count += detect_row(board, col, i, j, length, 1, -1)[0]
                semi_open_seq_count += detect_row(board, col, i, j, length, 0, 1)[1]
                semi_open_seq_count += detect_row(board, col, i, j, length, 1, 1)[1]
                semi_open_seq_count += detect_row(board, col, i, j, length, 1, -1)[1]
                # print(i,j,open_seq_count)
                # print(i,j,semi_open_seq_count)
            elif i == 7:
                open_seq_count += detect_row(board, col, i, j, length, 1, 1)[0]
                open_seq_count += detect_row(board, col, i, j, length, 1, -1)[0]
                semi_open_seq_count += detect_row(board, col, i, j, length, 1, 1)[1]
                semi_open_seq_count += detect_row(board, col, i, j, length, 1, -1)[1]
                # print(i,j,open_seq_count)
                # print(i,j,semi_open_seq_count)
            elif j == 7 and i != 7:
                open_seq_count += detect_row(board, col, i, j, length, 1, 1)[0]
                open_seq_count += detect_row(board, col, i, j, length, 1, -1)[0]
                semi_open_seq_count += detect_row(board, col, i, j, length, 1, 1)[1]
                semi_open_seq_count += detect_row(board, col, i, j, length, 1, -1)[1]
                # print(i,j,open_seq_count)
                # print(i,j,semi_open_seq_count)

    return open_seq_count, semi_open_seq_count

def search_max(board):
    Score = {}
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == " ":
                put_seq_on_board(board, i, j, 0, 0, 1, "b")
                Score[(i,j)] = score(board)
                put_seq_on_board(board, i, j, 0, 0, 1, " ")
    keys = list(Score.keys())
    values = list(Score.values())
    move_y, move_x = keys[values.index(max(values))]
    return move_y, move_x

def score(board):
    MAX_SCORE = 100000

    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}

    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)

    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE

    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE

    return (-10000 * (open_w[4] + semi_open_w[4])+
            500  * open_b[4]                     +
            50   * semi_open_b[4]                +
            -100  * open_w[3]                    +
            -30   * semi_open_w[3]               +
            50   * open_b[3]                     +
            10   * semi_open_b[3]                +
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])


def is_win(board):
    d = [(1,0), (0,1), (1,1), (1,-1)]
    d1 = [(1,0), (1,1), (1,-1)]
    d2 = [(0,1), (1,1), (1,-1)]
    d3 = [(1,1), (1,-1)]

    for y in range(len(board)):
        for x in range(len(board[y])):
            if y == 0 and x == 0:
                for (d_y, d_x) in d:
                    R = show_row(board, y, x, d_y, d_x)
                    # print(R)
                    for i in range(len(R)-1):
                        b = 0
                        w = 0
                        for j in range(5):
                            if i+j < len(R):
                                if R[i] == R[i+j] == "b":
                                    b += 1
                                elif R[i] == R[i+j] == "w":
                                    w += 1
                        if b == 5:
                            # print(b)
                            if i + 5 < len(R):
                                print("hi")
                                if R[i+5] != "b":
                                    if R[i-1] != "b" and i != 0:
                                        return "Black won"
                                    elif i == 0:
                                        return "Black won"
                            elif i + 5 == len(R):
                                if R[i-1] != "b" and i != 0:
                                    return "Black won"
                                elif i == 0:
                                    return "Black won"
                        elif w == 5:
                            if i + 5 < len(R):
                                if R[i+5] != "w":
                                    if R[i-1] != "w" and i != 0:
                                        return "White won"
                                    elif i == 0:
                                        return "White won"
                            elif i + 5 == len(R):
                                if R[i-1] != "w" and i != 0:
                                    return "White won"
                                elif i == 0:
                                    return "White won"
            elif y == 0 and x != 0:
                for (d_y, d_x) in d1:
                    R = show_row(board, y, x, d_y, d_x)
                    # print(R)
                    for i in range(len(R)-1):
                        b = 0
                        w = 0
                        for j in range(5):
                            if i+j < len(R):
                                if R[i] == R[i+j] == "b":
                                    b += 1
                                elif R[i] == R[i+j] == "w":
                                    w += 1
                        if b == 5:
                            # print(b)
                            if i + 5 < len(R):
                                print("hi")
                                if R[i+5] != "b":
                                    if R[i-1] != "b" and i != 0:
                                        return "Black won"
                                    elif i == 0:
                                        return "Black won"
                            elif i + 5 == len(R):
                                if R[i-1] != "b" and i != 0:
                                    return "Black won"
                                elif i == 0:
                                    return "Black won"
                        elif w == 5:
                            if i + 5 < len(R):
                                if R[i+5] != "w":
                                    if R[i-1] != "w" and i != 0:
                                        return "White won"
                                    elif i == 0:
                                        return "White won"
                            elif i + 5 == len(R):
                                if R[i-1] != "w" and i != 0:
                                    return "White won"
                                elif i == 0:
                                    return "White won"
            elif x == 0 and y != 0:
                for (d_y, d_x) in d2:
                    R = show_row(board, y, x, d_y, d_x)
                    for i in range(len(R)-1):
                        b = 0
                        w = 0
                        for j in range(5):
                            if i+j < len(R):
                                if R[i] == R[i+j] == "b":
                                    b += 1
                                elif R[i] == R[i+j] == "w":
                                    w += 1

                        if b == 5:
                            if i + 5 < len(R):
                                if R[i+5] != "b":
                                    if R[i-1] != "b" and i != 0:
                                        return "Black won"
                                    elif i == 0:
                                        return "Black won"
                            elif i + 5 == len(R):
                                if R[i-1] != "b" and i != 0:
                                    return "Black won"
                                elif i == 0:
                                    return "Black won"
                        elif w == 5:
                            if i + 5 < len(R):
                                if R[i+5] != "w":
                                    if R[i-1] != "w" and i != 0:
                                        return "White won"
                                    elif i == 0:
                                        return "White won"
                            elif i + 5 == len(R):
                                if R[i-1] != "w" and i != 0:
                                    return "White won"
                                elif i == 0:
                                    return "White won"
            elif y == 7:
                for (d_y, d_x) in d3:
                    R = show_row(board, y, x, d_y, d_x)
                    for i in range(len(R)-1):
                        b = 0
                        w = 0
                        for j in range(5):
                            if i+j < len(R):
                                if R[i] == R[i+j] == "b":
                                    b += 1
                                elif R[i] == R[i+j] == "w":
                                    w += 1
                        if b == 5:
                            if i + 5 < len(R):
                                if R[i+5] != "b":
                                    if R[i-1] != "b" and i != 0:
                                        return "Black won"
                                    elif i == 0:
                                        return "Black won"
                            elif i + 5 == len(R):
                                if R[i-1] != "b" and i != 0:
                                    return "Black won"
                                elif i == 0:
                                    return "Black won"
                        elif w == 5:
                            if i + 5 < len(R):
                                if R[i+5] != "w":
                                    if R[i-1] != "w" and i != 0:
                                        return "White won"
                                    elif i == 0:
                                        return "White won"
                            elif i + 5 == len(R):
                                if R[i-1] != "w" and i != 0:
                                    return "White won"
                                elif i == 0:
                                    return "White won"
            elif x == 7 and y != 7:
                for (d_y, d_x) in d3:
                    R = show_row(board, y, x, d_y, d_x)
                    for i in range(len(R)-1):
                        b = 0
                        w = 0
                        for j in range(5):
                            if i+j < len(R):
                                if R[i] == R[i+j] == "b":
                                    b += 1
                                elif R[i] == R[i+j] == "w":
                                    w += 1
                        if b == 5:
                            if i + 5 < len(R):
                                if R[i+5] != "b":
                                    if R[i-1] != "b" and i != 0:
                                        return "Black won"
                                    elif i == 0:
                                        return "Black won"
                            elif i + 5 == len(R):
                                if R[i-1] != "b" and i != 0:
                                    return "Black won"
                                elif i == 0:
                                    return "Black won"
                        elif w == 5:
                            if i + 5 < len(R):
                                if R[i+5] != "w":
                                    if R[i-1] != "w" and i != 0:
                                        return "White won"
                                    elif i == 0:
                                        return "White won"
                            elif i + 5 == len(R):
                                if R[i-1] != "w" and i != 0:
                                    return "White won"
                                elif i == 0:
                                    return "White won"

    for i in range(len(board)):
            for j in board[i]:
                if j == " ":
                    return "Continue playing"
    return "Draw"



def print_board(board):

    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"

    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1])

        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"

    print(s)


def make_empty_board(sz):
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board



def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))






def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])

    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)

        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res





        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res



def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x


def test_is_empty():
    board  = make_empty_board(8)
    if is_empty(board):
        print("TEST CASE for is_empty PASSED")
    else:
        print("TEST CASE for is_empty FAILED")

def test_is_bounded():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)

    y_end = 3
    x_end = 5

    print(is_bounded(board, y_end, x_end, length, d_y, d_x))

    if is_bounded(board, y_end, x_end, length, d_y, d_x) == 'OPEN':
        print("TEST CASE for is_bounded PASSED")
    else:
        print("TEST CASE for is_bounded FAILED")


def test_detect_row():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_row(board, "w", 0,x,length,d_y,d_x) == (1,0):
        print("TEST CASE for detect_row PASSED")
    else:
        print("TEST CASE for detect_row FAILED")

def test_detect_rows():
    board = make_empty_board(8)
    x = 5; y = 1; d_x = 0; d_y = 1; length = 3; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    if detect_rows(board, col,length) == (1,0):
        print("TEST CASE for detect_rows PASSED")
    else:
        print("TEST CASE for detect_rows FAILED")

def test_search_max():
    board = make_empty_board(8)
    x = 5; y = 0; d_x = 0; d_y = 1; length = 4; col = 'w'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    x = 6; y = 0; d_x = 0; d_y = 1; length = 4; col = 'b'
    put_seq_on_board(board, y, x, d_y, d_x, length, col)
    print_board(board)
    if search_max(board) == (4,6):
        print("TEST CASE for search_max PASSED")
    else:
        print("TEST CASE for search_max FAILED")

def easy_testset_for_main_functions():
    test_is_empty()
    test_is_bounded()
    test_detect_row()
    test_detect_rows()
    test_search_max()

def some_tests():
    board = make_empty_board(8)

    board[0][5] = "w"
    board[0][6] = "b"
    y = 5; x = 2; d_x = 0; d_y = 1; length = 3
    put_seq_on_board(board, y, x, d_y, d_x, length, "w")
    print_board(board)
    analysis(board)

    # Expected output:
    #       *0|1|2|3|4|5|6|7*
    #       0 | | | | |w|b| *
    #       1 | | | | | | | *
    #       2 | | | | | | | *
    #       3 | | | | | | | *
    #       4 | | | | | | | *
    #       5 | |w| | | | | *
    #       6 | |w| | | | | *
    #       7 | |w| | | | | *
    #       *****************
    #       Black stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 0
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0
    #       White stones:
    #       Open rows of length 2: 0
    #       Semi-open rows of length 2: 0
    #       Open rows of length 3: 0
    #       Semi-open rows of length 3: 1
    #       Open rows of length 4: 0
    #       Semi-open rows of length 4: 0
    #       Open rows of length 5: 0
    #       Semi-open rows of length 5: 0

    y = 3; x = 5; d_x = -1; d_y = 1; length = 2

    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    print_board(board)
    analysis(board)

    # Expected output:
    #        *0|1|2|3|4|5|6|7*
    #        0 | | | | |w|b| *
    #        1 | | | | | | | *
    #        2 | | | | | | | *
    #        3 | | | | |b| | *
    #        4 | | | |b| | | *
    #        5 | |w| | | | | *
    #        6 | |w| | | | | *
    #        7 | |w| | | | | *
    #        *****************
    #
    #         Black stones:
    #         Open rows of length 2: 1
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 0
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #         White stones:
    #         Open rows of length 2: 0
    #         Semi-open rows of length 2: 0
    #         Open rows of length 3: 0
    #         Semi-open rows of length 3: 1
    #         Open rows of length 4: 0
    #         Semi-open rows of length 4: 0
    #         Open rows of length 5: 0
    #         Semi-open rows of length 5: 0
    #

    y = 5; x = 3; d_x = -1; d_y = 1; length = 1
    put_seq_on_board(board, y, x, d_y, d_x, length, "b");
    print_board(board);
    analysis(board);

    #        Expected output:
    #           *0|1|2|3|4|5|6|7*
    #           0 | | | | |w|b| *
    #           1 | | | | | | | *
    #           2 | | | | | | | *
    #           3 | | | | |b| | *
    #           4 | | | |b| | | *
    #           5 | |w|b| | | | *
    #           6 | |w| | | | | *
    #           7 | |w| | | | | *
    #           *****************
    #
    #
    #        Black stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0
    #        White stones:
    #        Open rows of length 2: 0
    #        Semi-open rows of length 2: 0
    #        Open rows of length 3: 0
    #        Semi-open rows of length 3: 1
    #        Open rows of length 4: 0
    #        Semi-open rows of length 4: 0
    #        Open rows of length 5: 0
    #        Semi-open rows of length 5: 0


def testing_win_5_closed():
    board = make_empty_board(8)
    board[2][2] = "w"
    y = 3;
    x = 2;
    d_x = 0;
    d_y = 1;
    length = 5
    put_seq_on_board(board, y, x, d_y, d_x, length, "b")
    # print_board(board)
    # print(is_win(board))
    if is_win(board)=="Black won":
        print("PASSSSSSSSS")
    else:
        print("EPIC FAIL :(")
        # Expected output:
        # *0|1|2|3|4|5|6|7*
        # 0 | | | | | | | *
        # 1 | | | | | | | *
        # 2 | |w| | | | | *
        # 3 | |b| | | | | *
        # 4 | |b| | | | | *
        # 5 | |b| | | | | *
        # 6 | |b| | | | | *
        # 7 | |b| | | | | *
        # *****************
        # PASSSSSSSSS

if __name__ == '__main__':
    #play_gomoku(8)
    board = []
    board = make_empty_board(8)
    board[0][0] = "x"
    board[7][7] = "x"
    board[0][7] = "x"
    board[7][0] = "x"
    # put_seq_on_board(board, 4,5,1,-1,4,"w")
    print_board(board)
    # board=np.array([["x"," "," "," "," "," "," ","x"],
    #                 [" "," "," "," "," "," "," "," "],
    #                 [" "," "," "," "," "," "," "," "],
    #                 [" "," "," "," "," "," "," "," "],
    #                 [" "," "," "," "," "," "," "," "],
    #                 [" "," "," "," "," "," "," "," "],
    #                 [" "," "," "," "," "," "," "," "],
    #                 ["x"," "," "," "," "," "," ","x"]])

    print("\nchecking (0,0)")
    print(is_bounded(board,0,0,1,0,1)) #semiopen
    print(is_bounded(board,0,0,1,1,0))#semiopen
    print(is_bounded(board,0,0,1,1,-1))#closed
    print(is_bounded(board,0,0,1,1,1))#semiopen

    print("\nchecking (7,0)")
    print(is_bounded(board,7,0,1,0,1))#semiopen
    print(is_bounded(board,7,0,1,1,0))#semiopen
    print(is_bounded(board,7,0,1,1,-1))#semiopen
    print(is_bounded(board,7,0,1,1,1)) #closed

    print("\nchecking (0,7)")
    print(is_bounded(board,0,7,1,0,1))#semiopen
    print(is_bounded(board,0,7,1,1,0))#semiopen
    print(is_bounded(board,0,7,1,1,-1))#semiopen
    print(is_bounded(board,0,7,1,1,1))#closed



    print("\nchecking (7,7)")
    print(is_bounded(board,7,7,1,0,1)) #semiopen
    print(is_bounded(board,7,7,1,1,0)) ##semiopen
    print(is_bounded(board,7,7,1,1,-1)) #closed
    print(is_bounded(board,7,7,1,1,1)) #semiopen


















































