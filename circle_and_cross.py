# CIRCLE AND CROSS

# GLOBAL CONSTANCE

X = "X"
O = "0"
EMPTY = " "
REMIS = " DRAW"
NUM_SQUARES = 9


def display_instruct():
    """GAME INSTRUCTION"""
    print(
        """BOARD. YOU HAVE TO CHOOSE FIELD FROM 0 TO 8
           LIKE ON EXAMPLE BOARD BELOW: 
            
            0  |  1  |  2
            -------------
            3  |  4  |  5
            -------------
            6  |  7  |  8
            \n
            """
    )


def ask_yes_no(question):
    # FUNCTION, WITH ANSWER YES OR NO
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    # FUNCTION, WHICH ASKING FOR NUMBER FROM DECLARING RANGE
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def pieces():
    # WHO START THE GAME AND WHICH MARK BELONGS TO (X lub O)
    go_first = ask_yes_no("DO YOU WANT TO MOVE FIRST? (y/n): ")
    if go_first == "y":
        print("YOU START")
        human = X
        computer = O
    else:
        print("COMPUTER PLAYER START")
        human = O
        computer = X
    return computer, human


def new_board():
    # CREATION NEW BOARD
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board  # FUNCTION RETURNS LISTS (BOARD) WITH EVERY EMPTY FIELDS


def display_board(board):
    # DISPLAYING GAME BOARD ON SCREEN
    print("\n\t", board[0], " | ", board[1], " | ", board[2])
    print("\t", "-------------")
    print("\t", board[3], " | ", board[4], " | ", board[5])
    print("\t", "-------------")
    print("\t", board[6], " | ", board[7], " | ", board[8])
    print("\n")


def legal_moves(board):
    # CREATION CORRECT MOVEMENT LIST
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves  # FUNCTION RETURNS LISTS (BOARD) WITH EMPTY FIELDS


def winner(board):
    # ustalenie zwyciezcy gry
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return REMIS
    return None


def human_move(board, human):
    # HUMAN MOVEMENT
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("WHAT WILL BE YOUR MOVEMENT LIKE? (0-8):", 0, NUM_SQUARES)
        if move not in legal:
            print("\nTHIS FILED IS BUSY. CHOOSE OTHER ONE.")
    print("BRAVO!")
    return move  # RETURN NUMBER OF FILED, WHERE HUMAN PLAYER PUT MARK


def computer_move(board, computer, human):
    # COMPUTER MOVEMENT

    # WORKING COPY OF BOARD (BECAUSE FUNCTION WILL BE CHANGING BOARD)
    board = board[:]
    print("EMPTY BOARD ELEMENTS: ", board)
    print("LEGAL MOVES BEFORE COMPUTER TURN: ", legal_moves(board), "\n")

    # BEST MOVES
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print("NUMBER OF CHOOSING FILED: ", end=" ")

    # IF COMPUTER CAN WIN EXECUTE THIS MOVE
    for move in legal_moves(board):     # CHECKING EVERY MOVEMENT (STEP BY STEP) IN POSSIBLE MOVEMENTS
        board[move] = computer          # ASSIGN CURRENT CHECKING MOVEMENT TO COMPUTER MARK (X)
        if winner(board) == computer:   # CHECKING IN HOLE BOARD IN CASE OF MOVEMENT, WHICH IS CURRENT CHECKING MEETS THE CONDITION FOR WIN
            print(move)                 # IF YES, PRINT THIS MOVEMENT (FIELD NUMBER)
            print("\n>>>>>>>>> IF COMPUTER CAN WIN OPTION\n")
            return move                 # RETURN FIELD
        # THIS MOVEMENT WAS CHECKED, CANCEL IT
        board[move] = EMPTY             # IF CONDITION DOESN'T FULFILLED, CLEAR SELECTED FIELD ON BOARD

    # IF HUMAN PLAYER CAN WIN - BLOCK HIM
    for move in legal_moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            print("\n>>>>>>>>> IF HUMAN PLAYER CAN WIN OPTION\n")
            return move
        # THIS MOVEMENT WAS CHECKED, CANCEL IT
        board[move] = EMPTY

    # IF COMPUTER CAN WIN IN TWO NEXT STEPS, EXECUTE FIRST ONE
    # CHECK NEXT TIME (NEXT STEP) AFTER FIRST STEP WAS CHECKED
    # THE CONDITION: AFTER FIRST STEP, IN SECOND STEP, THERE ARE TWO FIELDS, WHICH BOTH WINS

    for move in legal_moves(board):
        board[move] = computer
        for move_2 in legal_moves(board):
            board[move_2] = computer
            if winner(board) == computer:
                print("\nFIRST MOVE: ", move)
                print("\nSECOND MOVE: ", move_2)
                for move_3 in legal_moves(board):
                    board[move_3] = computer
                    # THIS MOVEMENT WAS CHECKED, CANCEL IT
                    board[move_2] = EMPTY
                    if winner(board) == computer:
                        print("\nTHIRD MOVE: ", move_3)
                        print(move)
                        print("\n>>>>>>>>> HIGH LEVEL OPTION\n")
                        return move
                    board[move_3] = EMPTY
            board[move_2] = EMPTY
        # THIS MOVEMENT WAS CHECKED, CANCEL IT
        board[move] = EMPTY

    # LET'S CHOOSE OTHER FILED BECAUSE NO ONE CAN WIN IN NEXT STEP
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            print("\n>>>>>>>>> BEST MOVE OPTION\n")
            return move


def next_turn(turn):
    # CHANGE TURN
    if turn == X:
        return O
    else:
        return X


def congrat_winner(the_winner, computer, human):
    # CONGRATULATION
    if the_winner != REMIS:
        print(the_winner, " IS WINNER!\n")
    else:
        print("DRAW")

    if the_winner == computer:
        print("COMPUTER WIN")
    elif the_winner == human:
        print("PLAYER WIN")
    elif the_winner == REMIS:
        print("DRAW")


def main():
    display_instruct()
    computer, human = pieces()
    turn = X
    board = new_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    congrat_winner(the_winner, computer, human)


# START THE GAME
main()
input("\n\nTo exit game press 'Enter'. ")



