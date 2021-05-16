from helpers import *
import engine
import ui
import sys
import random

PLAYER_ICON = '@'
PLAYER_START_X = 3
PLAYER_START_Y = 3

wolf_icon = 'W'
wolf_start_x = 10
wolf_start_y = 10
prev_wolf_posx = 10
prev_wolf_posy = 10

ham_icon = '.'
ham_start_x = 2
ham_start_y = 2
ham_status = False

BOARD_WIDTH = 30
BOARD_HEIGHT = 15

hp = 0
pot = 0
mana = 0

def create_player():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Feel free to extend this dictionary!
    Returns:
    dictionary
    '''
    player = {}
    player["x"] = PLAYER_START_X
    player["y"] = PLAYER_START_Y
    player["icon"] = PLAYER_ICON
    return player

def create_wolf():
    '''
    Creates a 'player' dictionary for storing all player related informations - i.e. player icon, player position.
    Fell free to extend this dictionary!
    Returns:
    dictionary
    '''
    wolf = {}
    wolf["x"] = wolf_start_x
    wolf["y"] = wolf_start_y
    wolf["icon"] = wolf_icon
    wolf['prevx'] = prev_wolf_posx
    wolf['prevy'] = prev_wolf_posy
    return wolf

def create_ham():
    ham = {}
    ham["x"] = ham_start_x
    ham["y"] = ham_start_y
    ham["icon"] = ham_icon
    ham["status"] = ham_status
    return ham

def movement(player, board):
    list_of_movement = ["h"]
    # board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    x = player["x"]
    y = player["y"]
    way_list = ".EZa#"     
    if board[y-1][x] in way_list:
        list_of_movement.append("w")
    if board[y+1][x] in way_list:
        list_of_movement.append("s")
    if board[y][x-1] in way_list:
        list_of_movement.append("a")
    if board[y][x+1] in way_list:
        list_of_movement.append("d")
    
    return list_of_movement

def movement_wolf(wolf, board):
    list_of_movement_wolf = []
    # board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    x = wolf["x"]
    y = wolf["y"]
    way_list = ".H"
    if board[y-1][x] in way_list:
        list_of_movement_wolf.append(1)
    if board[y+1][x] in way_list:
        list_of_movement_wolf.append(2)
    if board[y][x-1] in way_list:
        list_of_movement_wolf.append(3)
    if board[y][x+1] in way_list:
        list_of_movement_wolf.append(4)
    
    return list_of_movement_wolf

def colision(board, player, prev_field_data, wolf, ham):
    global hp, pot, mana
    dissapear_list = "TEZ"
    x = player["x"]
    y = player["y"]
    xw = wolf["x"]
    yw = wolf["y"]
    yh = ham["y"]
    xh = ham["x"]
    player_field = board[y][x]
    wolf_field = board[yw][xw]
    ham_field = board[yh][xh]
    if player_field == wolf_field:
        hp += 1
    elif wolf_field == ham_field:
        pot += 1
    elif player_field == "E":
        mana += 1
    player_field = "."
        
    if prev_field_data is not None:
        prev_field_data[2] = "."
    
    return board, prev_field_data

def change_player_positions(player, key, ham):
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    list_of_movement = movement(player, board)
    x = player["x"]
    y = player["y"]
    prev_field_data = None
    if key in list_of_movement:
        if prev_field_data == None:
            prev_field_data = [x, y, board[y][x]]
        if key == "w":
            player["y"] = player["y"] - 1
        elif key == "s":
            player["y"] = player["y"] + 1
        elif key == "a":
            player["x"] = player["x"] - 1
        elif key == "d":
            player["x"] = player["x"] + 1
        elif key == "h":
            ham["x"] = player["x"]
            ham["y"] = player["y"]
            ham["icon"] = 'H'
            ham["status"] = True

    return player, prev_field_data, ham

def random_wolf_movement(wolf, board, list_of_movement_wolf):
    move_direction = random.randint(0,4)
    x = wolf["x"]
    y = wolf["y"]
    if move_direction in list_of_movement_wolf:
        wolf['prevx'] = x
        wolf['prevy'] = y
        if move_direction == 1 and move_direction in list_of_movement_wolf:
            wolf["y"] = wolf["y"] - 1
        elif move_direction == 2 and move_direction in list_of_movement_wolf:
            wolf["y"] = wolf["y"] + 1
        elif move_direction == 3 and move_direction in list_of_movement_wolf:
            wolf["x"] = wolf["x"] - 1
        elif move_direction == 4 and move_direction in list_of_movement_wolf:
            wolf["x"] = wolf["x"] + 1
    
    return wolf

def move_up_wolf(wolf, board, list_of_movement_wolf):
    x = wolf["x"]
    y = wolf["y"]
    wolf['prevx'] = x
    wolf['prevy'] = y
    wolf["y"] = wolf["y"] - 1
    return wolf

def move_down_wolf(wolf, board, list_of_movement_wolf):
    x = wolf["x"]
    y = wolf["y"]
    wolf['prevx'] = x
    wolf['prevy'] = y
    wolf["y"] = wolf["y"] + 1
    return wolf
 
def move_left_wolf(wolf, board, list_of_movement_wolf):
    x = wolf["x"]
    y = wolf["y"]
    wolf['prevx'] = x
    wolf['prevy'] = y
    wolf["x"] = wolf["x"] - 1
    return wolf

def move_right_wolf(wolf, board, list_of_movement_wolf):
    x = wolf["x"]
    y = wolf["y"]
    wolf['prevx'] = x
    wolf['prevy'] = y
    wolf["x"] = wolf["x"] + 1
    return wolf

def wolf_goto_ham(wolf, board, ham, list_of_movement_wolf):

    list_of_movement_wolf = movement_wolf(wolf, board)
    xw = wolf["x"]
    yw = wolf["y"]
    yh = ham["y"]
    xh = ham["x"]
    wolf_field = board[yw][xw]
    ham_field = board[yh][xh]
    if ham_field != wolf_field:
            if yh < yw:
                move_up_wolf(wolf, board, list_of_movement_wolf)
            if yh > yw:
                move_down_wolf(wolf, board,list_of_movement_wolf)
            if xh < xw:
                move_left_wolf(wolf, board, list_of_movement_wolf)
            if xh > xw:
                move_right_wolf(wolf, board, list_of_movement_wolf)
    else:
        ham["status"] = False
    return wolf

def change_wolf_positions(wolf, board, ham, list_of_movement_wolf):
    
    if ham["status"] == False:
        random_wolf_movement(wolf, board, list_of_movement_wolf)
    else:
        wolf_goto_ham(wolf, board, ham, list_of_movement_wolf)

    return wolf

def asking():
    question_list = {"# This program adds two numbers":1, "num1 = 1.5" : 2, "num2 = 6.3" : 3, "sum = float(num1) + float(num2)" : 4, "print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))]" : 5}

def play_game():
    board = engine.create_board(BOARD_WIDTH, BOARD_HEIGHT)
    player = create_player()
    wolf = create_wolf()
    ham = create_ham()
    list_of_movement_wolf = movement_wolf(wolf, board)
    is_running = True
    prev_field_data = None

    while is_running:
        key = key_pressed()
        if key == 'q':
            is_running = False
        else:
            player, prev_field_data, ham = change_player_positions(player, key, ham)
            board, prev_field_data = colision(board, player, prev_field_data, wolf, ham)
            board = engine.put_player_on_board(board, player, prev_field_data)
            wolf = change_wolf_positions(wolf, board, ham, list_of_movement_wolf)
            board = engine.put_wolf_on_board(board, wolf)
            board = engine.put_ham_on_board(board, ham)
            ui.display_board(board)
            z = ham["status"]
            print(f"HAPE = {hp} Mana = {mana} Potion = {pot} HamStat = {z}")

def main():
    while True:
        clear_screen()
        ui.menu()
        user_choice = int(input())
        if user_choice == 1:
            ui.how_to_play()
        elif user_choice == 2:
            play_game()
        elif user_choice == 3:
            ui.high_scores()
        elif user_choice == 4:
            sys.exit(4)
        else:
            raise ValueError("There is no such option")

if __name__ == '__main__':
    main()