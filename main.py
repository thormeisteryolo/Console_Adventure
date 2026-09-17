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
weaponInfo = {
      "mace": {
            "damage": 20,
            "type": "blunt",
            "crit": 3,
            "speed": "medium"
      },
      "sword": {
            "damage": 15,
            "type": "pierce",
            "crit": 4,
            "speed": "fast"
      },
      "greatsword": {
            "damage": 35,
            "type": "slash",
            "crit": 2,
            "speed": "slow"
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

monsters.sort()
def locationChanger():
      x = True
      while x == True:
            location = input(f"Where does {playerName} want to go: ").lower()
            if location in locations:
                  x = False
                  return location
            else:
                  print("Not a valid location")

def playerAttack():
     print("A")

def startBattle():

 enemyCount = random.randint(1, 3)

 enemies = []

 for x in range(2, enemyCount + 1):
    enemies.append(monsters[random.randint(0, monsterCount - 1)])

 enemies.sort()
 numberEnemies = {}
 for i in range(0, monsterCount):
  numberEnemies[monsters[i]] = enemies.count(f"{monsters[i]}")

 numbers = list(numberEnemies.values())

 match len(enemies):
      case 1:
           encounterText = f"A {enemies[0]}"
      case 2:
           if enemies[0] == enemies[1]:
                encounterText = f"Two {enemies[0]}"
           else:
            encounterText = f"A {enemies[0]} and {enemies[1]}"
      case 3:
           if 3 in numbers:
                encounterText = f"Three {enemies[numbers.index(3)]}s"
           elif 2 in numbers:
                encounterText = f"Two {enemies[numbers.index(2)]}s and one {enemies[numbers.index(1)]}"
           else:
                encounterText = f"A {enemies[0]}, {enemies[1]} and {enemies[2]}"
           

 print(f"{encounterText} appear infront of {playerData["name"]}")

 print("ATTACK|GUARD|HEAL")
 a = True
 while a == True:
  action = input(f"What will {playerData['name']} do: ")
 match action.lower:
  case "attack":
         playerAttack()
         a = False
  case "guard":
        print("Not done")
  case "heal":
        print("Not done")
  case _:
        print("NOT AN ACTION")


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
