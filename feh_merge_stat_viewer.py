import sys
sys.path.append('C:/Users/long4/Desktop/software/Python 3.10/scripts/Merge Sort (Python)')
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
sortedStats = []

flaw = {"name": Stat.NEU.value, "variant": 0}

# Get base stat from user until 5 stats are available
def get_base_stat():
    global base_stats, sortedStats
    input_stats = []
    stats_for_sort = []
    index = 0
    while len(input_stats) != 5:
        input_stats = [int(x) for x in input("Enter base stats(HP ATK SPD DEF RES): \n").split()]
        if len(input_stats) != 5:
            print("ERROR: missing one or more stats!")
    for stat in input_stats:
        base_stats[index]["value"] = stat
        stats_for_sort.append(base_stats[index])
        index += 1
    sortedStats = merge_sort.merge_sort_main(stats_for_sort, "value")
        
# Get stat from user until 5 stats are available
def get_stat():
    global stats
    input_stats = []
    index = 0
    while len(input_stats) != 5:
        input_stats = [int(x) for x in input("Enter stats(HP ATK SPD DEF RES): \n").split()]
        if len(input_stats) != 5:
            print("ERROR: missing one or more stats!")
    for stat in input_stats:
        stats[index]["value"] = stat
        index += 1
        
# Get stat variation if available
#   Return: True will continue, False will repeat this function
def get_asset_flaw():
    global flaw
    while True:
        rtn = input("Enter Flaw stat(HP/ATK/SPD/DEF/RES) or n if neutral: ")
        rtn = rtn.upper()
        match rtn:
            case "N":
                return True
            case _:
                for name in Stat:
                    if rtn == name.value:
                        flaw["name"] = rtn
                        while flaw["variant"] == 0:
                            var = input("Enter Flaw stat variant with neutral: ")
                            var = int(var)
                            if var == 3 or var == 4:
                                flaw["variant"] = var
                            else:
                                print("ERROR: Invalid stat variant! \n")
                        return False
                print("ERROR: Invalid stat name! \n")

# Starts calculating merges
def merges():
    global stats, neutral, flaw, sortedStats
    for merge in range(10):
        for index in range(5):
            break

# Increase stat value          
def stat_increase(currentMerge):
    global stats, neutral, flaw, sortedStats
    stat1Name = sortedStats[currentMerge]["name"]
    stat2Name = sortedStats[currentMerge+1]["name"]
    stat3Name = sortedStats[currentMerge+2]["name"]
    nFound = 0
    for index in range(5):
        found = False
        if stats[index]["name"] == stat1Name or stats[index]["name"] == stat2Name:
            stats[index]["value"] = stats[index]["value"] + 1
            found = True
        if neutral and (found or stats[index]["name"] == stat3Name):
            stats[index]["value"] = stats[index]["value"] + 1
            found = True
        if found:
            nFound = nFound + 1
        if (neutral and nFound == 3) or (not neutral and nFound == 2):
            break
        
def get_info():
    print("")
    print("name | HP | ATK | SPD | DEF | RES |")
    print("-----------------------------------")
    output = "base | "
    for stat in base_stats:
        var = stat["value"]
        output = output + str(var)
        if stat["name"] == "HP":
            output = output + " | "
        elif var < 10:
            output = output + "   | "
        else:
            output = output + "  | "
    print(output)
    output = "lv40 | "
    for stat in stats:
        var = stat["value"]
        output = output + str(var)
        if stat["name"] == "HP":
            output = output + " | "
        elif var < 10:
            output = output + "   | "
        else:
            output = output + "  | "
    print(output)
    print("--------------------------------- \n")
    print("Stats sorted in value: ")
    print("Stat | BS | MAX")
    print("---------------")
    for stat in sortedStats:
        name = stat["name"]
        var = stat["value"]
        for index in range(5):
            if name == stats[index]["name"]:
                var2 = stats[index]["value"]
                break
        if name == "HP":
            print(f"{name}   | {var} | {var2} ")
        elif var < 10:
            print(f"{name}  | {var}  | {var2} ")
        else:
            print(f"{name}  | {var} | {var2} ")
    print("---------------")
    print(f"Neutral: {neutral}")
    if not neutral:
        name = flaw["name"]
        variant = flaw["variant"]
        print(f"Flaw Stat: {name} | Variant: -{variant}")

def main():
    global neutral
    name = ""
    var = 0
    var2 = 0
    get_base_stat()
    get_stat()
    neutral = get_asset_flaw()
    
    
main()
get_info()
