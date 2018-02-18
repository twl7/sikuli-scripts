import os,sys
parent = os.path.dirname(sys.path[0])
if(not parent in sys.path): sys.path.append(parent)

from org.sikuli.basics import Debug
from org.sikuli.script import *
from sikuli_tools import *
from time import *

sri = SRI()

png = png_manifest()
activity_orders = {png.explore_map:[],
                }
def complete_activity():
    def return_to_activity():
        return_to_main_screen()
        click_best_match(png.mainscreen_activity)
        for activity in activity_orders:
            

def clear_maze():
    pass
def claim_friends_energy():
    click_best_match("d")
