def start_haunted_castle():
    print("🏰 Welcome to the Mystery of the Haunted Castle!")
    print("You're a brave adventurer exploring an old, cursed castle.")
    print("You enter the castle and find two doors: one to the LIBRARY and one to the DUNGEON.")

    choice1 = input("Do you enter the 'library' or the 'dungeon'? ").lower()

    if choice1 == "library":
        library_path()
    elif choice1 == "dungeon":
        dungeon_path()
    else:
        print("⚠️ Invalid choice. You trip on a trapdoor and fall into darkness. Game over.")

def library_path():
    print("\n📚 The library is dusty and full of old books.")
    print("A ghostly figure whispers to you about a secret in a BOOK or a hidden LEVER behind a shelf.")

    choice2 = input("Do you investigate the 'book' or the 'lever'? ").lower()

    if choice2 == "book":
        print("\n📖 The book glows and opens a magical portal. You escape with treasure! 🏆 You Win!")
    elif choice2 == "lever":
        print("\n🪤 The lever triggers a trapdoor! You fall into a pit. Game over.")
    else:
        print("⚠️ Invalid choice. The ghost curses you. Game over.")

def dungeon_path():
    print("\n🔒 The dungeon is dark and cold. Chains hang from the walls.")
    print("You hear growls from the shadows. Do you LIGHT a torch or RUN back?")

    choice3 = input("Type 'light' or 'run': ").lower()

    if choice3 == "light":
        print("\n🔥 The torch reveals a secret passage. You follow it and escape safely! 🎉 You Win!")
    elif choice3 == "run":
        print("\n👻 A phantom chases you and you vanish into the darkness. Game over.")
    else:
        print("⚠️ Invalid choice. You get trapped forever. Game over.")

# Run the game
start_haunted_castle()
