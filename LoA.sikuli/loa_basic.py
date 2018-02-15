import os,sys
parent = os.path.dirname(sys.path[0])
if(not parent in sys.path): sys.path.append(parent)

from org.sikuli.basics import Debug
from org.sikuli.script import *
from sikuli_tools import *
from time import *

png = png_manifest()

def claim_friends_energy():
    click_best_match("d")
