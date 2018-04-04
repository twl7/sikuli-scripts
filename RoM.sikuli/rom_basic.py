import os,sys
parent_directory = os.path.dirname(sys.path[0])

if(not parent_directory in sys.path): sys.path.append(parent_directory)

from org.sikuli.basics import Debug
from org.sikuli.script import *
from sikuli_tools import *
from time import *
import datetime


sri = SRI()
png = png_manifest(sys.path[0])

def make_fzone_trades(number_of_tabs,trade_array, num_trades = -1, wait_time = 3600):
    exchange = Pattern(png.fzone_exchange).similar(0.99)
    trade_array = [Pattern(trade).similar(0.9) for trade in trade_array]
    totals = [0] * number_of_tabs
    count = 0
    while(count != num_trades):
        for i in xrange(number_of_tabs):
            if(num_trades != 1):
                for p in [Pattern(png.menu_close_button).similar(.95),png.mainscreen_fz_icon]:
                    
                    if(not sri.click_best_match(p)):
                        break
                    sleep(0.6)
            regions = sum([[m for m in sri.get_all_matches(trade)] for trade in trade_array if sri.exists(trade)],[])
            for r in regions:
                totals[i] += sri.click_best_match(exchange,1,r.below(100))
                
            sleep(0.5)
            sri.switch_tab_right()
            sleep(0.5)
        for i in xrange(number_of_tabs):
            sri.switch_tab_left()
            sleep(0.2)
        Debug.log("Number of trades so far is {}".format(str(totals)))
        count += 1
        sleep(wait_time)
        
        


def run_bosses(number_of_tabs,number_of_fights):
    
    if(number_of_tabs <= 0):
        return
    
    hover_location = sri.region.find(png.CONTAINER_SERVER).getCenter().offset(0,-80)
    b_r_b = png.BOSS_READY_BUTTON
    b_g_b = png.BOSS_GO_BUTTON
    reshuffle = Pattern(png.BATTLE_RESHUFFLE_PROMPT).similar(0.5).targetOffset(60,30)
    boss_button = b_g_b if number_of_tabs == 1 else b_r_b
    
    current_time = lambda : datetime.datetime.now()
    for iteration in xrange(number_of_fights):
        for tab in xrange(number_of_tabs - 1):
            sri.click_best_match(b_r_b,2)
            sri.switch_tab_left()
    
        sri.click_best_match(b_g_b,10)
        
        for tab in xrange(number_of_tabs):
            if(sri.region.exists(reshuffle,10-8*tab)):
                sri.click_best_match(reshuffle) 
                sri.region.hover(hover_location)
                sri.region.waitVanish(reshuffle,1)     
            sri.click_best_match(png.BATTLE_AUTO_BUTTON,2)
            
            sri.switch_tab_right()
        sri.switch_tab_left()
        sri.region.hover(hover_location)
        
        timing = current_time()
        
        sri.exists(boss_button,1000)
        write_to_file("boss times.txt","a",(current_time()-timing).total_seconds())


def run_world_boss(number_of_tabs,number_of_fights):
    hover_location = sri.region.find(png.CONTAINER_SERVER).getCenter().offset(0,-80)
    if(number_of_tabs <= 0):
        return
    b_r_b = png.BOSS_READY_BUTTON
    b_g_b = png.BOSS_GO_BUTTON
    boss_button = b_g_b
    
    for tab in xrange(number_of_tabs - 1):
            sri.click_best_match(b_r_b)
            sri.switch_tab_left()
            sleep(1)
            
    for iteration in xrange(number_of_fights):
                        
        sri.exists(b_g_b,5)
        sri.click_best_match(b_g_b)
        
        for tab in xrange(number_of_tabs):
            reshuffle = Pattern(png.BATTLE_RESHUFFLE_PROMPT).similar(0.5).targetOffset(60,30)
                
            if(sri.exists(reshuffle,max(0,10-8*tab))):
                sri.click_best_match(reshuffle) 
                sri.region.hover(hover_location)
                sri.region.waitVanish(reshuffle,1)     
            sri.click_best_match(png.BATTLE_AUTO_BUTTON,2)
            
            sri.switch_tab_right()
        sri.switch_browser_tabs(-1*number_of_tabs)
        sri.region.hover(hover_location)
        sri.exists(boss_button,1000)
       
def return_to_main_screen():
    for button in []:
        sri.click_best_match(button)
        pass
    pass
def complete_maps():
    pass

def collect_all_quests():
    pass

