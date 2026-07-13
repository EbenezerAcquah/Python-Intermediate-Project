board = ["1", "2", "3",
         "4", "5", "6",
         "7", "8", "9"]


def display_board():
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()


def check_winner(player):
    winning_combinations = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]

    for combo in winning_combinations:
        if (board[combo[0]] == player and
            board[combo[1]] == player and
            board[combo[2]] == player):
            return True

    return False


def board_full():
    for square in board:
        if square not in ["X", "O"]:
            return False
    return True


def play_game():
    global board

    board = ["1","2","3",
             "4","5","6",
             "7","8","9"]

    current_player = "X"

while True:

        display_board()

        try:
            choice = int(input(f"Player {current_player}, choose a position (1-9): "))

            if choice < 1 or choice > 9:
                print("Choose a number between 1 and 9.")
                continue

            if board[choice-1] in ["X","O"]:
                print("Position already taken.")
                continue

            board[choice-1] = current_player

            if check_winner(current_player):
                display_board()
                print(f"Player {current_player} wins!")
                break

            if board_full():
                display_board()
                print("It's a draw!")
                break

            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"

        except ValueError:
            print("Enter a valid number.")


while True:

    play_game()

    again = input("Play again? (y/n): ").lower()

    if again != "y":
        print("Goodbye!")
        break