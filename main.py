from random import randint


def main():
    game_end = False

    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    # Generate a random first player
    current_player = ["X", "0"][randint(0, 1)]

    game_state = (False, "", "")

    while not game_end:
        show_board(board)

        valid_move = False

        while not valid_move:
            move = input("What is {p}'s next move: ".format(p=current_player))

            valid_move = try_move(board, move, current_player)

        if current_player == "X":
            current_player = "0"
        else:
            current_player = "X"

        # Check the state of the game
        game_state = check_game_result(board)
        game_end = game_state[0]

    show_board(board)
    print(game_state[2])


def check_game_result(board):
    players = ["X", "0"]

    for player in players:
        # Check the Rows
        for i in range(3):
            if board[i].count(player) == 3:
                return True, player, "Player {p} won on row {row}".format(p=player, row=i)

        # Check the Columns
        for i in range(3):
            if board[0][i] == board[1][i] == board[2][i] == player:
                return True, player, "Player {p} won on column {col}".format(p=player, col=i)

        # Check the main diagonal
        if board[0][0] == board[1][1] == board[2][2] == player:
            return True, player, "Player {p} won on the main diagonal".format(p=player)

        # Check the secondary diagonal
        if board[0][2] == board[1][1] == board[2][0] == player:
            return True, player, "Player {p} won on the secondary diagonal".format(p=player)

    return False, "", ""


def show_board(board):

    print("\n" * 20)

    # Function to display the current board state and also the indexes of the rows/columns

    # 1st Way to print the board
    # print("Current board is:\n")
    # print("    (0) (1) (2)\n")
    # print("(0)  " + " ┃ ".join(board[0]))
    # print("    ━━━╋━━━╋━━━")
    # print("(1)  " + " ┃ ".join(board[1]))
    # print("    ━━━╋━━━╋━━━")
    # print("(2)  " + " ┃ ".join(board[2]))

    # 2nd way to print the board (i think it's more readable like this...less efficient a bit because of the replace)
    print(
        '''
             (0) (1) (2)
            
        (0)   {} ┃ {} ┃ {}
     -        ━━━╋━-━━╋━━━
        (1)   {} ┃ {} ┃ {}
     -        ━━━╋━-━━╋━━━
        (2)   {} ┃ {} ┃ {}
        '''.replace("-", "").format(board[0][0], board[0][1], board[0][2], board[1][0], board[1][1], board[1][2], board[2][0], board[2][1], board[2][2])
    )

    print("\n")


def try_move(board, move, player):
    # Check if user input is a number
    if move.isnumeric():
        # Check if user input is a number (upper condition) that has only 2 digits
        if len(move) == 2:
            row = int(move[0])
            col = int(move[1])
            # Check if the digits for the row and col are from the valid indexes
            if row in [0, 1, 2] and col in [0, 1, 2]:
                if board[row][col] != " ":
                    print("Board cell already contains {}, try a different move\n".format(board[row][col]))
                    return False
                else:
                    board[row][col] = player
                    return True
            else:
                print("Please pick the correct numbers for the rows/columns (0, 1 and 2) e.g move syntax: 00, 12, 02\n")
                return False
        else:
            print("Too may characters in input, please try again. e.g move syntax: 00, 12, 02\n")
            return False
    else:
        print("Please pick numbers for the move instead of strings (0, 1 and 2) e.g move syntax: 00, 12, 02\n")


main()
