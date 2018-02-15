import os,sys
parent = os.path.dirname(sys.path[0])
if(not parent in sys.path): sys.path.append(parent)

from org.sikuli.basics import Debug
from org.sikuli.script import *
import sikuli_tools
from time import *


def make_fzone_trades(number_of_tabs,trade_array):
    total = 0
    while(True):
        for i in xrange(number_of_tabs):
            for trade in trade_array:
                total += sikuli_tools.click_all(trade)
            sleep(1)
            sikuli_tools.switch_tab_right()
            sleep(1)
        for i in xrange(number_of_tabs):
            sikuli_tools.switch_tab_left()
            sleep(1)
            
        
        sleep(1000) #Modify to hour if needed. Number is in seconds


#TODO: Fix this
        '''
def run_bosses2(number_of_tabs,number_of_fights):
    if(number_of_tabs <= 0):
        return
    ST = sikuli_tools
    for iteration in xrange(number_of_fights):
        for tab in xrange(number_of_tabs - 1):
            ST.click_best_match("boss_ready_button.png")
            ST.switch_tab_left()
            sleep(1)
        ST.exists("boss_go_button.png",5)
        ST.click_best_match("boss_go_button.png")
        
        for tab in xrange(number_of_tabs):
            if(ST.exists(Pattern("battle_reshuffle_prompt.png").targetOffset(74,38),10)):
                ST.click_best_match(Pattern("battle_reshuffle_prompt.png").targetOffset(74,38))
            ST.click_best_match("battle_auto_button.png")
        
            ST.switch_tab_right()
        ST.switch_tab_left()
        
        ST.exists("boss_ready_button.png",1000)
'''
        
def complete_maps():
    pass

def collect_all_quests():
    pass

