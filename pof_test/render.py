import game_map as Map
import player as Player
import os

def clearScreen():
    os.system("cls")

def render():
    clearScreen()
    Map.gameMap[Player.player.pos] = "@"
    render = ''.join(str(item) for item in Map.gameMap)
    print(render)