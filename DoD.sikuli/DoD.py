import os,sys
parent = os.path.dirname(sys.path[0])
if(not parent in sys.path): sys.path.append(parent)

import dod_basic

import sikuli_tools
reload(sikuli_tools)
from sikuli_tools import *

SikuliInterface(
    find = find,findAll = findAll,wait = wait, waitVanish = waitVanish, exists = exists, 
    click = click, doubleClick = doubleClick,rightClick = rightClick, hover = hover,
    dragDrop = dragDrop, type = type, paste = paste
    )
KeyInterface(Key,KeyModifier)

### SETTINGS
Settings.MinSimilarity = 0.85
### /SETTINGS

