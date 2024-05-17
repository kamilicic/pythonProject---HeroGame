WIDTH = 1280
HEIGHT = 640
FPS = 60
TILESIZE = 64

UI_BG_COLOR = 'white'
ITEM_BOX_SIZE = 64
UI_FONT_SIZE = 18
UI_FONT = 'font/joystix.ttf'

WORLD_MAP = [
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', 'p', ' ', ' ', 'x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'w', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'e', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'f'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', 'e', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'w', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
]

weapons_data = {
    'sword': {'damage': 15, 'graphics': 'game pictures/weapons/sword.png'},
    'axe': {'damage': 20, 'graphics': 'game pictures/weapons/axe.png'},
    'rapier': {'damage': 8, 'graphics': 'game pictures/weapons/rapier.png'},
    'hammer': {'damage': 30, 'graphics': 'game pictures/weapons/hammer.png'},
    'spear': {'damage': 22, 'graphics': 'game pictures/weapons/spear.png'}
}
enemy_data = {
    'tomato': {'damage': 15, 'graphics': 'game pictures/enemies/rajce.png'},
    'dog': {'damage': 20, 'graphics': 'game pictures/enemies/dog.png'},
    'ghost': {'damage': 8, 'graphics': 'game pictures/enemies/ghost.png'},
    'snake': {'damage': 30, 'graphics': 'game pictures/enemies/snake.png'},
    'turtle': {'damage': 22, 'graphics': 'game pictures/enemies/turtle.png'}
}