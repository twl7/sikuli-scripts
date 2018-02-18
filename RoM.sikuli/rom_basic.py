import os,sys
parent = os.path.dirname(sys.path[0])
if(not parent in sys.path): sys.path.append(parent)

from org.sikuli.basics import Debug
from org.sikuli.script import *
from sikuli_tools import *
from time import *
import datetime


sri = SRI()
png = png_manifest()

def make_fzone_trades(number_of_tabs,trade_array):
    total = 0
    while(True):
        for i in xrange(number_of_tabs):
            for trade in trade_array:
                total += sri.click_all(trade)
            sleep(1)
            sri.switch_tab_right()
            sleep(1)
        for i in xrange(number_of_tabs):
            sri.switch_tab_left()
            sleep(1)
        
        sleep(1000) #Modify to hour if needed. Number is in seconds


def run_bosses(number_of_tabs,number_of_fights):
    hover_location = sri.region.find(png.CONTAINER_SERVER).getCenter().offset(0,-80)
    if(number_of_tabs <= 0):
        return
    b_r_b = png.BOSS_READY_BUTTON
    b_g_b = png.BOSS_GO_BUTTON
    current_time = lambda : datetime.datetime.now()
    for iteration in xrange(number_of_fights):
        for tab in xrange(number_of_tabs - 1):
            sri.click_best_match(b_r_b)
            sri.switch_tab_left()
            sleep(1)
        sri.region.exists(b_g_b,5)
        sri.click_best_match(b_g_b)
        
        for tab in xrange(number_of_tabs):
            reshuffle = Pattern(png.BATTLE_RESHUFFLE_PROMPT).targetOffset(60,30)
                
            if(sri.region.exists(reshuffle,10-8*tab)):
                sri.click_best_match(reshuffle) 
                sri.region.hover(hover_location)
                sri.region.waitVanish(reshuffle,1)     
            sri.click_best_match(png.BATTLE_AUTO_BUTTON,2)
            
            sri.switch_tab_right()
        sri.switch_tab_left()
        sri.region.hover(hover_location)
        
        timing = current_time()
        
        sri.region.exists(b_r_b,1000)
        write_to_file("boss times.txt","a",(current_time()-timing).total_seconds())

        
def complete_maps():
    pass

def collect_all_quests():
    pass

