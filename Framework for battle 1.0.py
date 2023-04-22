import random
import time
#点数生成的时候需要用
#可能有用的代码 debug
terrainlist=["mountain","lake","City","Swamp","Desert","Plain"]
Truepoint=0
bonus=0
class Untitled_army_group():
    #这是初步的构想，如下:
    #size是规模，单排是1，小规模是2，标准规模是3，大规模是4
    #当size小于0的时候，将会出现待补员的状态
    #depth是单排深度，战斗中如果遭到击穿则会减少规模
    #步兵是4或5，骑兵是3，装甲部队5+
    #length指的是进攻长度，是掷骰子的数量，越有战术的部队掷骰子的数量就越多
    #标准状态下一个部队进攻由2个骰子判定，防御由1个骰子判定
    #effect包括制海权，制空权，地形，天气*但是这个版本里，影响因素只有地形
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

        #self.terrain = input("select the terrain, it is in :")
        new_idx = int(input("\nselect the terrain index:"))

        if new_idx >len(terrainlist) or new_idx<=0:
            print(f"[Warning]:Your input {new_idx} is not in the index range, default index 3.{terrainlist[2]} will be used!")
            new_idx = 2
        else:            
            new_idx = new_idx - 1
        
        self.terrain = terrainlist[new_idx]        

        #print("Troop A information:\n"+"size:"+str(self.size)+" depth:"+str(self.depth)+" length:"+str(self.length)+" terrain:"+self.terrain)
        #optimized print with fstring
        print(f"Troop A information:\nsize: {self.size} depth:{self.depth} length: {self.length} terrain:{self.terrain}")
#强攻
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
    #战斗地形判定
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
#计算结果
def result():
    global Truepoint
    #进攻结果判定
    print(f"With bonus, defbuff, the true damage brought to your enemy is {Truepoint}")
    if Truepoint > 0:
        if Troop_B.depth <= Truepoint:
            Troop_B.size = Troop_B.size - 1
            print("\nYour attack exceeds TroopB's depth, Troop B lost one size")
            print("current size for Troop B:"+str(Troop_B.size))
        if Troop_B.depth >= Truepoint:
            print("\nNo size decline")
    if Truepoint < 0:
        if Troop_A.depth <= Truepoint:
            Troop_A.size = Troop_A.size - 1
            print("\nYour army size - 1")
            print("current size for your troop:"+str(Troop_A.size))
        if Troop_A.depth >= Truepoint:
            print("\nNo size decline")
    print("your size : " + str(Troop_A.size))
    if Troop_B.size <= 0:
        print("Troop_B is in need for supplement! Troop A wins!")
    if Troop_A.size <= 0:
        print("Your troop is in need for supplement! You lose!")
#普通进攻
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
#开补给
def supply():
    global bonus
    bonus+=random.randint(3,6)
    print(f"current bonus: {bonus}")
#主程序
#部队信息初始化
Troop_A = Untitled_army_group()
Troop_B = Untitled_army_group()
print("edit troop A:")
Troop_A.edit_troop()
print("\n\n\n")
print("edit troop B:")
Troop_B.edit_troop()
#战斗环节
while Troop_B.size>0:
    time.sleep(0.7)
    print("\n\n")
    print("You are now playing as troop A")
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
#条款部分请见Liscense部分