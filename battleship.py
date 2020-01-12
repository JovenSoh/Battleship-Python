from IPython.display import clear_output
import random as rd

def place_ship(board, ship,ships,alignment,position):
    code = {"Destroyer":5,
            "Cruiser":6,
            "Submarine":7,
            "Battleship":8,
            "Carrier":9}
    position = position.lower()
    coordinates = [0,0]
    coordinates[0] = ord(position[0]) - 97   
    if position[1:3] == "10":
        coordinates[1] = 9
    elif len(position) != 2:
        print("Invalid Coordinates")
        return False          
    else:
        coordinates[1] = ord(position[1]) - 49
    if coordinates[0] < 0 or coordinates[0] >9 or coordinates[1] < 0 or coordinates[1] >9:
        print("Invalid Coordinates")
        return False             
    
    if alignment == "1": #Vertical
        if coordinates[1] < 10 and coordinates[0] < 11 - ships[ship]:
            for tmp in range(ships[ship]):
                if board[coordinates[0] + tmp][coordinates[1]] > 1:
                    print("Ship overlaps!")
                    return False
            for tmp in range(ships[ship]):
                board[coordinates[0]+tmp][coordinates[1]] = code[ship]
        else:
            print ("Ship exceeds board!")
            return False
    elif alignment == "2": #Horizontal
        if coordinates[1] < 11 - ships[ship] and coordinates[0] < 10:
            for tmp in range(ships[ship]):
                if board[coordinates[0]][coordinates[1]+tmp] > 1:
                    print("Ship overlaps!")
                    return False
            for tmp in range(ships[ship]):
                board[coordinates[0]][coordinates[1]+tmp] = code[ship]
        else:
            print ("Ship exceeds board!") 
            return False
    else:
        print("Invalid alignment!")
        return False
    return board

def display(board):
    print("   1 2 3 4 5 6 7 8 9 10")
    for row in range(10):
        print(chr(row+65)," ", end = "")
        for column in range(10):
            if board[row][column] == 2:
                print("x ",end = "")
            elif board[row][column] >2 :
                print("* ",end = "")
            elif board[row][column] == 0:
                print("o ",end = "")
        print()
        
def minimap(board):
    print("   1 2 3 4 5 6 7 8 9 10")
    for row in range(10):
        print(chr(row+65)," ", end="")
        for column in range(10):
            if board[row][column] == 2:
                print("x ",end = "")
            elif board[row][column] == 3:
                print("+ ",end = "")
            else:
                print("o ",end = "")
        print()    
    
def check_sink(board,target):
    #state is a boolean array of the existence of the ship
    for row in range(10):
        if target in board[row]:
            return False #Ship is still in the game
    return True

def check_win(board):
    for row in range(10):
        for column in range(10):
            if board[row][column] >= 5:
                return False
    return True

def check_target(position):
    position = position.lower()
    coordinates = [0,0]
    coordinates[0] = ord(position[0]) - 97   
    if position[1:3] == "10":
        coordinates[1] = 9
    elif len(position) != 2:
        print("Invalid Coordinates")
        return False          
    else:
        coordinates[1] = ord(position[1]) - 49
    if coordinates[0] < 0 or coordinates[0] >9 or coordinates[1] < 0 or coordinates[1] >9:
        print("Invalid Coordinates")
        return False   
    return coordinates, True
        
def attack(board,position):
    row = position[0]
    column = position[1]    
    tile = board[row][column] #Save which ship you hit
    if tile > 4:
        board[row][column] = 2
        print("Hit!")
        if check_sink(board,tile): #Using the ship code, check if there are other parts of it standing
            print("You sunk my battleship!")
        if check_win(board):
            print("You win!")
        return True
    elif board[row][column] == 0:
        print("Miss!")
        board[row][column] = 3
        return False
    
def create_bot():
    placed = False
    board = [[0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],]
    for ship in ships:
        while placed == False:
            alignment = str(rd.randint(1,2))
            position = chr(rd.randint(65,74))+str(rd.randint(1,10))
            if type(place_ship(board,ship,ships,alignment,position)) == list:
                placed = True
        placed = False
        clear_output()
    return board

def board_creation(ships):
    player = [[0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0],]
    ship_length = [2,3,3,4,5]
    placed = False
    #Player board creation
    for ship in ships:
        while placed == False:
            print("Ship:", ship)
            print()
            print("(1) Vertical \n(2) Horizontal")
            alignment = input("Choose alignment of ship: ")
            position = str(input("Pick position to place ship: "))
            print()
            if type(place_ship(player,ship,ships,alignment,position)) == list:
                placed = True
        placed = False
        clear_output()

    print("      Your Board")
    print("-----------------------")
    display(player)

"""
Board Specifications
--------------------
0 - Nothing
1 - Ship
2 - Damaged Ship
3 - Miss
5 - Destroyer
6 - Cruiser
7 - Submarine
8 - Battleship
9 - Carrier

"""
def main(bot,ships):
    print("Welcome to the game Battleships")
    player = board_creation(ships)
    while not check_win(bot) or check_win(player):
        target = str(input("Input target: "))
        while not check_target(target):
            target = str(input("Input target: "))
        target = check_target(target)
        clear_output()
        attack(bot,target[0])
        print()
        print("   Opponent's Board")
        print("-----------------------")
        minimap(bot)

#Bot initialise
ships = {"Destroyer":2,
        "Cruiser":3,
        "Submarine":3,
        "Battleship":4,
        "Carrier":5}
bot = create_bot()
display(bot)

