{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from IPython.display import clear_output\n",
    "import random as rd\n",
    "\n",
    "def place_ship(board, ship,ships,alignment,position):\n",
    "    code = {\"Destroyer\":5,\n",
    "            \"Cruiser\":6,\n",
    "            \"Submarine\":7,\n",
    "            \"Battleship\":8,\n",
    "            \"Carrier\":9}\n",
    "    position = position.lower()\n",
    "    coordinates = [0,0]\n",
    "    coordinates[0] = ord(position[0]) - 97   \n",
    "    if position[1:3] == \"10\":\n",
    "        coordinates[1] = 9\n",
    "    elif len(position) != 2:\n",
    "        print(\"Invalid Coordinates\")\n",
    "        return False          \n",
    "    else:\n",
    "        coordinates[1] = ord(position[1]) - 49\n",
    "    if coordinates[0] < 0 or coordinates[0] >9 or coordinates[1] < 0 or coordinates[1] >9:\n",
    "        print(\"Invalid Coordinates\")\n",
    "        return False             \n",
    "    \n",
    "    if alignment == \"1\": #Vertical\n",
    "        if coordinates[1] < 10 and coordinates[0] < 11 - ships[ship]:\n",
    "            for tmp in range(ships[ship]):\n",
    "                if board[coordinates[0] + tmp][coordinates[1]] > 1:\n",
    "                    print(\"Ship overlaps!\")\n",
    "                    return False\n",
    "            for tmp in range(ships[ship]):\n",
    "                board[coordinates[0]+tmp][coordinates[1]] = code[ship]\n",
    "        else:\n",
    "            print (\"Ship exceeds board!\")\n",
    "            return False\n",
    "    elif alignment == \"2\": #Horizontal\n",
    "        if coordinates[1] < 11 - ships[ship] and coordinates[0] < 10:\n",
    "            for tmp in range(ships[ship]):\n",
    "                if board[coordinates[0]][coordinates[1]+tmp] > 1:\n",
    "                    print(\"Ship overlaps!\")\n",
    "                    return False\n",
    "            for tmp in range(ships[ship]):\n",
    "                board[coordinates[0]][coordinates[1]+tmp] = code[ship]\n",
    "        else:\n",
    "            print (\"Ship exceeds board!\") \n",
    "            return False\n",
    "    else:\n",
    "        print(\"Invalid alignment!\")\n",
    "        return False\n",
    "    return board\n",
    "\n",
    "def display(board):\n",
    "    print(\"   1 2 3 4 5 6 7 8 9 10\")\n",
    "    for row in range(10):\n",
    "        print(chr(row+65),\" \", end=\"\")\n",
    "        for column in range(10):\n",
    "            if board[row][column] == 2:\n",
    "                print(\"x \",end = \"\")\n",
    "            elif board[row][column] >2 :\n",
    "                print(\"* \",end = \"\")\n",
    "            elif board[row][column] == 0:\n",
    "                print(\"o \",end = \"\")\n",
    "        print()\n",
    "        \n",
    "def minimap(board):\n",
    "    print(\"   1 2 3 4 5 6 7 8 9 10\")\n",
    "    for row in range(10):\n",
    "        print(chr(row+65),\" \", end=\"\")\n",
    "        for column in range(10):\n",
    "            if board[row][column] == 2:\n",
    "                print(\"x \",end = \"\")\n",
    "            elif board[row][column] == 3:\n",
    "                print(\"+ \",end = \"\")\n",
    "            else:\n",
    "                print(\"o \",end = \"\")\n",
    "        print()    \n",
    "    \n",
    "def check_sink(board,target):\n",
    "    #state is a boolean array of the existence of the ship\n",
    "    for row in range(10):\n",
    "        if target in board[row]:\n",
    "            return False #Ship is still in the game\n",
    "    return True\n",
    "\n",
    "def check_win(board):\n",
    "    for row in range(10):\n",
    "        for column in range(10):\n",
    "            if board[row][column] >= 5:\n",
    "                return False\n",
    "    return True\n",
    "\n",
    "def check_target(position):\n",
    "    position = position.lower()\n",
    "    coordinates = [0,0]\n",
    "    coordinates[0] = ord(position[0]) - 97   \n",
    "    if position[1:3] == \"10\":\n",
    "        coordinates[1] = 9\n",
    "    elif len(position) != 2:\n",
    "        print(\"Invalid Coordinates\")\n",
    "        return False          \n",
    "    else:\n",
    "        coordinates[1] = ord(position[1]) - 49\n",
    "    if coordinates[0] < 0 or coordinates[0] >9 or coordinates[1] < 0 or coordinates[1] >9:\n",
    "        print(\"Invalid Coordinates\")\n",
    "        return False   \n",
    "    return coordinates, True\n",
    "        \n",
    "def attack(board,position):\n",
    "    row = position[0]\n",
    "    column = position[1]    \n",
    "    tile = board[row][column] #Save which ship you hit\n",
    "    if tile > 4:\n",
    "        board[row][column] = 2\n",
    "        print(\"Hit!\")\n",
    "        if check_sink(board,tile): #Using the ship code, check if there are other parts of it standing\n",
    "            print(\"You sunk my battleship!\")\n",
    "        if check_win(board):\n",
    "            print(\"You win!\")\n",
    "        return True\n",
    "    elif board[row][column] == 0:\n",
    "        print(\"Miss!\")\n",
    "        board[row][column] = 3\n",
    "        return False\n",
    "    \n",
    "def create_bot():\n",
    "    placed = False\n",
    "    board = [[0,0,0,0,0,0,0,0,0,0],\n",
    "            [0,0,0,0,0,0,0,0,0,0],\n",
    "            [0,0,0,0,0,0,0,0,0,0],\n",
    "            [0,0,0,0,0,0,0,0,0,0],\n",
    "            [0,0,0,0,0,0,0,0,0,0],\n",
    "            [0,0,0,0,0,0,0,0,0,0],\n",
    "            [0,0,0,0,0,0,0,0,0,0],\n",
    "            [0,0,0,0,0,0,0,0,0,0],\n",
    "            [0,0,0,0,0,0,0,0,0,0],\n",
    "            [0,0,0,0,0,0,0,0,0,0],]\n",
    "    for ship in ships:\n",
    "        while placed == False:\n",
    "            alignment = str(rd.randint(1,2))\n",
    "            position = chr(rd.randint(65,74))+str(rd.randint(1,10))\n",
    "            if type(place_ship(board,ship,ships,alignment,position)) == list:\n",
    "                placed = True\n",
    "        placed = False\n",
    "        clear_output()\n",
    "    return board\n",
    "\n",
    "def board_creation(ships):\n",
    "    player = [[0,0,0,0,0,0,0,0,0,0],\n",
    "            [0,0,0,0,0,0,0,0,0,0],\n",
    "            [0,0,0,0,0,0,0,0,0,0],\n",
    "            [0,0,0,0,0,0,0,0,0,0],\n",
    "            [0,0,0,0,0,0,0,0,0,0],\n",
    "            [0,0,0,0,0,0,0,0,0,0],\n",
    "            [0,0,0,0,0,0,0,0,0,0],\n",
    "            [0,0,0,0,0,0,0,0,0,0],\n",
    "            [0,0,0,0,0,0,0,0,0,0],\n",
    "            [0,0,0,0,0,0,0,0,0,0],]\n",
    "    ship_length = [2,3,3,4,5]\n",
    "    placed = False\n",
    "    #Player board creation\n",
    "    for ship in ships:\n",
    "        while placed == False:\n",
    "            print(\"Ship:\", ship)\n",
    "            print()\n",
    "            print(\"(1) Vertical \\n(2) Horizontal\")\n",
    "            alignment = input(\"Choose alignment of ship: \")\n",
    "            position = str(input(\"Pick position to place ship: \"))\n",
    "            print()\n",
    "            if type(place_ship(player,ship,ships,alignment,position)) == list:\n",
    "                placed = True\n",
    "        placed = False\n",
    "        clear_output()\n",
    "\n",
    "    print(\"      Your Board\")\n",
    "    print(\"-----------------------\")\n",
    "    display(player)\n",
    "\n",
    "\"\"\"\n",
    "Board Specifications\n",
    "--------------------\n",
    "0 - Nothing\n",
    "1 - Ship\n",
    "2 - Damaged Ship\n",
    "3 - Miss\n",
    "5 - Destroyer\n",
    "6 - Cruiser\n",
    "7 - Submarine\n",
    "8 - Battleship\n",
    "9 - Carrier\n",
    "\n",
    "\"\"\"\n",
    "def main(bot,ships):\n",
    "    print(\"Welcome to the game Battleships\")\n",
    "    player = board_creation(ships)\n",
    "    while not check_win(bot) or check_win(player):\n",
    "        target = str(input(\"Input target: \"))\n",
    "        while not check_target(target):\n",
    "            target = str(input(\"Input target: \"))\n",
    "        target = check_target(target)\n",
    "        clear_output()\n",
    "        attack(bot,target[0])\n",
    "        print()\n",
    "        print(\"   Opponent's Board\")\n",
    "        print(\"-----------------------\")\n",
    "        minimap(bot)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Bot initialise\n",
    "ships = {\"Destroyer\":2,\n",
    "        \"Cruiser\":3,\n",
    "        \"Submarine\":3,\n",
    "        \"Battleship\":4,\n",
    "        \"Carrier\":5}\n",
    "bot = create_bot()\n",
    "display(bot)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "main(bot,ships)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "ord(\"9\") - 49"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
