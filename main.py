# Super tic tac toe

playerX = set()
playerO = set()
top_list = [[] for _ in range(9)]


def check_for_win_per_cell(list_to_check, player_symbol):
    if(list_to_check[0] == player_symbol and list_to_check[1] == player_symbol and list_to_check[2] == player_symbol):
        return True
    elif(list_to_check[3] == player_symbol and list_to_check[4] == player_symbol and list_to_check[5] == player_symbol):
        return True
    elif(list_to_check[6] == player_symbol and list_to_check[7] == player_symbol and list_to_check[8] == player_symbol):
        return True
    elif(list_to_check[0] == player_symbol and list_to_check[3] == player_symbol and list_to_check[6] == player_symbol):
        return True
    elif(list_to_check[1] == player_symbol and list_to_check[4] == player_symbol and list_to_check[7] == player_symbol):
        return True
    elif(list_to_check[2] == player_symbol and list_to_check[5] == player_symbol and list_to_check[8] == player_symbol):
        return True
    elif(list_to_check[0] == player_symbol and list_to_check[4] == player_symbol and list_to_check[8] == player_symbol):
        return True
    elif(list_to_check[2] == player_symbol and list_to_check[4] == player_symbol and list_to_check[6] == player_symbol):
        return True
    else:
        return False

def check_for_win(player_symbol):
    if(player_symbol == 'X'):
        player_symbol = playerX
    else:
        player_symbol = playerO

    if(0 in player_symbol and 1 in player_symbol and 2 in player_symbol):
        return True
    elif(3 in player_symbol and 4 in player_symbol and 5 in player_symbol):
        return True
    elif(6 in player_symbol and 7 in player_symbol and 8 in player_symbol):
        return True
    elif(0 in player_symbol and 3 in player_symbol and 6 in player_symbol):
        return True
    elif(1 in player_symbol and 4 in player_symbol and 7 in player_symbol):
        return True
    elif(2 in player_symbol and 5 in player_symbol and 8 in player_symbol):
        return True
    elif(0 in player_symbol and 4 in player_symbol and 8 in player_symbol):
        return True
    elif(2 in player_symbol and 4 in player_symbol and 6 in player_symbol):
        return True
    else:
        return False

# Driver Code
print("Welcome to Super Tic Tac Toe")
print("Player 1: X")
print("Player 2: O")

print("Player 1's turn")
cell_number = int(input("Enter the cell number to start: 0-8"))
position = int(input("Enter the position to start: 0-8"))

top_list[cell_number][position] = 'X'
next_cell_to_play_in = position

turn = 2
while(True):
    print(f"Player {turn}'s turn")
    position = int(input("Enter the position : 0-8"))
    if position is not "":
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
        print(f"Player {turn} wins")
        break

    next_cell_to_play_in = position
    turn = 1 if turn == 2 else 2
