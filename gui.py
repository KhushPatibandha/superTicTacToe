import pygame
import sys

pygame.init()

# Constants
WIDTH, HEIGHT = 900, 900
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

next_cell_to_play_in = None
turn = 0
game_over = False
winner = None

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

def highlight_next_cell():
    if next_cell_to_play_in is not None and not game_over:
        x = (next_cell_to_play_in % 3) * 300
        y = (next_cell_to_play_in // 3) * 300
        pygame.draw.rect(screen, GREEN, (x, y, 300, 300), 5)
    if next_cell_to_play_in is None:
        for i in range(9):
            if i not in playerX and i not in playerO and i not in tie and not is_cell_full(top_list[i]):
                x = (i % 3) * 300
                y = (i // 3) * 300
                pygame.draw.rect(screen, GREEN, (x, y, 300, 300), 5)
def valid_cell(cell):
    global next_cell_to_play_in,game_over

    if game_over:
        return False
    if next_cell_to_play_in == None:
        return True
    if cell in playerO or cell in playerX:
        return False
    elif next_cell_to_play_in in playerX or next_cell_to_play_in in playerO:
        return True
    elif cell == next_cell_to_play_in:
        return True
    elif is_cell_full(top_list[next_cell_to_play_in]):
        return True

def draw_board():
    for x in range(1, 9):
        pygame.draw.line(screen, BLACK, (x * WIDTH // 9, 0), (x * WIDTH // 9, HEIGHT), 2)
        pygame.draw.line(screen, BLACK, (0, x * HEIGHT // 9), (WIDTH, x * HEIGHT // 9), 2)
    for y in range(1, 3):
        pygame.draw.line(screen, BLACK, (y * WIDTH // 3, 0), (y * WIDTH // 3, HEIGHT), 4)
        pygame.draw.line(screen, BLACK, (0, y * HEIGHT // 3), (WIDTH, y * HEIGHT // 3), 4)

# Draw Marks
def draw_marks():
    for cell in playerX:
        font = pygame.font.Font(None, 370)
        text = font.render("X", True, BLACK)
        screen.blit(text, (300*(cell%3) + 50, 300*(cell//3) + 50))
    for cell in playerO:
        font = pygame.font.Font(None, 370)
        text = font.render("O", True, BLACK)
        screen.blit(text, (300*(cell%3) + 50, 300*(cell//3) + 50))
    for row in range(9):
        for col in range(9):
            if top_list[row][col] != '':
                mark = top_list[row][col]
                x = 300*(row%3) + 50 + 100*(col%3)
                y = 300*(row//3) + 50 + 100*(col//3)
                font = pygame.font.Font(None, 72)
                text = font.render(mark, True, BLACK)
                screen.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))

# placing marks
def place_mark(row, col, player):
    if top_list[row][col] == '':
        top_list[row][col] = player
        return True
    return False

# handling clicks
def handle_click(pos):
    symbol = ''
    global turn, next_cell_to_play_in, game_over, winner

    if turn == 0:
        symbol = 'X'
    if turn == 1:
        symbol = 'O'
    cell_number = pos[0]//300 + (pos[1] // 300)*3
    position = ((pos[1]%300)//100)*3 + (pos[0]%300)//100
    if valid_cell(cell_number):
        if place_mark(cell_number,position,symbol):
            if check_for_win_per_cell(top_list[cell_number],symbol):
                if symbol == 'X':
                    playerX.add(cell_number)
                else:
                    playerO.add(cell_number)

                if check_for_win(symbol):
                    game_over = True
                    winner = f"Player {symbol}"

            if position in playerX or position in playerO or is_cell_full(top_list[position]) or position in tie:
                next_cell_to_play_in = None
            else:
                next_cell_to_play_in = position

            turn = 1- turn
            if check_game_tie():
                game_over = True
                winner = 'Tie'
    else:
        print("Enter a valid cell")

# Driver code
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Super Tic Tac Toe")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            handle_click(event.pos)
    screen.fill(WHITE)
    draw_board()
    draw_marks()
    if game_over:
            font = pygame.font.Font(None, 100)
            if winner == "Tie":
                text = font.render("It's a tie!", True, GREEN)
            else:
                text = font.render(f"{winner} wins!", True, GREEN)
            text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2))
            screen.blit(text, text_rect)

    highlight_next_cell()
    pygame.display.flip()

pygame.quit()
sys.exit()
