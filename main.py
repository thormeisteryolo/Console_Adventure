import monsterstat 


playerData = {
    "name" : None,
    "armor" : None,
    "weapon" : None,
    "health" : 100
}
armorInfo = {
    "light" : {
        "defense" : 50,
        "mobility" : 1.25
    },
    "medium" : {
        "defense" : 100,
        "mobility" : 1
    },
    "heavy" : {
        "defense" : 150,
        "mobility" : 0.75
    }
}


armorTypes = ("light", "medium", "heavy")
weaponTypes = ("mace", "sword", "greatsword")


playerData["name"] = input("What name does it go by: ")
y = True
while y == True:
    armor = input("What kind of armor does it wear: ")
    if armor in armorTypes:
            playerData["armor"] = armor
            weapon = input("What is it's prefered weapon: ")
            if weapon in weaponTypes:
                    playerData["weapon"] = weapon
                    y = False
            else:
                 print("Not a valid weapon")
    else:
        print("Not a valid armor type")

print(f"{playerData['name']} wakes up in a cottage not to far from the local town")
