import random
import time
import os

# Optional: Clear screen for cleaner output
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ASCII dice faces
DICE_FACES = {
    1: (
        "┌─────┐",
        "│     │",
        "│  •  │",
        "│     │",
        "└─────┘",
    ),
    2: (
        "┌─────┐",
        "│ •   │",
        "│     │",
        "│   • │",
        "└─────┘",
    ),
    3: (
        "┌─────┐",
        "│ •   │",
        "│  •  │",
        "│   • │",
        "└─────┘",
    ),
    4: (
        "┌─────┐",
        "│ • • │",
        "│     │",
        "│ • • │",
        "└─────┘",
    ),
    5: (
        "┌─────┐",
        "│ • • │",
        "│  •  │",
        "│ • • │",
        "└─────┘",
    ),
    6: (
        "┌─────┐",
        "│ • • │",
        "│ • • │",
        "│ • • │",
        "└─────┘",
    )
}

def print_dice_face(value):
    for line in DICE_FACES[value]:
        print(line)

def animate_roll():
    for _ in range(5):
        roll = random.randint(1, 6)
        clear_screen()
        print("Rolling the dice...\n")
        print_dice_face(roll)
        time.sleep(0.3)

def main():
    input("Press Enter to roll the dice...")
    animate_roll()
    final_roll = random.randint(1, 6)
    clear_screen()
    print("You rolled:\n")
    print_dice_face(final_roll)

if __name__ == "__main__":
    main()
