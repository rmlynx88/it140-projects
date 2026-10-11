# ==========================================
# Module Six Milestone: Move Between Rooms
# Author: RaShaun
# ==========================================

# Dictionary linking rooms to other rooms based on valid movement directions
rooms = {
    'Great Hall': {'south': 'Bedroom'},
    'Bedroom': {'north': 'Great Hall', 'east': 'Cellar'},
    'Cellar': {'west': 'Bedroom'}
}

def show_instructions():
    """Displays game instructions and available commands."""
    print("Welcome to the Dragon Text Adventure Game!")
    print("Move commands: go north, go south, go east, go west (or simply north, south, east, west)")
    print("Type 'exit' to quit the game.\n")

def main():
    # Set the starting room
    current_room = 'Great Hall'
    show_instructions()

    # Gameplay loop running until the exit condition is reached
    while current_room != 'exit':
        print("-" * 40)
        print(f"You are currently in the {current_room}.")
        
        # Prompt for user input
        user_input = input("Enter your move: ").strip().lower()
        
        # Exit check
        if user_input == 'exit':
            current_room = 'exit'
            print("\nThank you for playing! Goodbye.")
            break
            
        # Parse movement direction
        words = user_input.split()
        direction = ""
        if len(words) == 2 and words[0] == 'go':
            direction = words[1]
        elif len(words) == 1:
            direction = words[0]

        # Decision branching & movement validation
        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
        else:
            print("\n[!] You cannot go that way! Invalid movement command.")

if __name__ == '__main__':
    main()
