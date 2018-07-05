def draw_board(board):
    print(" ", " ".join("123"))
    print("\n".join([" ".join([x for x in y]) for y in list(zip("123", *board))]))


def game_init():
    return [["." for x in range(3)] for y in range(3)], "O"


def add_board(board, coords, player):
    x, y = [int(_) - 1 for _ in coords]
    if board[x][y] == ".":
        board[x][y] = player
    else:
        print("\nЗанято !!!\n")


def check_board(board, player):
    win = 0
    res = 0
    for pl in ["X", "O"]:
        print(pl)
        if any(x == pl for x in [column for column in board]):
            print("found", pl)

    return win, res, player


def validate_input(inp):
    return inp.isdigit() and 0 < int(inp) < 4


def input_board(board, player):
    x = 0
    y = 0

    while not x and not y:
        xt, yt = input(f"Игрок {player} введите координаты через запятую :").split(",")
        if validate_input(xt) and validate_input(yt):
            x, y = xt, yt
        else:
            print("Что-то ты ввел неправильно .... Давай еще разок ")
    return add_board(board, (x, y), player)


def main():
    board, player = game_init()
    while True:
        # print(board)
        draw_board(board)
        input_board(board, player)
        win, res, player = check_board(board, player)


if __name__ == "__main__":
    main()
