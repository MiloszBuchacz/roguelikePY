def create_board(width, height):
    '''
    Creates game board based on input parameters.
    Args:
    int: The width of the board
    int: The height of the board
    Returns:
    list: Game board  
    '''
    board = []

    for row_index in range(height):
        row = []
        if row_index == 0 or row_index == height - 1:
            for i in range(width):
                row.append("X")
        else:
            row.append("X")
            for i in range(width - 2):
                row.append(".")
            row.append("X")
        board.append(row)

    return board
    
def put_player_on_board(board, player, prev_field_data):
    '''
    Puts the player icon on the board on player coordinates.
    Args:
    list: The game board
    dictionary: The player information - the icon and coordinates
    Returns:
    list: The game board with the player sign on it
    '''
    if prev_field_data != None:
        field_x = prev_field_data[0]
        field_y = prev_field_data[1]
        field_icon = prev_field_data[2]
        board[field_y][field_x] = field_icon

    player_icon = player["icon"]
    player_x = player["x"]
    player_y = player["y"]

    board[player_y][player_x] = player_icon

    return board

def put_wolf_on_board(board, wolf):
    wolf_icon = wolf["icon"]
    prev_x = wolf["prevx"]
    prev_y = wolf["prevy"]
    wolf_x = wolf["x"]
    wolf_y = wolf["y"]

    board[wolf_y][wolf_x] = wolf_icon
    board[prev_y][prev_x] = "."

    return board

def put_ham_on_board(board, ham):
    ham_icon = ham["icon"]
    ham_x = ham["x"]
    ham_y = ham["y"]
    
    board[ham_y][ham_x] = ham_icon

    return board