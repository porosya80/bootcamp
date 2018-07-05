def draw_board(board):
    print(" ", " ".join("123"))
    print("\n".join([" ".join([x for x in y]) for y in list(zip("123", *board))]))


def game_init():
    print(
        """Крестики нолики
            для выхода используйте CTRL+c
            Поехали ..."""
    )
    return [["." for x in range(3)] for y in range(3)], "O"


def add_board(board, coords, player):
    x, y = [int(_) - 1 for _ in coords]
    if board[x][y] == ".":
        board[x][y] = player
    else:
        print("\nЗанято !!!\n")


def check_board(board, player):
    win = ""
    for pl in "XO":
        for col in board:
            if all(x == pl for x in col):
                win = pl
        for col in list(zip(*board)):
            if all(x == pl for x in col):
                win = pl
        if board[0][0] == board[1][1] == board[2][2] == pl or board[2][0] == board[1][1] == board[0][2] == pl:
            win = pl

    if sum(col.count(".") for col in board) == 0 and win == "":
        win = "TIE !!!"

    return win, "X" if player == "O" else "O"


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
        win, player = check_board(board, player)
        if win:
            print(f"\n\n{win} выиграл\n\n") if win != "TIE !!!" else print(f"\n\nНичья\n\n")
            board, player = game_init()


if __name__ == "__main__":
    main()
