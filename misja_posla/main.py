# main.py
import tools as ts
import actions as act
import game_characters as gc
import random
import time

print("     MISJA POSŁA \n")
input('')
gameover = False
while not gameover:
    player_choice = None
    # GAME START
    equipment = act.game_start()
    print(act.get_story("game_start.txt"))
    host_weapon = act.host_weapon_create()

    # weapons from the Host and player's choice
    player_choice = act.player_choice(host_weapon)
    act.purchase_equip(host_weapon, player_choice, equipment)
    act.use_coin(equipment)

    time.sleep(2)
    # in the RuneKeeper dwarf's hut
    print(act.get_story("dwarf_house.txt"))

    # purchase of weapons from the Dwarf
    dwarf_weapon = act.create_weapon()
    player_weapon = act.player_choice(dwarf_weapon)
    act.purchase_equip(dwarf_weapon, player_weapon, equipment)
    act.use_coin(equipment)

    time.sleep(2)
    # Dwarf's riddle
    print(act.get_story("dwarf_riddle.txt"))
    
    player_answer = input("Twoja odpowiedź: ")

    time.sleep(1)
    dwarf = gc.QuestioningDwarf()
    right_answer = dwarf.dwarf_reply_draw(player_answer)

    time.sleep(2)
    # paying for phial secret 
    if right_answer:
        act.phial_status(equipment)
    else:
        print(act.get_story("dwarf_paying.txt"))
        player_pays = input("\nCzy chcesz zapłacić za informacje? (t/n) ")
        if player_pays in ["t", "T"]:
            print("")
            act.phial_status(equipment)
            act.use_coin(equipment)

    time.sleep(2)
    # monster's atack
    print(act.get_story("meet_creature.txt"))        
    monsters = act.create_monsters()
    monster = random.choice(monsters)

    time.sleep(0)
    print(monster)
    time.sleep(4)
    print("Aby przeżyć, musisz działać. Co zrobisz?")
    player_weapon_choice = act.player_choice(equipment)
    use_weapon = act.obj_name(equipment, player_weapon_choice)
    act.use_equip(equipment, player_weapon_choice)

    time.sleep(2)
    # fight
    gameover = act.battle_result(use_weapon, equipment, monster)
        
    time.sleep(2)
    if not gameover: 
        # robbery
        print(act.get_story("meet_thief.txt"))
        robber = gc.RobberDwarf() 
        thief_fight = input("\nCzy staniesz z nim do walki? (t/n) ")
        if thief_fight in ["t", "T"]:
            weapon_robber = act.player_choice(equipment)
            time.sleep(2)
            if weapon_robber in ["sztylet", "maczuga"]:
                result =robber.robber_winning()
                if result:
                    act.use_equip(equipment, weapon_robber)
                    act.robb_coin(equipment)
            else:
                print("To był zły wybór. Zostałeś pokonany")
                act.robb_coin(equipment)
        else:
            print("Zostajesz okradziony.")
            act.robb_coin(equipment)

        time.sleep(2)
        # at the gates of the city 
        print(act.get_story("city_gates.txt"))

        time.sleep(1)
        act.persuading_the_guard(equipment)

        time.sleep(2)
        print(act.get_story("recognition.txt"))

        time.sleep(2)
        the_end = act.is_the_phial(equipment)
        if the_end == "happy end" : print(act.get_story("happy_end.txt"))
        elif the_end == "escape" : print(act.get_story("escape_end.txt"))
        else: print(act.get_story("dungeons_end.txt"))

    # END OF GAME
    
    again = input("\nGraj ponownie:  (t/n) ")
    if again in[ "n", "N"]: gameover = True
    else: gameover = False
        

