import game_map as Map
import player as Player
import objects as Obj
import os

def clearScreen():
    os.system("cls")

def render():
    if Map.gameMap[Player.player.pos] not in Obj.last:
        Map.gameMap[Player.player.pos] = "@"
    else:
        Map.gameMap[Player.player.pos] = "@\n"
    clearScreen()
    render = ''.join(str(item) for item in Map.gameMap)
    print(render)
