
# import files and modules
import game_map as Map
import player   as Player
import lower    as Tiles
import render   as Render
import ui       as UI
import items    as Items
import objects  as Obj
import keyboard
import time
import random


randomItem = random.choice(Items.items)
inv = Player.player.inventory

# intial map render on game start
def initialize():
    Render.render()

    # main loop
    while True:
        movePlayer()
        time.sleep(0.08)


# check for items in a container
def itemCheck():

    # container check left
    if Map.gameMap[Player.player.pos - 1] == "%" and keyboard.is_pressed("e"):
        Render.clearScreen()
        print(UI.uiElements.checkItemElement)
        while keyboard.is_pressed("1") == False or keyboard.is_pressed("2") == False:
            if keyboard.is_pressed("1"):
                randomItem = random.choice(Items.items)
                Render.clearScreen()
                print(UI.uiElements.pickItemElement)
                time.sleep(0.1)
                while keyboard.is_pressed("1") == False or keyboard.is_pressed("2") == False:
                    if keyboard.is_pressed("1"):
                        Player.player.inventory.append(item)
                        initialize()
                    elif keyboard.is_pressed("2"):
                        initialize()
            elif keyboard.is_pressed("2"):
                initialize()

    # container check right
    elif Map.gameMap[Player.player.pos + 1] == "%" and keyboard.is_pressed("e"):
        Render.clearScreen()
        print(UI.uiElements.checkItemElement)
        while keyboard.is_pressed("1") == False or keyboard.is_pressed("2") == False:
            if keyboard.is_pressed("1"):
                item = random.choice(Items.items)
                Render.clearScreen()
                print(UI.uiElements.pickItemElement)
                while keyboard.is_pressed("1") == False or keyboard.is_pressed("2") == False:
                    if keyboard.is_pressed("1"):
                        Player.player.inventory.append(item)
                        initialize()
                    elif keyboard.is_pressed("2"):
                        initialize()
            elif keyboard.is_pressed("2"):
                initialize()

    # container check up
    elif Map.gameMap[Player.player.pos - 10] == "%" and keyboard.is_pressed("e"):
        Render.clearScreen()
        print(UI.uiElements.checkItemElement)
        while keyboard.is_pressed("1") == False or keyboard.is_pressed("2") == False:
            if keyboard.is_pressed("1"):
                item = random.choice(Items.items)
                Render.clearScreen()
                print(UI.uiElements.pickItemElement)
                while keyboard.is_pressed("1") == False or keyboard.is_pressed("2") == False:
                    if keyboard.is_pressed("1"):
                        Player.player.inventory.append(item)
                        initialize()
                    elif keyboard.is_pressed("2"):
                        initialize()
            elif keyboard.is_pressed("2"):
                initialize()

    # container check down
    elif Map.gameMap[Player.player.pos + 10] == "%" and keyboard.is_pressed("e"):
        Render.clearScreen()
        print(UI.uiElements.checkItemElement)
        while keyboard.is_pressed("1") == False or keyboard.is_pressed("2") == False:
            if keyboard.is_pressed("1"):
                item = random.choice(Items.items)
                Render.clearScreen()
                print(UI.uiElements.pickItemElement)
                while keyboard.is_pressed("1") == False or keyboard.is_pressed("2") == False:
                    if keyboard.is_pressed("1"):
                        Player.player.inventory.append(item)
                        initialize()
                    elif keyboard.is_pressed("2"):
                        initialize()
            elif keyboard.is_pressed("2"):
                initialize()
    else:
        pass


# check for doors
def doorCheck():

    # door check left
    if (Map.gameMap[Player.player.pos - 1] == "+" or Map.gameMap[Player.player.pos - 1] == "-") and keyboard.is_pressed("e"):
        print(UI.uiElements.doorElement)
        while keyboard.is_pressed("1") == False or keyboard.is_pressed("2") == False:
            if keyboard.is_pressed("1") and Map.gameMap[Player.player.pos - 1] == "+":
                Map.gameMap[Player.player.pos - 1]   = "-"
                Tiles.tileMap[Player.player.pos - 1] = "-"
                Render.render()
                return True
            elif keyboard.is_pressed("2") and Map.gameMap[Player.player.pos - 1] == "-":
                Map.gameMap[Player.player.pos - 1]   = "+"
                Tiles.tileMap[Player.player.pos - 1] = "+"
                Render.render()
                return True

    # door check right
    elif (Map.gameMap[Player.player.pos + 1] == "+" or Map.gameMap[Player.player.pos + 1] == "-") and keyboard.is_pressed("e"):
        print(UI.uiElements.doorElement)
        while keyboard.is_pressed("1") == False or keyboard.is_pressed("2") == False:
            if keyboard.is_pressed("1") and Map.gameMap[Player.player.pos + 1] == "+":
                Map.gameMap[Player.player.pos + 1]   = "-"
                Tiles.tileMap[Player.player.pos + 1] = "-"
                Render.render()
                return True
            elif keyboard.is_pressed("2") and Map.gameMap[Player.player.pos + 1] == "-":
                Map.gameMap[Player.player.pos + 1]   = "+"
                Tiles.tileMap[Player.player.pos + 1] = "+"
                Render.render()
                return True

    # door check up
    elif (Map.gameMap[Player.player.pos - 10] == "+" or Map.gameMap[Player.player.pos - 10] == "-") and keyboard.is_pressed("e"):
        print(UI.uiElements.doorElement)
        while keyboard.is_pressed("1") == False or keyboard.is_pressed("2") == False:
            if keyboard.is_pressed("1") and Map.gameMap[Player.player.pos - 10] == "+":
                Map.gameMap[Player.player.pos - 10]   = "-"
                Tiles.tileMap[Player.player.pos - 10] = "-"
                Render.render()
                return True
            elif keyboard.is_pressed("2") and Map.gameMap[Player.player.pos - 10] == "-":
                Map.gameMap[Player.player.pos - 10]   = "+"
                Tiles.tileMap[Player.player.pos - 10] = "+"
                Render.render()
                return True

    # door check down
    elif (Map.gameMap[Player.player.pos + 10] == "+" or Map.gameMap[Player.player.pos + 10] == "-") and keyboard.is_pressed("e"):
        print(UI.uiElements.doorElement)
        while keyboard.is_pressed("1") == False or keyboard.is_pressed("2") == False:
            if keyboard.is_pressed("1") and Map.gameMap[Player.player.pos + 10] == "+":
                Map.gameMap[Player.player.pos + 10]   = "-"
                Tiles.tileMap[Player.player.pos + 10] = "-"
                Render.render()
                return True
            elif keyboard.is_pressed("2") and Map.gameMap[Player.player.pos + 10] == "-":
                Map.gameMap[Player.player.pos + 10]   = "+"
                Tiles.tileMap[Player.player.pos + 10] = "+"
                Render.render()
                return True
    else:
        pass


# player move function
def movePlayer():
    doorCheck()
    itemCheck()

    # player move left
    if keyboard.is_pressed("a") and Map.gameMap[Player.player.pos - 1] not in Obj.walls:
        Player.player.pos                  = Player.player.pos - 1
        Map.gameMap[Player.player.pos + 1] = Tiles.tileMap[Player.player.pos + 1]
        Render.render()
    
    # player move right
    elif keyboard.is_pressed("d") and Map.gameMap[Player.player.pos + 1] not in Obj.walls:
        Player.player.pos                  = Player.player.pos + 1
        Map.gameMap[Player.player.pos - 1] = Tiles.tileMap[Player.player.pos - 1]
        Render.render()

    # player move down
    elif keyboard.is_pressed("s") and Map.gameMap[Player.player.pos + 10] not in Obj.walls:
        Player.player.pos                   = Player.player.pos + 10
        Map.gameMap[Player.player.pos - 10] = Tiles.tileMap[Player.player.pos - 10]
        Render.render()

    # player move up
    elif keyboard.is_pressed("w") and Map.gameMap[Player.player.pos - 10] not in Obj.walls:
        Player.player.pos                   = Player.player.pos - 10
        Map.gameMap[Player.player.pos + 10] = Tiles.tileMap[Player.player.pos + 10]
        Render.render()

    elif keyboard.is_pressed("i"):
        stack = 0
        for i in Player.player.inventory:
            if Player.player.inventory[stack] != Player.player.inventory[stack - 1]:
                print(''.join(str(Player.player.inventory[stack])), "(x" + str(Player.player.inventory.count(Player.player.inventory[stack])) + ")")
                stack = stack + 1
            else:
                pass

    # pause menu
    elif keyboard.is_pressed("esc"):
        Render.clearScreen()
        print(UI.uiElements.pauseMenuElement)
        while keyboard.is_pressed("1") == False or keyboard.is_pressed("2") == False:
            if keyboard.is_pressed("1"):
                initialize()
            elif keyboard.is_pressed("2"):
                exit()
    else:
        pass


# main menu function
def mainMenu():
    Render.clearScreen()
    print(UI.uiElements.mainMenuElement)
    while keyboard.is_pressed("1") == False or keyboard.is_pressed("2") == False:
            if keyboard.is_pressed("1"):
               initialize()
            elif keyboard.is_pressed("2"):
                exit()


if __name__ == "__main__":
    mainMenu()