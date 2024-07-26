playerX = set()
playerO = set()
top_list = [['' for _ in range(9)] for _ in range(9)]

def check_for_win_per_cell(list_to_check, player_symbol):
    return (
        (list_to_check[0] == player_symbol and list_to_check[1] == player_symbol and list_to_check[2] == player_symbol) or
        (list_to_check[3] == player_symbol and list_to_check[4] == player_symbol and list_to_check[5] == player_symbol) or
        (list_to_check[6] == player_symbol and list_to_check[7] == player_symbol and list_to_check[8] == player_symbol) or
        (list_to_check[0] == player_symbol and list_to_check[3] == player_symbol and list_to_check[6] == player_symbol) or
        (list_to_check[1] == player_symbol and list_to_check[4] == player_symbol and list_to_check[7] == player_symbol) or
        (list_to_check[2] == player_symbol and list_to_check[5] == player_symbol and list_to_check[8] == player_symbol) or
        (list_to_check[0] == player_symbol and list_to_check[4] == player_symbol and list_to_check[8] == player_symbol) or
        (list_to_check[2] == player_symbol and list_to_check[4] == player_symbol and list_to_check[6] == player_symbol)
    )

def check_for_win(player_symbol):
    if(player_symbol == 'X'):
        player_symbol = playerX
    else:
        player_symbol = playerO

    return (
        (0 in player_symbol and 1 in player_symbol and 2 in player_symbol) or
        (3 in player_symbol and 4 in player_symbol and 5 in player_symbol) or
        (6 in player_symbol and 7 in player_symbol and 8 in player_symbol) or
        (0 in player_symbol and 3 in player_symbol and 6 in player_symbol) or
        (1 in player_symbol and 4 in player_symbol and 7 in player_symbol) or
        (2 in player_symbol and 5 in player_symbol and 8 in player_symbol) or
        (0 in player_symbol and 4 in player_symbol and 8 in player_symbol) or
        (2 in player_symbol and 4 in player_symbol and 6 in player_symbol)
    )

def print_single_board(board):
    lines = []
    for i in range(0, 9, 3):
        line = " {} | {} | {} ".format(
            board[i] if board[i] != '' else ' ',
            board[i+1] if board[i+1] != '' else ' ',
            board[i+2] if board[i+2] != '' else ' '
        )
        lines.append(line)
        if i < 6:
            lines.append("===+===+===")
    return lines

def print_super_board(top_list):
    super_board = []
    for row in range(3):
        for sub_row in range(3):
            line_parts = []
            for col in range(3):
                board = top_list[row * 3 + col]
                line_parts.append(print_single_board(board)[sub_row * 2])
            super_board.append(" || ".join(line_parts))
            if sub_row < 2:
                line_parts = []
                for col in range(3):
                    board = top_list[row * 3 + col]
                    line_parts.append(print_single_board(board)[sub_row * 2 + 1])
                super_board.append(" || ".join(line_parts))
        if row < 2:
            super_board.append("=" * 43)
    for line in super_board:
        print(line)

# Driver Code
print("Welcome to Super Tic Tac Toe")
print("Player 1: X")
print("Player 2: O")

print_super_board(top_list)
print("Player 1's turn")
cell_number = int(input("Enter the cell number to start: 0-8: "))
position = int(input("Enter the position to start: 0-8: "))

top_list[cell_number][position] = 'X'
next_cell_to_play_in = position

random_block = 0
turn = 2
while(True):
    print_super_board(top_list)
    print(f"Player {turn}'s turn")

    if random_block == 1:
        print("You can play in any cell")
        next_cell_to_play_in = int(input("Enter the cell number to play in: "))

        # Check if the inputed cell is already won by a player or not
        # If yes, ask the player to enter a valid cell
        # Else, continue the game
        if next_cell_to_play_in in playerX or next_cell_to_play_in in playerO:
            print("Enter a valid cell")
            continue
        random_block = 0

    position = int(input("Enter the position : 0-8: "))
    if position < 0 or position > 8 or top_list[next_cell_to_play_in][position] != '':
        print("Enter a valid position")
        continue

    symbol = 'X'
    if turn == 1:
        symbol = 'X'
    else:
        symbol = 'O'

    top_list[next_cell_to_play_in][position] = symbol

    # Check if the player had won in this current cell
    # If yes, add the cell to the player's set
    win_or_no_win = check_for_win_per_cell(top_list[next_cell_to_play_in], symbol)
    if win_or_no_win:
        if turn == 1:
            playerX.add(next_cell_to_play_in)
        else:
            playerO.add(next_cell_to_play_in)

    # Check if the player had won the game
    # If yes, print the winner and break the loop
    # Else, continue the game
    final_win_or_no_win = check_for_win(symbol)
    if final_win_or_no_win:
        print_super_board(top_list)
        print(f"Player {turn} wins, you bamboozled that bozo. ")
        break

    next_cell_to_play_in = position
    if next_cell_to_play_in in playerX or next_cell_to_play_in in playerO:
        random_block = 1

    turn = 1 if turn == 2 else 2
