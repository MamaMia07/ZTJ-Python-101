# tools classes:
import random

class Equipment():
    
    def __init__(self):
        self.obj_list =[]
        self.eqlist = []
        
    def add_item(self, element):
        self.obj_list.append(element)
        return self.obj_list
    
    def remove_item(self, element):
        self.obj_list.remove(element)
        return self.obj_list

    def show_equipment(self):
        print("Możesz wybrać:")
        for element in self.obj_list:
            print(f"{element.name}   ", end = '')
        print("   /pomoc \n")

    def equip_list(self):
        for element in self.obj_list:
            self.eqlist.append(element.name)
        return self.eqlist
            
    def __del__(self):
        pass


    

class Tools():
    def __init__(self):
       self.name = name

    def effective_use(self, demon_name):
        print(f'''Dzięki temu, że broń była chroniona runami, udało Ci się pokonać demona.
Jednak w walce broń uległa zniszczeniu. Resztę nocy spędziłeś w lesie''')

    def ineffective_use(self, demon_name):
        print(f'''Mimo że broń była chroniona runami, to była ciężka potyczka.
Ostatecznie walkę tę wygrałeś, ale {demon_name} atakując zdołał zadać Ci powazne rany.
Broń w walce uległa zniszczeniu.''')
    
    def pointless_use(self, demon_name):
        print("To nie był dobry wybór")

    def __del__(self):
        print(f"Wybrałeś: {self.name}")


        
    
class Coin():
    number = 4
    name = "monety"

    def paycoin(self):
        if self.number > 0:
            self.number -= 1
            print(f"Wykorzystałeś 1 monetę. Pozostały: {self.number}")
            return self.number
        
    def __del__(self):
        pass    

    def __str__(self):
        return f"{self.name}: pozostały Ci {self.number}, wykonane są z czystego złota"





class Phial(Tools):
    name = "fiolka"
    def __init__(self):
        self.action_is_known = False

    def __str__(self):
        if not self.action_is_known:
            return f"{self.name}: zawiera substancję, której przeznaczenia nie jesteś \
w stanie sobie przypomnieć"
        else:
            return f"{self.name}: zawiera cenny eliksir uzdrawiający, który może \
uleczyć rany zadane przez demony"


class SafeConduct(Tools):
    def __init__(self):
        self.name = "glejt"
    def __str__(self):
        return f"{self.name} królewski:  dokument wydany przez władcę, zezwalający \
na przejazd przez terytorium królestwa"




class Knife(Tools):
    def __init__(self):
        self.name = "sztylet"
    def __str__(self):
        return f"{self.name}: ostry, wykonany z dobrej jakości stali nierdzewnej \
z ręcznie wykonanym ozdobnym trzonem."



class WoodenMace(Tools):
    def __init__(self):
        self.name = "maczuga"
    def __str__(self):
        return f"{self.name}:  pałka wykonana z twardego drewna z masywną głowicą, \
nabijaną metalowymi ćwiekami." 



class Sword(Tools):
    def __init__(self):
        self.name = "miecz"
    def __str__(self):
        return f'''{self.name}:  wyryte na nim runy obronne sprawiają, że jest
skuteczna bronią w bezpośredniej walce z demonami ziemi i ognia'''


    

class Bow(Tools):
    def __init__(self):
        self.name = "kusza" 
    def __str__(self):
        return f'''{self.name} i kołczan strzał:  to broń pozwalająca na walkę w dystansie, 
skuteczna w obronie przed latającymi demonami powietrza'''




class RunicCircle(Tools):
    def __init__(self):
        self.name = "krąg"

    def effective_use(self, demon_name):
        print(f'''Runiczny krąg pozwolił Ci się ukryć za magiczną barierą.
Silna magia run skutecznie chroniła Cię przed atakami rozwścieczonego demona.
Pomimo jego wrzaskow i ustawicznych prob przebicia bariery, udalo Ci sie przetrwac
do switu. Blask wschodzącego słońca odpędził wszystke demony.
''')

    def ineffective_use(self, demon_name):
        print(f'''Runiczny krąg pozwolił Ci się ukryć za magiczną barierą.
Jednak uszkodzenia jednego elementu spowodowały wyrwę w barierze,
przez którą demon zadał Ci poważne rany.
''')

    def circle_use(self):
        self.effect = random.choice([True , False])
        return self.effect
       
    def __str__(self):
        return f'''runiczny krąg:  wykonany z drewnianych elementów z namalowanymi
magicznymi runami, połączonych ze sobą sznurem. Po rozłożeniu w okrag runy tworzą
magiczną barierę chroniącą przed demonami.Bariera jest skuteczna tylko jeśli
żaden z runów nie jest uszkodzony.'''
