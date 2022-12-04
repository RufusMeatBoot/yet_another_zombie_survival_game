import main as Main


class uiElements:
    doorElement = """|---------------|
| 1) Open door  |
| 2) Close door |
|---------------|"""

    mainMenuElement = """*----Title----*
|-------------|
| 1) New Game |
| 2) Quit     |
|-------------|"""

    pauseMenuElement = """|-----------|
| 1) Resume |
| 2) Quit   |
|-----------|"""

    checkItemElement = """|--------------------|
| 1) Check container |
| 2) Exit            |
|--------------------|"""

    pickItemElement = f"""|-------------------|
| 1) Pick up {Main.randomItem} |
| 2) Leave {Main.randomItem}   |
|-------------------|"""