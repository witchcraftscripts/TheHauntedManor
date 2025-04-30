# Haunted Manor - Text-Based Adventure Game
# Author: Michelle Zierk

# Function to display game introduction
def show_introduction():
    print("\nWelcome to Haunted Manor!")
    print("You are a paranormal investigator, summoned to uncover the secrets of this eerie estate.")
    print("Legend speaks of The Marionette, a haunted doll that lurks in the Grand Hall, trapping lost souls.")
    print("Your goal is to explore the manor, collect sacred artifacts, and uncover the truth before it's too late.")

# Function to display game instructions
def show_instructions():
    print("\nGame Instructions:")
    print("Move between rooms to explore!")
    print("Move commands: go North, go South, go East, go West")
    print("Add to Inventory: get 'item name'")
    print("Type 'exit' to quit the game.")
    print("The Secret Passage allows one-way movement only. Choose carefully!")

# Dictionary of rooms, possible movements, and items
rooms = {
    'Foyer': {'description': "The grand entrance of Blackwood Manor, filled with dust and echoes of the past.",
              'North': 'Library', 'West': 'Parlor', 'East': 'Dining Room'},
    'Library': {'description': "Rows of ancient books line the shelves. A Spellbook rests open on a lectern.",
                'South': 'Foyer', 'East': 'Kitchen', 'West': 'Study', 'item': 'Spellbook'},
    'Kitchen': {'description': "Cobweb-covered pots hang from the ceiling. A Cake sits untouched on the counter.",
                'West': 'Library', 'South': 'Dining Room', 'North': 'Grand Hall', 'item': 'Cake'},
    'Parlor': {
        'description': "A cozy yet eerie room with flickering candlelight. A Teddy Bear lies abandoned on a chair.",
        'North': 'Study', 'West': 'Secret Passage', 'East': 'Foyer', 'item': 'Teddy Bear'},
    'Study': {'description': "The desk is cluttered with papers. A hand Bell sits on the corner of the desk", 'East': 'Library', 'North': 'Attic', 'South': 'Parlor', 'item': 'Bell'},
    'Dining Room': {'description': "A large banquet table stands empty. A Knife is embedded in the wood.",
                    'West': 'Foyer', 'North': 'Kitchen', 'item': 'Knife'},
    'Secret Passage': {
        'description': "A hidden corridor within the walls. Choose carefully—this passage is one-way!",
        'North': 'Attic', 'West': 'Grand Hall', 'South': 'Foyer'},
    'Attic': {
        'description': "A dark, foreboding space filled with forgotten relics. A Balloon floats eerily in the center of the room.",
        'South': 'Study', 'item': 'Balloon'},
    'Grand Hall': {
        'description': "The heart of the manor, filled with eerie portraits whose eyes seem to follow you. The Marionette looms here, waiting...",
        'South': 'Kitchen'}
}

def show_status(current_room, inventory):
    print("\n----------------------")
    print(f"You are in the {current_room}")
    print(f"{rooms[current_room]['description']}")
    print(f"Inventory: {inventory}")
    directions = [direction for direction in rooms[current_room] if direction in ['North', 'South', 'East', 'West']]
    print("You can go: " + ", ".join(directions))
    if 'item' in rooms[current_room]:
        print(f"You see a {rooms[current_room]['item']}")
    print("----------------------")

def move_to_new_room(current_room, direction, inventory):
    if direction in rooms[current_room]:
        if current_room == 'Secret Passage':
            print("You have passed through the Secret Passage. You cannot return the same way!")
        if rooms[current_room][direction] == 'Grand Hall':
            if set(inventory) == {'Cake', 'Knife', 'Teddy Bear', 'Balloon', 'Spellbook', 'Bell'}:
                print("\nYou set the cake on the table with the knife stabbed into it.")
                print("The Teddy Bear holds the Balloon gently.")
                print("You open the Spellbook and recite the enchantment.")
                print("Finally, you ring the Bell three times...")
                print("The candles on the cake light themselves.")
                print("Ghostly confetti fills the air and a child's laughter echoes through the hall.")
                print("The Marionette smiles as she fades into the light. YOU WIN!")
                exit()
            else:
                print("\nThe Marionette's glassy eyes glow red... She takes your soul. GAME OVER!")
                exit()
        return rooms[current_room][direction]
    else:
        print("You can't go that way!")
        return current_room

def main():
    show_introduction()
    show_instructions()
    current_room = 'Foyer'
    inventory = []
    while True:
        show_status(current_room, inventory)
        move = input(" >> ").strip().lower()
        if move == 'exit':
            print("Thanks for playing!")
            break
        elif move.startswith("go "):
            direction = move.split()[1].capitalize()
            current_room = move_to_new_room(current_room, direction, inventory)
        elif move.startswith("get ") and 'item' in rooms[current_room]:
            item_name = rooms[current_room]['item']
            inventory.append(item_name)
            print(f"{item_name} collected!")
            del rooms[current_room]['item']
        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    main()
