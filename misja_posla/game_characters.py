# monsters classes

# karzeł
import random

class Dwarf():
    def __init__(self):
        self.name = name
        self.answers = []

    def dwarfs_statement (self):
        self.answer = random.choice(self.answers)
        return self.answer



class QuestioningDwarf(Dwarf):
    def __init__(self):
        self.name = "Mysterious Dwarf"
        self.answers = ["serce" , "rozum"]

    def dwarf_reply_draw(self, player):
        self.dwarfrepl = super().dwarfs_statement()
        if self.dwarfrepl != player :
            print(f"Prawidłowa odpowiedż to: {self.dwarfrepl}")
            return  False    
        else:
            print("Zgadłeś!")
            return True
            
        
    

class RobberDwarf(Dwarf):
    def __init__(self):
        self.name = "Dwarf Robber"
        self.answers = ["won", "lost"]

    def robber_winning(self):
        self.dwarfwin = super().dwarfs_statement()
        
        if self.dwarfwin == "won":
            print(f"Rabuś pokonał Cię w walce. Straciłeś swoją broń.")
            return  True    
        else:
            print("Wygrałeś tę walkę!")
            return False



class FlyingCreature():
    name = "wichrowy demon"
    def __str__(self):
        return f'''
Wichrowy demon:  demon materializujący się w powietrzu. Lata z dużą prędkością,
przez co jest trudnym celem. Jego skrzydła osiągają rozpiętość do 4m.
Długie, ostre szpony i potężne szczęki w kształcie dzioba sprawiają, ze jest
niezmiernie groźnym przeciwnikiem. Atakuje pikując i plując jadem na duże odległości.
'''


class RunningCreature():
    name = "demon ziemi"
    def __str__(self):
        return f'''
Demon ziemi:  demon materializujący się na ziemi. Długie i silne tylne łapy pozwalają
mu na bardzo szybki bieg. Przednie łapy wyposażone są w długie, ostre szpony,
którymi jest w stanie rozszarpać najtwardsza zbroję. Wydłużony pysk pełen ostrych zebów
i kolczasty ogon. są jego bronią. Jedna z najbardziej agresywnych odmian demonów.
'''
