import random

# Board setup with snakes and ladders
# A dictionary where key is the starting point of a snake or ladder,
# and value is the destination.
board = {
    3: 22, 
    5: 8,   
    11: 26, 
    17: 4,  
    19: 7,  
    20: 29, 
    27: 1   
}

# Initial positions of players
players = {
    "Player 1": 0,
    "Player 2": 0
}

# Function to roll a dice
def roll_dice():
    return random.randint(1, 6)

# Function to move a player
def move_player(player):
    roll = roll_dice()
    print(f"{player} rolled a {roll}")
    
    new_position = players[player] + roll
    
    # Check if the new position exceeds 30
    if new_position > 30:
        print(f"{player} stays at {players[player]} (too high)")
        return
    
    # Update player position
    players[player] = new_position
    
    # Check for snakes or ladders
    if players[player] in board:
        if board[players[player]] > players[player]:
            print(f"{player} hit a ladder at {new_position}!")
        else:
            print(f"{player} hit a snake at {new_position}!")
        players[player] = board[players[player]]
    
    print(f"{player} moves to {players[player]}")

# Main game loop
def play_game():
    while True:
        for player in players:
            move_player(player)
            # Check for win condition
            if players[player] >= 30:
                print(f"{player} wins the game!")
                return

# Start the game
play_game()