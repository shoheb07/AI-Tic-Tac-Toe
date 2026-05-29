import math

board = [" " for _ in range(9)]

def print_board():
    print()
    for i in range(0, 9, 3):
        print(board[i] + " | " + board[i+1] + " | " + board[i+2])
        if i < 6:
            print("--+---+--")
    print()

def check_winner(b, player):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for win in wins:
        if all(b[pos] == player for pos in win):
            return True

    return False

def is_draw(b):
    return " " not in b

def minimax(b, depth, is_maximizing):

    if check_winner(b, "O"):
        return 1

    if check_winner(b, "X"):
        return -1

    if is_draw(b):
        return 0

    if is_maximizing:

        best_score = -math.inf

        for i in range(9):

            if b[i] == " ":

                b[i] = "O"

                score = minimax(
                    b,
                    depth + 1,
                    False
                )

                b[i] = " "

                best_score = max(
                    score,
                    best_score
                )

        return best_score

    else:

        best_score = math.inf

        for i in range(9):

            if b[i] == " ":

                b[i] = "X"

                score = minimax(
                    b,
                    depth + 1,
                    True
                )

                b[i] = " "

                best_score = min(
                    score,
                    best_score
                )

        return best_score

def ai_move():

    best_score = -math.inf

    move = None

    for i in range(9):

        if board[i] == " ":

            board[i] = "O"

            score = minimax(
                board,
                0,
                False
            )

            board[i] = " "

            if score > best_score:

                best_score = score

                move = i

    board[move] = "O"

def player_move():

    while True:

        try:

            move = int(
                input("Enter position (1-9): ")
            ) - 1

            if board[move] == " ":

                board[move] = "X"

                break

            else:

                print("Position occupied!")

        except:

            print("Invalid input!")

print("AI Tic Tac Toe")
print("You = X")
print("AI = O")

while True:

    print_board()

    player_move()

    if check_winner(board, "X"):

        print_board()

        print("You Win!")

        break

    if is_draw(board):

        print_board()

        print("Draw!")

        break

    ai_move()

    if check_winner(board, "O"):

        print_board()

        print("AI Wins!")

        break

    if is_draw(board):

        print_board()

        print("Draw!")

        break
