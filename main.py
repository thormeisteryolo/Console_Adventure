import monsterstat 
import random

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

locations = ("home", "town", "forest", "cave")
currentLocation = "home"
armorTypes = ("light", "medium", "heavy")
weaponTypes = ("mace", "sword", "greatsword")

monsterCount = len(monsterstat.monsters)


monsters = []
for x in monsterstat.monsters:
      monsters.append(x)

def locationChanger():
      x = True
      while x == True:
            location = input(f"Where does {playerName} want to go: ").lower()
            if location in locations:
                  x = False
                  return location
            else:
                  print("Not a valid location")

def startBattle():
      enemyCount = random.randint(1, monsterCount)
      enemies = list(())
      for x in range(1, enemyCount):
            enemies.append(monsters[random.randint(0, monsterCount - 1)])
    


      #print(enemies)
      #print(len(enemies))

playerData["name"] = input("What name does it go by: ")
playerName = playerData["name"]
y = True
while y == True:
    armor = input("What kind of armor does it wear: ").lower()
    if armor in armorTypes:
            playerData["armor"] = armor
            weapon = input("What is it's prefered weapon: ").lower()
            if weapon in weaponTypes:
                    playerData["weapon"] = weapon
                    y = False
            else:
                 print("Not a valid weapon")
    else:
        print("Not a valid armor type")

print(f"{playerName} wakes up in a cottage not to far from the local town.")
currentLocation = locationChanger()
if currentLocation == "forest":
      startBattle()
