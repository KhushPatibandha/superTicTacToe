# Super tic tac toe

top_dict = {}
top_list = [[] for _ in range(9)]


def check_for_win(list_to_check, player_symbol):
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


# Driver Code
print("Welcome to Super Tic Tac Toe")
print("Player 1: X")
print("Player 2: O")
