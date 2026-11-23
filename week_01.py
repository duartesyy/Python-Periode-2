print("Hello Periode 2!")

player_name = input("What is your name?")
player_gold = 100
inventory = []

print(f"Hello {player_name}!, You have {player_gold} Gold")

shop_items = ("Sword","Shield","Potion","Bow")

for item in shop_items:
    print(item)


while True:
    print("=== Fantasy Item Shop ===")
    print("1. Buy Sword (50 gold)")
    print("2. Buy Shield (40 gold)")
    print("3. Buy Potion (20 gold)")
    print("4. Buy Bow (60 gold)")
    print("5. View Inventory")
    print("6. Exit Shop")

    choice = input("What would you like to do? ")

    if choice == "6":
        print("Thanks for visiting the shop!")
        break

    match choice:
        case "1":
            if player_gold >= 50:
                player_gold -= 50
                inventory.append("Sword")
                print("You bought a Sword!")
                print("Remaining gold:", player_gold)
            else:
                print("Not enough Gold!")

        case "2":
            if player_gold >= 40:
                player_gold -= 40
                inventory.append("Shield")
                print("You bought a Shield!")
                print("Remaining gold:", player_gold)
            else:
                print("Not enough Gold!")

        case "3":
           if player_gold >= 20:
               player_gold -= 20
               inventory.append("Potion")
               print("You bought a Potion!")
               print("Remaining gold:", player_gold)
           else:
               print("Not enough Gold!")

        case "4":
           if player_gold >= 60:
               player_gold -= 60
               inventory.append("Bow")
               print("You bought a Bow!")
               print("Remaining gold:", player_gold)
           else:
               print("Not enough Gold!")

        case "5":
            if len(inventory) == 0:
                print("Your inventory is empty!")
            else:
                print("Your inventory:")
                for item in inventory:
                    print(item)

        case "6":
            print("Thanks for visiting the shop,", player_name)
            print("You have", player_gold, "gold left.")
            break
              
        case _:
            print("Invalid choice! Please try again.")