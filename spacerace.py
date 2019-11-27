def game():
    # whole game put into a single function so it can be restarted from the beginning
    
    import time # import necessary libraries
    import sys                                                                                  
    import random
    class color: # allows to color and underline text
       BOLD = '\033[1m'
       UNDERLINE = '\033[4m'
       END = '\033[0m'
    
    def write_level():
        # letter by letter printing for each level - Michael
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.02)

    def write_letter():    
        # letter by letter printing for each sentence - Michael
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.04)      

    def restart():
        # prompt allowing the player to restart the game or to quit the game - Tim
        print("\nWould you like to play again? Enter [Y] to restart. Enter [N] to quit")
        restart = ""
        while restart !="y" and restart !="n":
            restart = input().lower()
            if restart == "y":
                game()
            elif restart == "n":
                sys.exit("Thanks for playing!")
            else: 
                print("ERROR: Enter Y or N")
                
    def win_lose():
        # end game scenario, end game if user health or Gorg leader health is less than or equal to 0 - Tim
        if ha["health"] <= 0:
            for i in range(5):
                time.sleep(1)
                print(i+1) 
            print("\nYou have failed to save the galaxy!")    
            restart()
        elif gl["health"] <= 0:
            for i in range(5):
                time.sleep(1)
                print(i+1)
                print("             __\n" # art by Joan G. Stark
            "        _   / /|\n"
            "       |\\  \/_/\n"
            "       \_\| / __              \n"
            "          \/_/__\           .-=='/~\\n"
            "   ____,__/__,_____,______)/   /{~}}}\n"
            "   -,------,----,-----,---,\'-' {{~}}\n"
            "                            '-==.\}/)\n")
            print("\nThe Gorg leader has been defeated! You are a hero of epic proportions! You've single-handedly saved the galaxy from destruction!")
            restart()
   
    def fail_mission():
        # fail mission notification and display restart prompt - ChiaWen
        for i in range(5):
            time.sleep(1)
            print(i+1)  
        restart()

    # game introduction and title screen - Tim
    print("#####################")
    print(color.UNDERLINE + "Welcome to Space Race" + color.END)
    print("#####################\n")
    intro = "Welcome to the planet Brierton. The planet is in a state of chaos and needs your assistance. Gorgs have taken over and are threatening to rule the galaxy. It's a race against time before the Gorgs conquer the planet and force its inhabitants into slavery. The entire balance of the galaxy is in your hands.\n\n"
    for letter in intro:
        write_letter()    

    # character selection, assigns health and attack value based on chosen character - Cory
    ha = {"health": 0, "attack": 0}
    print("Choose your character:")
    print("[1] Warrior - High health, Low attack\n[2] Assassin - Medium armor, Medium attack\n[3] Magician - Low health, High attack")
    character = "" # choose character type by option 1, 2, or 3
    while character != "1" and character != "2" and character != "3":
        character = input()
        if character == "1":
            print("You chose " + color.UNDERLINE + "WARRIOR" + color.END)
            ha["health"] += 40
            ha["attack"] += 20
        elif character == "2":
            print("You chose " + color.UNDERLINE + "ASSASSIN" + color.END)
            ha["health"] += 30
            ha["attack"] += 30
        elif character == "3":
            print("You chose " + color.UNDERLINE +"MAGICIAN" + color.END)
            ha["health"] += 20
            ha["attack"] += 40
        else:
            print("ERROR: Please select by number!")

    name = input("Enter your character's name: ")
    print("\nEverything depends on you, " + name + "!")

    # level one title screen - Cory (ASCII retrieved from http://patorjk.com/)
    print("\nEntering:")
    welcome1 = (
    "  _                             _         _ \n"
    " | |       ___  __   __   ___  | |  _    / |\n"
    " | |      / _ \ \ \ / /  / _ \ | | (_)   | |\n"
    " | |___  |  __/  \ V /  |  __/ | |  _    | |\n"
    " |_____|  \___|   \_/    \___| |_| (_)   |_|\n")
    for letter in welcome1:
        write_level()

    # level one introduction and weapon selection, adds health and attack based on chosen weapons - Tim
    level_oneA = "\nTake some time to gather supplies that will help you along your way to victory.\n"
    for letter in level_oneA:
        write_letter()
    print("\nYou've entered the armory of the Briertonian High Council. Choose your weapons:")
    print("[1] The Sword and Shield of Truth\n[2] The Bow and Cloak of Wonders\n[3] The Wand and Book of Destiny")
    weapon = "" # choose weapons by option 1, 2, or 3
    while weapon != "1" and weapon != "2" and weapon != "3":
        weapon = input() 
        if weapon == "1":
            print("You chose " + color.UNDERLINE + "The Sword and Shield of Truth" + color.END)  
            print(color.UNDERLINE + "\nThe old-fashioned sword and shield, good choice. Adding 20 health and 10 attack." + color.END)
            ha["health"] += 20
            ha["attack"] += 10
        elif weapon == "2":
            print("You chose " + color.UNDERLINE + "The Bow and Cloak of Wonders" + color.END)
            print(color.UNDERLINE + "\nSo you like to do damage while staying alive, smart choice. Adding 15 health and 15 attack." + color.END)
            ha["health"] += 15
            ha["attack"] += 15
        elif weapon == "3":
            print("You chose " + color.UNDERLINE + "The Wand and Book of Destiny" + color.END)
            print(color.UNDERLINE + "\nYou're a wizard " + name + ". Adding 10 health and 20 attack." + color.END)
            ha["health"] += 10
            ha["attack"] += 20
        else: 
            print("ERROR: Please select by number!")

    # inventory selection, add chosen items to a dictionary - Cory
    level_oneB = "\nThis might be a long day, grab some supplies and maybe something to drink to help keep you energized.\n"
    for letter in level_oneB:
        write_letter()
    inventory = {}
    print("\nSelect an item:")
    print("[1] Cookie\n[2] Gluten-Free Bread\n[3] Refreshing ice cold Coca-Cola")
    item = "" # choose first item by option 1, 2, or 3
    while item != "1" and item != "2" and item != "3":
        item = input()
        if item == "1":
            inventory.update({"Cookie":"+5 Attack"})
        elif item == "2":
            inventory.update({"Gluten-Free Bread":"+10 Health"})
        elif item == "3":
            inventory.update({"Refreshing ice cold Coca-Cola":"-5 Health"})
        else:
            print("ERROR: Please select by number!")

    print("\nInventory:\n",inventory)

    level_oneC = "\nLet's grab one more thing before we go.\n"
    for letter in level_oneC:
        write_letter()
    item2 = "" # choose second item by option 1, 2, or 3
    print("\nSelect an item:")
    print("[1] Starbucks Pumpkin Spice Latte\n[2] Canned Spinach\n[3] Advil\n")
    while item2 != "1" and item2 != "2" and item2 != "3":
        item2 = input()
        if item2 == "1":
            inventory.update({"Starbucks Pumpkin Spice Latte":"-10 Health"})
        elif item2 == "2":
            inventory.update({"Canned Spinach":"+5 Attack"})
        elif item2 == "3":
            inventory.update({"Advil":"+5 Health"})
        else:
            print("ERROR: Please select by number!")

    print("\nInventory:\n",inventory)

    level_oneD = "\nGreat! These will definitely help out later...depending on your choices.\n"
    for letter in level_oneD:
        write_letter()

    # level two introduction and title screen
    print("\nEntering:")
    welcome2 = (
    "  _                    _       ___  \n"
    " | |                  | |     |_  \ \n"
    " | |     _____   _____| | _     ) |\n"
    " | |    / _ \ \ / / _ \ |(_)   / / \n"
    " | |___|  __/\ V /  __/ |     / /_ \n"
    " |______\___| \_/ \___|_|(_) |____|\n")
    for letter in welcome2:
        write_level()

    level_twoA = "\nNow that you're equipped you should probably get on with saving the planet. Time is of utmost importance! However, there's an unexplored room in the council building.\n"
    for letter in level_twoA:
        write_letter()
    print("\nWhat do you do?")
    print("[1] Explore the room\n[2] Continue on with your mission")
    choice = "" # choose a direction by option 1 or 2 - Michael
    while choice != "1" and choice != "2":
        choice = input()
        if choice == "1":
            print("\nThe room was booby trapped. You died and failed to save the planet, resulting in the death of millions. Good job")
            fail_mission()
        if choice == "2":
            level_twoB = "\nYou leave the council building in search of the Gorg leader. But first, lets get ready for a fight.\n"
            for letter in level_twoB:
                write_letter()
        else:
            print("ERROR: Please select a number!")

    def inventory_select():
        # select an item to use from inventory, add effect of item. Remove item from inventory after use - ChiaWen
        print("\nInventory:",inventory)
        use_inventory = input("\nType the name of the item you want to use, or type Skip\n")
        use_inventory = use_inventory.lower()
        while use_inventory != "skip":
            if use_inventory == "cookie":
                del inventory["Cookie"]
                ha["attack"] += 5
                break
            elif use_inventory == "gluten-free bread":
                del inventory["Gluten-Free Bread"]
                ha["health"] += 10
                break
            elif use_inventory == "refreshing ice cold coca-cola":
                del inventory["Refreshing ice cold Coca-Cola"]
                ha["health"] -= 5
                break
            elif use_inventory == "starbucks pumpkin spice latte":
                del inventory["Starbucks Pumpkin Spice Latte"]
                ha["health"] -= 10
                break
            elif use_inventory == "canned spinach":
                del inventory["Canned Spinach"]
                ha["attack"] += 5
                break
            elif use_inventory == "advil":
                del inventory["Advil"]
                ha["health"] += 5
                break
            else:
                print("ERROR: Type the correct item name from your inventory or type Skip")
                use_inventory = input()
    inventory_select()
    
    # fight against Gorg minions, guess the right number between 1-6 - ChiaWen
    level_twoB = "\n\nYou find a horde of Gorg minions in the main plaza. The Briertonians have set a bomb but couldn't activate it in time. You see the detonator in front of you in the hands of a dead Briertonian. Your only chance is to grab the detonator and guess the correct authentication code, but you better hurry...the Gorgs have spotted you and are heading straight for you!\n" 
    for letter in level_twoB:
        write_letter()
    random_number = random.randint(1,6)
    user_guess = input("\nEnter a number between 1 and 6: ")
    user_guess = int(user_guess)
    min = 1
    max = 6
    while user_guess != random_number and ha["health"] != 0:
        ha["health"] -= 5
        if (ha["health"] == 0):
            break
        if user_guess < random_number:
            min = user_guess
            print("\nYou were hit by a Gorg minion attack. Your health is:", ha["health"])
            print("\nEnter a number between", min, "and", max)
        elif user_guess > random_number:
            max = user_guess
            print("\nYou were hit by a Gorg minion attack. Your health is:", ha["health"])
            print("\nEnter a number between", min, "and", max)
        temp = user_guess
        user_guess = int(input(""))
        if (user_guess > max or user_guess < min):
            user_guess = temp        
    if (ha["health"] != 0 and user_guess == random_number):
        level_twoC = "\n[[ACCESS GRANTED]] You guessed the correct authentication code and detonated the bomb in time, killing all the Gorg minions.\n"
        for letter in level_twoC:
            write_letter()
    else:
        print("\nYOU ARE DEAD!!!!")
        fail_mission()

    # level three introduction and title screen
    print("\nEntering:")
    welcome3 = (  
    "  _                    _       ____ \n"
    " | |                  | |     |__  \ \n" 
    " | |     _____   _____| |      __) | \n"
    " | |    / _ \ \ / / _ \ | (_) |__ < \n"
    " | |___|  __/\ V /  __/ |  _   __) |\n"
    " |______\___| \_/ \___|_| (_) |____/ \n")
    for letter in welcome3: 
        write_letter()

    level_threeA = "\nThe minions are slain. It's time to face the Gorg leader. Here's another chance to use an item from your inventory.\n"
    for letter in level_threeA:
        write_letter()

    inventory_select()
    
    # final boss fight, set boss health to 225 - Tim
    gl = {"health" : 225}
    level_threeB = "\nThe Gorg leader is directly ahead and hasn't spotted you yet. How will you attack?\n"
    for letter in level_threeB:
        write_letter()
    print("\nChoose a plan of attack:")
    print("[1] Attack from the front\n[2] Attack from the back")
    attack = "" # choose plan of attack by option 1 or 2
    while attack != "1" and attack != "2":
        attack = input()
        if attack == "1": 
            print("The Gorg leader saw you coming and easily countered your attack with his flaming whip.")
            gl_attack = random.randint(20,25) # Gorg leader deals random damage between 20-25
            print("\nGorg leader dealt %d damage!" % gl_attack)
            ha["health"] -= gl_attack
            print("\nYour health is: ", ha["health"])
            win_lose()
        elif attack == "2":
            print("You managed to sneak up on the Gorg Leader and deal an attack.")
            print("\nYou dealt %d damage!" % ha["attack"])
            gl["health"] -= ha["attack"]
            print("Gorg leader health is: ", gl["health"])
            win_lose()
        else:
            print("ERROR: Please select by number!")

    level_threeC = "\nThe Gorg leader leaps into the air preparing his special attack, The Flaming Whiplash of Doom...Do you choose to attack or do you choose to defend?\n"
    for letter in level_threeC:
        write_letter()
    print("\nChoose a strategy:")
    print("[1] Attack before he can strike\n[2] Get out of the way")
    strategy = "" # choose strategy by option 1 or 2
    while strategy != "1" and strategy != "2":
        strategy = input()
        if strategy == "1":
            print("You chose to attack at precisely the right time when he was the most vulnerable.")
            print("\nYou dealt %d damage!" % (ha["attack"]*2)) # deal user attack damage multiplied by 2 to the Gorg leader
            gl["health"] -= (ha["attack"]*2)
            win_lose()
        elif strategy == "2":
            print("The Gorg leader anticipated your cowardice and will now destroy you.")
            gl_special = random.randint(75,80) # Gorg leader deals random damage between 75-80
            print("\nGorg leader dealt %d damage!" % gl_special)
            ha["health"] -= gl_special
            print("\nYour health is: ", ha["health"])
            win_lose()
        else:
            print("ERROR: Please select by number!")

    level_threeD = "\nThe Gorg leader is weak, it's time to finish him!\n"
    for letter in level_threeD:
        write_letter()
    print("\nChoose a power attack:")
    print("[1] Infinity Strike\n[2] Spirit Blade")
    power_attack = "" # choose final attack by option 1 or 2
    while power_attack != "1" and power_attack != "2":
        power_attack = input()
        if power_attack == "1":
            print("Fabulous choice!")
            print("\nYou dealt %d damage!" % ha["attack"] * 10) # deal user attack damage to the Gorg leader 10 times in a row
            gl["health"] -= ha["attack"] * 10
            win_lose()
        elif power_attack == "2":
            print("Touched by an angel!")
            print("\nYou dealt %d damage!" % ha["attack"] ** 2) # deal user attack damage squared to the Gorg leader
            gl["health"] -= ha["attack"] ** 2
            win_lose()
        else: 
            print("ERROR: Please select by number!")
game() 