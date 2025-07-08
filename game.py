import random
strength=0
intelligence=0
defense=0
HP=0
dexterit=0
name=""
current_room=0
has_chest=bool(False)
has_creature=bool(False)
has_trap=bool(False)
is_empty=bool(False)
active_trap = bool(False)
looted=bool(False)
combated=bool(False)
creature_number=0
chest_number = 0
choice2=0
itens=[["stick","leather gloves","shoes","water bottle","empty bottle"],
    ["iron sword","leather chestplate","hat","dry berries","arrows"],
    ["bow","helmet","reinforced boots","dry meat","dagger","bandages"],
    ["steel axe","chainmail chestplate","iron boots","potion of heal","iron balls"],
    ["crossbow","steel chestplate","steel pants","darts","medicine"],
    ["musket","instant heal potion","strenght potion"]
]
inventory=[]
equiped_hand=''
equiped_feet=''
equiped_weapon=''
equiped_chest=''
equiped_legs=''
equiped_head=''
equiped_feet=''
def set_defense():
    global equiped_hand, equiped_chest, equiped_legs, equiped_head, equiped_feet
    try:
        chest=equiped_chest
        tmp=""
        chest=chest.split()
        if len(chest) >= 1:
            if len(chest) > 1:
                chest=str(chest[0]+"-"+chest[1])
            else:
                chest=str(chest.strip())
        else:
            chest="placeholder"
        tmp=chest + ".txt"
        tmp="itens/"+tmp
        file_chest=open(tmp,"r")
        file_chest.seek(0)
        sum_chest=int(file_chest.readlines()[3].strip())
    except FileNotFoundError :
        sum_chest=0
    try:
        hand=equiped_hand
        tmp=""
        hand=hand.split()
        if len(hand) >= 1:
            if len(hand) > 1:
                hand=str(hand[0]+"-"+hand[1])
            else:
                hand=str(hand.strip())
        else:
            hand="placeholder"
        tmp=hand + ".txt"
        tmp="itens/"+tmp
        file_hand=open(tmp,"r")
        file_hand.seek(0)
        sum_hand=int(file_hand.readlines()[3].strip())
    except FileNotFoundError :
        sum_hand=0
    try:
        head=equiped_head
        tmp=""
        head=head.split()
        if len(head) >= 1:
            if len(head) > 1:
                head=str(head[0]+"-"+head[1])
            else:
                head=str(head.strip())
        else:
            head="placeholder"
        tmp=head + ".txt"
        tmp="itens/"+tmp
        file_head=open(tmp,"r")
        file_head.seek(0)
        sum_head=int(file_head.readlines()[3].strip())
    except FileNotFoundError :
        sum_head=0
    try:
        legs=equiped_legs
        tmp=""
        legs=legs.split()
        if len(legs) >= 1:
            if len(legs) > 1:
                legs=str(legs[0]+"-"+legs[1])
            else:
                legs=str(legs.strip())
        else:
            legs="placeholder"
        tmp=legs + ".txt"
        tmp="itens/"+tmp
        file_legs=open(tmp,"r")
        file_legs.seek(0)
        sum_legs=int(file_legs.readlines()[3].strip())
    except FileNotFoundError :
        sum_legs=0
    try:
        feet=equiped_feet
        tmp=""
        feet=feet.split()
        if len(feet) >= 1:
            if len(feet) > 1:
                feet=str(feet[0]+"-"+feet[1])
            else:
                feet=str(feet.strip())
        else:
            feet="placeholder"
        tmp=feet + ".txt"
        tmp="itens/"+tmp
        file_feet=open(tmp,"r")
        file_feet.seek(0)
        sum_feet=int(file_feet.readlines()[3].strip())
    except FileNotFoundError :
        sum_feet=0  
    return sum_chest+sum_feet+sum_hand+sum_head+sum_legs
def starter_itens():
    inventory.append("iron sword")   #adds the starter sword to inventory
    inventory.append("leather chestplate") #adds the starter armor to inventory
def character_roll():
    global name, dexterity, strength, intelligence, HP, defense, inventory, equiped_weapon, equiped_hand, equiped_chest, equiped_legs,set_defense, equiped_head, equiped_feet #imports character variables from main.py
    name = input("Your name: ")
    equiped_weapon=(inventory[0])
    equiped_chest=(inventory[1])
    strength = random.choice(range(9,19))
    intelligence = random.choice(range(9,19))
    dexterity = random.choice(range(9,19))
    defense = set_defense()
    HP=100
    print("------------------------")
    print(f"name: {name}")
    print(f"str: {strength}")
    print(f"dex: {dexterity}")
    print(f"int: {intelligence}")
    print(f"DEF: {defense}, HP: {HP}")
    print("------------------------")
    print("GAME START!")
    print("------------------------")


def generate_room():
    global current_room, has_chest, has_creature, has_trap, is_empty, creature_number, chest_number, combated, looted
    current_room += 1
    has_creature = False
    has_chest = False
    has_trap = False
    is_empty = False
    creature_number = 0
    if random.randint(1,101) <= 30:
        has_creature = True
        combated = False
        if current_room < 20:
            creature_number = 1
        elif current_room > 20:
            if current_room < 40:
                creature_number = random.randint(1,3)
        elif current_room >= 40:
            creature_number = random.randint(1,4)
    if random.randint(0,101) <= 70:
        has_chest = True
        looted = False
        chest_number = random.randint(1,4)
        if random.randint(1,101) <= 5:
            has_trap = True
    if has_chest==False:
        looted=True
        if has_creature==False:
            is_empty = True
            if random.randint(1,101) <= 5:
                has_trap=True
    if has_creature == False:
        combated = True
        
def combat():
    global defense, strength, dexterity, combated, inventory, equiped_weapon, creature_number, HP, choice2, enter_room
    print("------------------------")
    print(f"you entered in combat with {creature_number} creatures!")
    print("------------------------")
    if creature_number == 1:
        creature1_HP = 30
        creature2_HP = 0
        creature3_HP = 0
    elif creature_number == 2:
        creature1_HP = 30
        creature2_HP = 30
        creature3_HP = 0
    elif creature_number == 3:
        creature1_HP = 30
        creature2_HP = 30
        creature3_HP = 30
    while creature1_HP > 0 or creature2_HP > 0 or creature3_HP > 0:
        print("------------------------")
        print(f"your HP: {HP}")
        print(f"creature 1's HP: {creature1_HP}")
        if creature_number == 2:
            print(f"creature 2's HP: {creature2_HP}")
        elif creature_number == 3:
            print(f"creature 2's HP: {creature2_HP}")
            print(f"creature 3's HP: {creature3_HP}")
        print("------------------------")
        print("actions:")
        print("(1) attack")
        choice2 = int(input(":"))
        if choice2 == 1:
            if equiped_weapon == "bow":
                if "arrows" in inventory:
                    if random.randint(1,16) <= dexterity:
                        print("You hit!")
                        creature1_HP -= 7
                        creature2_HP -= 7
                        creature3_HP -= 7
                        if random.randint(1,21) <= dexterity:
                            HP -= 5 * creature_number
                            print("you were hit")
                    else:
                        print("You missed!")
                else:
                    print("you have no arrows, weapon switched to iron sword!")
                    equiped_weapon = "iron sword"
            elif equiped_weapon == "crossbow":
                if "darts" in inventory:
                    if random.randint(1,16) <= dexterity:
                        print("You hit!")
                        creature1_HP -= 11
                        creature2_HP -= 11
                        creature3_HP -= 11
                        if random.randint(1,21) <= dexterity:
                            HP -= 5 * creature_number
                            print("you were hit")
                    else:
                        print("you missed!")
                else:
                    print("you have no darts, weapon switched to iron sword!")
                    equiped_weapon = "iron sword"
            elif equiped_weapon == "musket":
                if "iron balls" in inventory:
                    if random.randint(1,16) <= dexterity:
                        print("You hit!")
                        creature1_HP -= 22
                        creature2_HP -= 22
                        creature3_HP -= 22
                        if random.randint(1,21) <= dexterity:
                            HP -= 5 * creature_number
                            print("you were hit")
                    else:
                        print("you missed!")
                else:
                    print("you have no iron balls, weapon switched to iron sword!")
                    equiped_weapon = "iron sword"
            else:
                if random.randint(1,16) <= strength:
                    print("You hit!")
                    weapon = equiped_weapon
                    tmp=""
                    weapon=weapon.split()
                    if len(weapon) >= 1:
                        if len(weapon) > 1:
                            weapon=str(weapon[0]+"-"+weapon[1])
                        else:
                            weapon=str(weapon.strip())
                    else:
                        weapon="placeholder"
                    tmp=weapon + ".txt"
                    tmp="itens/"+tmp
                    file_weapon=open(tmp,"r")
                    file_weapon.seek(0)
                    damage=int(file_weapon.readlines()[2].strip())
                    creature1_HP -= damage
                    creature2_HP -= damage
                    creature3_HP -= damage
            if random.randint(1,21) <= dexterity:
                HP -= 5 * creature_number
                print("you were hit")
    combated = True           #add have consumables option
    print("------------------------")
    enter_room()


def loot():
    global inventory, chest_number, itens, enter_room, looted
    chances=[47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,11,11,11,11,11,11,11,11,11,11,11,9,9,9,9,9,9,9,9,9,6,6,6,6,6,6,3,3,3]
    for x in range(0,chest_number):
        item=""
        if random.choice(chances) == 47:
            item = random.choice(itens[0])
            inventory.append(item)
            print(f"you gained a {item}")
        elif random.choice(chances) == 24:
            item = random.choice(itens[1])
            inventory.append(item)
            print(f"you gained a {item}")
        elif random.choice(chances) == 11:
            item = random.choice(itens[2])
            inventory.append(item)
            print(f"you gained a {item}")
        elif random.choice(chances) == 9:
            item = random.choice(itens[3])
            inventory.append(item)
            print(f"you gained a {item}")
        elif random.choice(chances) == 6:
            item = random.choice(itens[4])
            inventory.append(item)
            print(f"you gained a {item}")
        elif random.choice(chances) == 3:
            item = random.choice(itens[5])
            inventory.append(item)
            print(f"you gained a {item}")
    looted=True
    enter_room()

def look_inventory(): #add consumables and equip options!!!
    global inventory, HP, strength, dexterity, intelligence
    print(inventory)
    print(f"hp: {HP}")
    print("stats:")

    enter_room()

def trapped():
    global active_trap, HP
    if active_trap == True:
        HP -= 7

def rest():
    global HP
    if HP >= 80:
        HP = 100
    elif HP < 80:
        HP += 20
    print("restored 20 HP")

def enter_room():
    global current_room, has_chest, has_creature, has_trap, is_empty, creature_number, chest_number, generate_room
    global generate_room, intelligence, active_trap, combated, looted, combat, loot, choice2, rest
    choice2 = 0
    if has_trap == True:
        if random.randint(1,16) >= intelligence:
                print("you just activated a trap on the room!")
                print("-7 life")
                active_trap = True
                trapped()
    if is_empty == False:
        print("------------------------")
        print(f"Room number: {current_room}")
        print("------------------------")
        print("you enter a new room and see:")
        if has_chest == True:
            print(f"{chest_number} chest(s)")
        if has_creature == True:
            print(f"{creature_number} creature(s)")
        print("------------------------")
        while choice2 not in [1,2,3,4]:
            if has_chest == True:
                if looted == False:
                    print("(1) Loot chests")
            if has_creature == True:
                if combated == False: 
                    print("(2) Combat")
            if looted == True:
                if combated == True:
                    print("(3) Next room")
            print("(4) inventory")
            choice2 = int(input(":"))
            if choice2 == 1:
                loot()
            elif choice2 == 2:
                combat()
            elif choice2 == 3:
                return 0
            elif choice2 == 4:
                look_inventory()


    elif is_empty == True:
        print("------------------------")
        print("this room is empty, \n here you can rest and regain some health")
        print("------------------------")
        rest()
        while choice2 not in [1,2]:
            print("(1) Next room")
            print("(2) inventory")
            choice2 = int(input(":"))
            if choice2 == 1:
                return 0
            elif choice2 == 2:
                look_inventory()
            else:
                print("invalid choice!")
         


def game_start():
    global character_roll, starter_itens, set_defense, generate_room, enter_room
    choice = 0
    print("D U N G E O N")
    print("      of     ")
    print("D I S C O R D")
    print("________________")
    while choice not in range(1,3):
        print("(1) Start game")
        print("(2) Exit game")
        choice = int(input(":"))
        if choice == 2:
            exit()
        elif choice == 1:
            starter_itens()
            character_roll()
            while True:
                generate_room()
                enter_room()
        else:
            print("Invalid choice!")

game_start()


