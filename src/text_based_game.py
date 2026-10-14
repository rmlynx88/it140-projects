# ===================================================
# IT 140 Project Two: Text-Based Adventure Game
# File Name: text_based_game.py
# Author: RaShaun
# ===================================================

def show_instructions():
    """Displays the game controls and main objective."""
    print("=" * 50)
    print("        DRAGON'S DUNGEON TEXT ADVENTURE")
    print("=" * 50)
    print("Collect all 6 items before confronting the Dragon!")
    print("Move Commands:   go South, go North, go East, go West")
    print("Item Commands:   get 'item name'")
    print("Type 'exit' to quit the game.")
    print("=" * 50 + "\n")


def show_status(current_room, inventory, rooms):
    """Displays player's status, current room details, exits, and items."""
    print("-" * 40)
    print(f"You are currently in the {current_room}.")
    print(f"Inventory: {inventory}")
    
    # Display room exits
    exits = [dir.capitalize() for dir in rooms[current_room].keys() if dir != 'item']
    print(f"Available Exits: {', '.join(exits)}")

    # Display room item if present
    if 'item' in rooms[current_room]:
        print(f"You see a {rooms[current_room]['item']} here.")
    print("-" * 40)


def main():
    # 1. Full 8-Room Dictionary setup with rooms, movement links, and items
    rooms = {
        'Great Hall': {'south': 'Bedroom', 'north': 'Dungeon', 'east': 'Kitchen', 'west': 'Library'},
        'Bedroom': {'north': 'Great Hall', 'east': 'Cellar', 'item': 'Armor'},
        'Cellar': {'west': 'Bedroom', 'item': 'Helmet'},
        'Library': {'east': 'Great Hall', 'item': 'Spellbook'},
        'Kitchen': {'west': 'Great Hall', 'item': 'Potion'},
        'Dungeon': {'south': 'Great Hall', 'east': 'Armory', 'item': 'Shield'},
        'Armory': {'west': 'Dungeon', 'north': 'Dining Room', 'item': 'Sword'},
        'Dining Room': {'south': 'Armory', 'item': 'Dragon'}  # Villain Room
    }

    # Track player state
    current_room = 'Great Hall'
    inventory = []
    
    # Dynamically determine win condition based on total collectible items on the map
    total_required_items = sum(1 for room in rooms.values() if 'item' in room and room['item'] != 'Dragon')

    show_instructions()

    # 2. Main Gameplay Loop
    while True:
        # Check Win/Loss conditions upon entering the Villain's room
        if current_room == 'Dining Room':
            if len(inventory) == total_required_items:
                print("\n" + "=" * 50)
                print("CONGRATULATIONS! You collected all items and defeated the Dragon!")
                print("You win!")
                print("=" * 50)
            else:
                print("\n" + "=" * 50)
                print("NOM NOM... GAME OVER!")
                print("You confronted the Dragon without all 6 items and were defeated.")
                print("=" * 50)
            break

        # Display current status
        show_status(current_room, inventory, rooms)

        # Prompt player command
        user_input = input("\nEnter your move: ").strip().lower()

        # Handle Exit Command
        if user_input == 'exit':
            print("\nThank you for playing! Goodbye.")
            break

        # Parse command words
        words = user_input.split()

        # 3. Decision Branching: Movement Logic (e.g., "go north" or "north")
        if len(words) >= 1 and (words[0] == 'go' or words[0] in ['north', 'south', 'east', 'west']):
            direction = words[-1]
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
                print(f"\nYou moved to the {current_room}.")
            else:
                print("\n[!] You cannot go that way!")

        # 4. Decision Branching: Item Collection Logic (e.g., "get armor" or "get item")
        elif len(words) >= 2 and words[0] == 'get':
            target_item = ' '.join(words[1:]).title()
            
            if 'item' in rooms[current_room] and rooms[current_room]['item'].title() == target_item:
                picked_item = rooms[current_room].pop('item')
                inventory.append(picked_item)
                print(f"\n[+] Success! You picked up the {picked_item}.")
            else:
                print(f"\n[!] There is no {target_item} to pick up here.")

        # Invalid Input Validation
        else:
            print("\n[!] Invalid command. Use 'go [direction]', 'get [item]', or 'exit'.")


if __name__ == '__main__':
    main()
