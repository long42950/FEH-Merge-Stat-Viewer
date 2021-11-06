from enum import Enum
import merge_sort

class Stat(Enum):
    HP = "HP"
    ATK = "ATK"
    SPD = "SPD"
    DEF = "DEF"
    RES = "RES"
    NEU = "NEU"
    
stats = [{"name": Stat.HP.value,
          "value" : 0},
         {"name": Stat.ATK.value,
          "value" : 0},
         {"name": Stat.SPD.value,
          "value" : 0},
         {"name": Stat.DEF.value,
          "value" : 0},
         {"name": Stat.RES.value,
          "value" : 0}]

base_stats = [{"name": Stat.HP.value,
              "value" : 0},
             {"name": Stat.ATK.value,
              "value" : 0},
             {"name": Stat.SPD.value,
              "value" : 0},
             {"name": Stat.DEF.value,
              "value" : 0},
             {"name": Stat.RES.value,
              "value" : 0}]
neutral = True
high3 = []

flaw = Stat.NEU

# Get base stat from user until 5 stats are available
def get_base_stat():
    global base_stats
    input_stats = []
    index = 0
    while len(input_stats) != 5:
        input_stats = [int(x) for x in input("Enter base stats(HP ATK SPD DEF RES): \n").split()]
        if len(input_stats) != 5:
            print("missing one or more stats")
    for stat in input_stats:
        base_stats[index]["value"] = stat
        index += 1
    sortedList = merge_sort.merge_sort_main(base_stats, "value")
    print(sortedList)
        
# Get stat from user until 5 stats are available
def get_stat():
    global stats
    input_stats = []
    index = 0
    while len(input_stats) != 5:
        input_stats = [int(x) for x in input("Enter stats(HP ATK SPD DEF RES): \n").split()]
        if len(input_stats) != 5:
            print("missing one or more stats")
    for stat in input_stats:
        stats[index]["value"] = stat
        index += 1
        
# Get stat variation if available
#   Return: True will continue, False will repeat this function
def get_asset_flaw():
    global var
    rtn = input("Enter Flaw stat(HP/ATK/SPD/DEF/RES) or n if neutral: ")
    match rtn:
        case "n":
            return True
        case "HP":
            flaw = Flaw.HP
            return True
        case "ATK":
            flaw = Flaw.ATK
            return True
        case "SPD":
            flaw = Flaw.SPD
            return True
        case "DEF":
            flaw = Flaw.DEF
            return True
        case "RES":
            flaw = Flaw.RES
            return True
        case _:
            print("Invalid input!")
            return False

# Starts calculating merges
def merge():
    pass


get_base_stat()
print(base_stats)
