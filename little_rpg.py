import random

def CreateCharacter():
    print("Noc zapanowala na niebie. Jestes w lesie i dostrzeles ogien. Podchodzisz blizej i napotykasz maga, ktory robi magiczne sztuczki na ognisku.")
    print("- Oczekiwalem Ciebie, widzialem w ogniu jak kroczysz lasem...")
    print("Mag nieco zachwial sie, kiedy podparty o magiczny kij zapytal sie.")
    print("- Jak masz na imie?")
    
    PlayerName = input("Twoje imie: ")
    print("Witaj " + PlayerName)

def GoodBye():
    print("Dziekuje za granie w moja gre, ktora napisalem w czasie nauki Pythona :)!")

PlayerName = "Damian"
MaxHealthPoints = 100
HealthPoints = 100
Gold = 0
MonstersKilled = 0

GameRunning = True

CreateCharacter()

while GameRunning:
    print("__________________________________________________________________________________")
    print("| " + PlayerName)
    print("| Punkty zycia: " + str(HealthPoints))
    print("| Zloto: " + str(Gold))
    print("| Zabite potwory: " + str(MonstersKilled))
    print("__________________________________________________________________________________")
    
    print("\n\n")
    
    print("[1]" + "Statystyki postaci")
    print("[2]" + "Walka z losowym stworem")
    print("[3]" + "Odwiedz Druida. Koszt 20 sztuk zlota.")
    print("[0]" + "Wyjscie z gry.")
    
    Decision = input("Wybierz menu: ")
    
    if Decision == "1":
        print("Gracz: " + PlayerName)
        print("Punkty zycia: " + str(HealthPoints))
        print("Zloto: " + str(Gold))
        
    elif Decision == "2":
        Location = random.randint(1, 3)
        LostHealthPoints = random.randint(1, 30)
        FoundGold = random.randint(5, 10)
        
        if Location == 1:
            print("W czelusciach jaskini otulil Ciebie chlod i znienacka zaatakowal ciebie stwor. Zabijasz go ale tracisz " + str(LostHealthPoints) + " HP.")
        elif Location == 2:
            print("Jasnosc przeswityla z wysokich koron drzew. Stales tak wpatrzony w piekno lasu gdy nagle zostales zaatakowany. W walce straciles " + str(LostHealthPoints) + " HP.")
        elif Location == 3:
            print("Przemierasz ruiny starego miasta. Znuzony brakiem walki kopiesz ze wsciekloscia pobliski kamien. Rozlega sie halas, ktory przebudzil stwora. Ubylo Tobie " + str(LostHealthPoints) + " HP.")
            
        HealthPoints = HealthPoints - LostHealthPoints
        MonstersKilled = MonstersKilled + 1
        Gold = Gold + FoundGold
        print("Zdobywasz " + str(FoundGold) + " sztuk zlota!")
        
    elif Decision == "3":
        print("Wchodzisz do chaty Druida")
        if Gold < 20 and HealthPoints < MaxHealthPoints:
            print("- Wedrowcze, przyniesc mi 20 sztuk zlota, a ulecze Ciebie z ran wojennych.")
        elif HealthPoints == MaxHealthPoints:
            print("- Jestes zdrow, czemuz to przeszkadasz mi w mej pracy?")
        else:
            print("- Usiac przy zarze mego skromnego ogniska, a zostaniesz uleczony.")
            print("Odzyskales 20 HP.")
            
            Gold = Gold - 20
            HealthPoints = HealthPoints + 20
            if HealthPoints > MaxHealthPoints:
                HealthPoints = MaxHealthPoints
            
    elif Decision == "0":
        GameRunning = False
        
    if HealthPoints <= 0:
        if Gold >= 20:
            print("Szczescie Tobie sprzyja, zostajesz odnalaziony przez Druida, ktory udziela Tobie pomocy w zamian zabiera Twoje zloto!")
            HealthPoints = HealthPoints + 20
            Gold = Gold - 20
            
        else:
            print("Godnie polegles w walce...")
            print("Zabite potwory: " + str(MonstersKilled))
            GameRunning = False
            
GoodBye()
        


