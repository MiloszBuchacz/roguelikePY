import helpers

def display_board(board):
    '''
    Displays complete game board on the screen
    Returns:
    Nothing 
    '''
    helpers.clear_screen()

    for row in board:
        #print(''.join(row))
        for element in row:
            print(element, end='')
        print()

def menu():
    print("\033[34m" + "-" * 116 + "\n" + '''    ___    ___    __  __   ___     _     _____   ___  __   __  ___     __  __    ___    _  _   _  __  ___  __   __
   / __|  / _ \  |  \/  | | _ )   /_\   |_   _| |_ _| \ \ / / | __|   |  \/  |  / _ \  | \| | | |/ / | __| \ \ / /
  | (__  | (_) | | |\/| | | _ \  / _ \    | |    | |   \ V /  | _|    | |\/| | | (_) | | .` | | ' <  | _|   \ V / 
   \___|  \___/  |_|  |_| |___/ /_/ \_\   |_|   |___|   \_/   |___|   |_|  |_|  \___/  |_|\_| |_|\_\ |___|   |_|  
'''.center(116) + "\n" + "-" * 116 + "\033[0m" + "\n")
    print('1. How to play')
    print('2. Play')
    print('3. High Scores')
    print('4. Quit')
    print()
    print('Please, select the number: ')


def how_to_play():
    helpers.clear_screen()
    print("\033[34m" + "-" * 80 + "\n" + "RULES".center(80) + "\n" + "-" * 80 + "\033[0m")
    print('''
You are a combative monkey. Your goal is to get as many useful items as you can.
Avoid the attacks of the enemies and try to save your life. Be brave!
CONTROLS:
^ Move UP       press W
v Move DOWN     press S
< Move LEFT     press A
> Move RIGHT    press D
Grab something  .......
Light the torch .......
Quit            press Q
''')

    input("/Press enter to continue./")

def get_table_from_file(file_name):
    """
    Reads csv file and returns it as a list of lists.
    Lines are rows columns are separated by ";"
    Args:
        file_name (str): name of file to read
    Returns:
         list: List of lists read from a file.
    """
    with open(file_name, "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(";") for element in lines]
    return table

def write_table_to_file(file_name, table):
    """
    Writes list of lists into a csv file.
    Args:
        file_name (str): name of file to write to
        table (list): list of lists to write to a file
    Returns:
         None
    """
    with open(file_name, "w") as file:
        for record in table:
            row = ';'.join(record)
            file.write(row + "\n")

def print_table(table, title_list):
    the_longest_in_col = [['-']*len(table[0])]
    for row in table:
        # Loop to create a list of the longest elements
        for i in range(len(row)):
            if len(row[i]) > len(the_longest_in_col[0][i]):
                the_longest_in_col[0][i] = row[i]
    # Loop to eventually modify the list of longest elements, if title_list has longer elements
    for i in range(len(title_list)):
        if len(title_list[i]) > len(the_longest_in_col[0][i]):
            the_longest_in_col[0][i] = title_list[i]
        title_list[i] = title_list[i].center(len(the_longest_in_col[0][i]))
    # Loop to create width of the table
    table_width = 3*len(the_longest_in_col[0])-1
    for element in the_longest_in_col[0]:
        table_width += len(element)
    # Print awesome table
    print(f"*{'-'*(table_width)}*")
    print(f"| {' | '.join(title_list)} |")
    for row in table:
        print(f"|{'-'*(table_width)}|")
        # Loop to center elements in row
        for i in range(len(row)):
            row[i] = row[i].center(len(the_longest_in_col[0][i]))
        print(f"| {' | '.join(row)} |")
    print(f"*{'-'*(table_width)}*")

def high_scores():
    helpers.clear_screen()
    print("\033[34m" + "-" * 80 + "\n" + "HIGH SCORES".center(80) + "\n" + "-" * 80 + "\033[0m" + "\n")
    scores = get_table_from_file("high_scores.csv")
    print_table(scores, ["User", "Points", "Time Spent"])
    input("\n/Press enter to continue./")

def play_again():
    print("Play again? (enter 'yes' or 'no')")
    return input().lower().startswith("y")