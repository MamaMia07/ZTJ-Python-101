# actions classes
import tools as ts
import game_characters as ch
import pathlib


def get_story(file_name):
    '''reading stories from files'''
    path = pathlib.Path.cwd()/"stories"/file_name
    with path.open(mode="r", encoding="utf-8") as file:
        return file.read()


def game_start():
    '''creation of initial equipment'''
    equipment = ts.Equipment()
    coins = ts.Coin() 
    phial = ts.Phial()
    safe = ts.SafeConduct()
    equipment.add_item(phial)
    equipment.add_item(coins)
    equipment.add_item(safe)
    return equipment


def host_weapon_create():
    '''creation of weapons of the Host'''
    hostweapon = ts.Equipment()
    knife = ts.Knife() 
    mace = ts.WoodenMace()
    hostweapon.add_item(knife)
    hostweapon.add_item(mace)
    return hostweapon


def create_weapon():
    '''creation of Dwarf's magic weapon'''
    weapons = ts.Equipment()
    sword = ts.Sword()
    bow = ts.Bow()
    runic_circle = ts.RunicCircle()
    weapons.add_item(sword)
    weapons.add_item(bow)
    weapons.add_item(runic_circle)
    return weapons


def print_help(stuff):
    print('')
    for element in stuff:
        print(f"{element} \n")
    print("")


def create_monsters():
    flying_creatute = ch.FlyingCreature()
    running_creature = ch.RunningCreature()
    monsters = [flying_creatute , running_creature]
    return monsters



def player_choice(stuff):
    '''getting the player's answer - choose piece of equipment'''
    playerchoice = ''
    if len(stuff.obj_list) == 0:
        print("Nie masz już nic")
    else:
        stuff.show_equipment()
        while playerchoice not in stuff.equip_list():
            playerchoice = input("Twój wybór: ")
            if playerchoice == "pomoc":
                print_help(stuff.obj_list)
    return playerchoice


def use_coin(stuff):
    for obj in stuff.obj_list:
        if obj.name == "monety":
            obj.paycoin()
            if obj.number == 0:
                print(f"Wykorzystałeś już wszystkie monety")
                stuff.remove_item(obj)


def robb_coin(stuff):
    ''' losing all coins '''
    for obj in stuff.obj_list:
        if obj.name == "monety":
            obj.number = 0
            print(f"Stracileś wszystkie monety")
            stuff.remove_item(obj)
            

def obj_name(stuff, name_):
    for obj in stuff.obj_list:
        if obj.name == name_:
            return obj


def phial_status(stuff):
    ''' revealing the secret of the phial''' 
    for obj in stuff.obj_list:
        if obj.name == "fiolka":
            obj.action_is_known = True
            print(obj)


def use_equip(stuff, playerchoice):
    ''' remove the used item'''
    for obj in stuff.obj_list:
        if obj.name == playerchoice:
            if playerchoice != "monety":
                stuff.remove_item(obj)
            else:
                use_coin(stuff)
     


def use_ineffect_weapon(weapon, creature, stuff):
    ''' when use of weaker weapons'''
    fiol = stuff.obj_list[0]
    weapon.ineffective_use(creature.name)
    if fiol.action_is_known == True:
        stuff.remove_item(fiol)
        print(get_story("phial_used.txt"))
        survive = True
    else:
        print(get_story("noeliksir.txt"))
        survive = False
    return survive


def purchase_equip(stuff, playerchoice, equip):
    for obj in stuff.obj_list:
        if obj.name == playerchoice:
            equip.add_item(obj)



def persuading_the_guard(stuff):
    bribe = bribe = player_choice(stuff)
    while bribe not in ["monety", "glejt"]:
        print("To raczej nie przekona strażnika... ")
        bribe = player_choice(stuff)
    print("OK. Przekonałeś go.")
    


def is_the_phial(stuff):
    ''' checking the equipment pieces,  choice of ending'''
    if any(obj.name == 'fiolka' for obj in stuff.obj_list):
        return "happy end"
    elif any(obj.name == 'monety' for obj in stuff.obj_list):
        return "escape"
    else: return "failure"
  

def battle_result(weapon, stuff, monster = None):
    ending = False
    if weapon.name == "krąg":
        effect = weapon.circle_use()
        if effect : weapon.effective_use(monster.name)
        else:
            survive = use_ineffect_weapon(weapon, monster, stuff)
            if not survive : ending = True
    elif weapon.name == "kusza":
        if monster.name == "wichrowy demon": weapon.effective_use(monster.name)
        else:
            survive = use_ineffect_weapon(weapon, monster, stuff)
            if not survive : ending = True
    elif weapon.name == "miecz":
        if monster.name == "demon ziemi": weapon.effective_use(monster.name)
        else:
            survive = use_ineffect_weapon(weapon, monster, stuff)
            if not survive : ending = True
    else:
        print("To był zły wybór. Zostałeś pozarty przez demona\nKONIEC GRY")
        ending = True
    return ending

