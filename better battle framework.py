import random
import time
terrainlist=["mountain","lake","City","Swamp","Desert","Plain"]
bonus=0
class Untitled_army_group():
    def __init__(self, size=2, depth=4, length=2, effect=0):
        self.size = size
        self.depth = depth
        self.length = length
        self.effect = effect
    def edit_troop(self):
        self.size = int(input("size of the troop:(1,2,3 or 4)    :"))
        self.depth = int(input("depth of the troop:(3,4,5,6)     :"))
        self.length = int(input("Length of the troop:(2,3,or 4)  :"))
        for idx, value in enumerate(terrainlist):
            print(f"{idx+1}. {value}", end= " ")
        new_idx = int(input("\nselect the terrain index:"))
        if new_idx >len(terrainlist) or new_idx<=0:
            print(f"[Warning]:Your input {new_idx} is not in the index range, default index 3.{terrainlist[2]} will be used!")
            new_idx = 2
        else:            
            new_idx = new_idx - 1
        self.terrain = terrainlist[new_idx]        
        print(f"\033[0;30;44mTroop A information:\nsize: {self.size} depth:{self.depth} length: {self.length} terrain:{self.terrain}\033[0m")

def heavy_assult():
    global bonus
    global Truepoint
    i=0
    attackpoint = 0
    defensepoint = 0
    for i in range(Troop_A.length+1):
        turn_point=0
        turn_point=random.randint(2,6)
        attackpoint=attackpoint+turn_point
        i+=1
        print("The" + str(i) + "strike: "+ str(turn_point))
        time.sleep(0.7)
    i=0
    for i in range(Troop_B.length):
        turn_point=0
        turn_point=random.randint(1,6)
        defensepoint=defensepoint+turn_point
    i=0
    if Troop_B.terrain in ["mountain","lake"]:
        attackpoint -= 3
    if Troop_B.terrain in ["city","desert"]:
        attackpoint += random.randint(-2,1)
    if Troop_B.terrain == "swamp":
        attackpoint += 1

    print("total damage brought to the enemy:"+str(attackpoint))
    print("total defense of the enemy:"+str(defensepoint))
    Truepoint=bonus+attackpoint-defensepoint-2
    bonus=0

def result():
    global Truepoint
    print(f"\033[31mWith bonus, defbuff, the true damage brought to your enemy is {Truepoint}\033[0m")
    if Truepoint > 0:
        if Troop_B.depth < Truepoint:
            Troop_B.size = Troop_B.size - 1
            print("\nYour attack exceeds TroopB's depth, Troop B lost one size")
            print("current size for Troop B:"+str(Troop_B.size))
        if Troop_B.depth >= Truepoint:
            print("\nNo size decline")
    if Truepoint < 0:
        if Troop_A.depth < 0-Truepoint:
            Troop_A.size = Troop_A.size - 1
            print("\nYour army size - 1")
            print("current size for your troop:"+str(Troop_A.size))
        if Troop_A.depth >= 0-Truepoint:
            print("\nNo size decline")
    print("your size : " + str(Troop_A.size))
    if Troop_B.size <= 0:
        print("Troop_B is in need for supplement! Troop A wins!")
    if Troop_A.size <= 0:
        print("Your troop is in need for supplement! You lose!")

def normal_assult():
    global Truepoint
    global bonus
    time.sleep(0.7)
    i=0
    attackpoint = 0
    defensepoint = 0
    Truepoint = 0
    for i in range(Troop_A.length):
        turn_point=0
        turn_point=random.randint(1,6)
        attackpoint=attackpoint+turn_point
        i+=1
        print("The" + str(i) + "strike: "+ str(turn_point))
        time.sleep(0.7)
    i=0
    for i in range(Troop_B.length-1):
        turn_point=0
        turn_point=random.randint(1,6)
        defensepoint=defensepoint+turn_point
    i=0
    #战斗地形判定
    if Troop_B.terrain == ["mountain","lake"]:
        attackpoint -= 2
    if Troop_B.terrain == ["city","desert"]:
        attackpoint += random.randint(-2,2)
    if Troop_B.terrain == "swamp":
        attackpoint +=2

    print("total damage brought to the enemy:"+str(attackpoint))
    print("total defense of the enemy:"+str(defensepoint))
    Truepoint=bonus+attackpoint-defensepoint
    bonus=0

def supply():
    global bonus
    bonus+=random.randint(3,6)
    print(f"current bonus: {bonus}")
r=0
Troop_A = Untitled_army_group()
Troop_B = Untitled_army_group()
print("edit troop A:")
Troop_A.edit_troop()
print("\n\n\n")
print("edit troop B:")
Troop_B.edit_troop()

while Troop_B.size>0 and Troop_A.size>0:
    time.sleep(0.7)
    print("\n\n")
    print("You are now playing as troop A")
    r+=1
    choice = input("Now,it's your turn    A:attack    B.full attack   C.supply")
    if choice=="A":
        normal_assult()
        result()
    if choice=="B":
        heavy_assult()
        result()
    if choice=="C":
        supply()
    else:
        continue
time.sleep(1)
print("Victory")
print(f"It takes you {r} turns to defeat your enemy")