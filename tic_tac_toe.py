def draw_board(board):
    print(" ", " ".join("123"))
    for i, row in enumerate(board):
        print(i+1, *row)
    # print("\n".join([" ".join([x for x in y]) for y in board_print]))


def game_init():
    return [["." for x in range(3)] for y in range(3)]


def add_board(board, coords, player):
    x, y = [int(_) - 1 for _ in coords]
    board[x][y] = player


def check_board(board):
    pass


def valide_input(inp):
    return inp.isdigit() and 0 < int(inp) < 4


def input_board(board, player):
    x = 0
    y = 0

    while not x and not y:
        xt, yt = input(f"Игрок {player} введите координаты через запятую :").split(",")
        if valide_input(xt) and valide_input(yt):
            x, y = xt, yt
        else:
            print("Что то ты ввел неправильно .... Давай еще разок ")
    return add_board(board, (x, y), player)


def main():
    board = game_init()
    while True:
        # print(board)
        draw_board(board)
        input_board(board, "O")


if __name__ == "__main__":
    main()
