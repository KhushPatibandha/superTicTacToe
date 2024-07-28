from colorama import Fore, init, Style
import os

init(autoreset=True)

playerX = set()
playerO = set()
tie = set()
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

def is_cell_full(cell):
    return all(position != '' for position in cell)

def check_game_tie():
    return all(cell in playerX or cell in playerO or cell in tie for cell in range(9))

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

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

def get_valid_input(prompt, valid_range):
    while True:
        try:
            value = int(input(prompt))
            if value in valid_range:
                return value
            else:
                print(f"{Fore.RED}{Style.BRIGHT}Enter a valid number between 0 and 8.")
        except ValueError:
            print(f"{Fore.RED}{Style.BRIGHT}Invalid input. Please enter a number between 0 and 8.")

# Driver Code
print(f"{Fore.GREEN}{Style.BRIGHT}Welcome to Super Tic Tac Toe")
print(f"{Fore.GREEN}{Style.BRIGHT}Player 1: X")
print(f"{Fore.GREEN}{Style.BRIGHT}Player 2: O")

print_super_board(top_list)
print(f"{Fore.BLUE}{Style.BRIGHT}Player 1's turn")
cell_number = get_valid_input(f"{Fore.GREEN}Enter the cell number to start: 0-8: ", range(9))
position = get_valid_input(f"{Fore.GREEN}{Style.BRIGHT}Enter the position to start: 0-8: ", range(9))

top_list[cell_number][position] = 'X'
next_cell_to_play_in = position

random_block = 0
no_print_invalid = 1
turn = 2
message = ""
while(True):
    if no_print_invalid == 1:
        clear_screen()
        print_super_board(top_list)
        if message:
            print(message)
            message = ""
    no_print_invalid = 1
    print(f"{Fore.BLUE}{Style.BRIGHT}Player {turn}'s turn")

    if random_block == 1:
        print(f"{Fore.GREEN}{Style.BRIGHT}You can play in any cell")
        next_cell_to_play_in = get_valid_input(f"{Fore.GREEN}{Style.BRIGHT}Enter the cell number to play in: ", range(9))

        # Check if the inputed cell is already won by a player or not
        # If yes, ask the player to enter a valid cell
        # Else, continue the game
        if next_cell_to_play_in in playerX or next_cell_to_play_in in playerO:
            print(f"{Fore.RED}{Style.BRIGHT}Enter a valid cell")
            no_print_invalid = 0
            continue
        random_block = 0

    position = get_valid_input(f"{Fore.GREEN}{Style.BRIGHT}Enter the position in cell number {next_cell_to_play_in} : 0-8: ", range(9))
    if position < 0 or position > 8 or top_list[next_cell_to_play_in][position] != '':
        print(f"{Fore.RED}{Style.BRIGHT}Enter a valid position")
        no_print_invalid = 0
        continue

    symbol = 'X'
    if turn == 1:
        symbol = 'X'
    else:
        symbol = 'O'

    top_list[next_cell_to_play_in][position] = symbol

    # Check if the player had won in this current cell
    # If yes, add the cell to the player's set
    win_or_no_win_symbol = check_for_win_per_cell(top_list[next_cell_to_play_in], symbol)
    if win_or_no_win_symbol:
        if turn == 1:
            playerX.add(next_cell_to_play_in)
            message = f"{Fore.CYAN}{Style.BRIGHT}Player 1 won in cell number: {next_cell_to_play_in}"
        else:
            playerO.add(next_cell_to_play_in)
            message = f"{Fore.CYAN}{Style.BRIGHT}Player 2 won in cell number: {next_cell_to_play_in}"
    elif is_cell_full(top_list[next_cell_to_play_in]):
        tie.add(next_cell_to_play_in)
        message = f"{Fore.CYAN}{Style.BRIGHT}Cell number {next_cell_to_play_in} is a tie."

    # Check if the player had won the game
    # If yes, print the winner and break the loop
    # Else, continue the game
    final_win_or_no_win = check_for_win(symbol)
    if final_win_or_no_win:
        clear_screen()
        print_super_board(top_list)
        print(f"{Fore.CYAN}{Style.BRIGHT}Player {turn} wins, you bamboozled that bozo.")
        break
    elif check_game_tie():
        clear_screen()
        print_super_board(top_list)
        print(f"{Fore.CYAN}{Style.BRIGHT}It's a tie, you both suck.")
        break

    next_cell_to_play_in = position
    if next_cell_to_play_in in playerX or next_cell_to_play_in in playerO or next_cell_to_play_in in tie:
        random_block = 1

    turn = 1 if turn == 2 else 2
