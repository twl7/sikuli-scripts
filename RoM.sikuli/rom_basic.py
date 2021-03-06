import os,sys
parent_directory = os.path.dirname(sys.path[0])

if(not parent_directory in sys.path): sys.path.append(parent_directory)

from org.sikuli.basics import Debug
from org.sikuli.script import *
from sikuli_tools import *

import time
import datetime


sri = SRI()
png = png_manifest(sys.path[0])
hover_location = sri.find(png.CONTAINER_ROM_TITLE).getCenter().offset(0,80)


def return_to_main_screen():
    for button in []:
        sri.click_best_match(button)
        pass
    pass

def auto_battle(wait_time = 10):
    
    reshuffle = Pattern(png.BATTLE_RESHUFFLE_PROMPT).similar(0.5).targetOffset(60,30)
    auto_button = png.BATTLE_AUTO_BUTTON

    sri.exists(reshuffle,max(0,wait_time))
    start = time.time()
    while((time.time() - start) < 0.5 and not sri.click(reshuffle)):
        pass
    sri.hover(hover_location)
    start = time.time()
    while((time.time() - start) < 0.5 and not sri.click(auto_button)):
        pass
        
    """
    if(sri.exists(reshuffle,max(0,wait_time))):
        sri.click(reshuffle) 
        sri.hover(hover_location)
        sri.region.waitVanish(reshuffle,0.5)
    sri.click(png.BATTLE_AUTO_BUTTON,0.5)
    """

def make_fzone_trades(number_of_tabs,trade_array, num_trade_cycles = -1, wait_time = 3600,separate_trades = False):
    exchange = Pattern(png.fzone_exchange).similar(0.99)
    totals = [0] * number_of_tabs
    cycles = 0
    while(cycles != num_trade_cycles):
        for i in xrange(number_of_tabs):
            trades = trade_array
            if(separate_trades):
                trades = trade_array[i % len(trade_array)]
            trades = [Pattern(trade).similar(0.95) for trade in trades]
            
            if(num_trade_cycles != 1):
                for p in [Pattern(png.menu_close_button).similar(.80),png.mainscreen_icon_forbidden_zone]:
                    
                    sri.click(p,1)
                    time.sleep(0.6)
            regions = []
            to_click = True
            for trade in trades:
                if(sri.exists(trade)):
                    if(to_click):
                        sri.click(sri.getLastMatch())
                        to_click = False
                    Debug.log(str(trade))
                    regions += sri.find_all(trade)
            for r in regions:
                totals[i] += sri.click(exchange,1,r.below(100))
                
            time.sleep(0.5)
            sri.switch_tab_right()
            time.sleep(0.5)
        for i in xrange(number_of_tabs):
            sri.switch_tab_left()
            time.sleep(0.2)
        Debug.log("Number of trades so far is {}".format(str(totals)))
        cycles += 1
        time.sleep(wait_time)
        
#TODO make the boss functions less redundant
        
def tab_bosses(run_time):
    global hover_location
    current_time = lambda : datetime.datetime.now()
    b_r_b = png.BOSS_READY_BUTTON
    b_g_b = png.BOSS_GO_BUTTON
    victory = png.BATTLE_VICTORY
    reshuffle = Pattern(png.BATTLE_RESHUFFLE_PROMPT).similar(0.5).targetOffset(60,30)

    
    #sri.onAppear(victory,lambda : sri.click(victory))
    #sri.observe()
    
    timing = current_time()
    while((current_time() - timing).total_seconds() < run_time):
        if(sri.click(victory,1)):
            time.sleep(1)
        if(sri.click(b_r_b)):
            pass
        elif(sri.click(b_g_b)):
            pass
        else:
            auto_battle(0)

        sri.switch_tab_right()
    
        
#
def run_bosses(number_of_tabs,number_of_fights):
    global hover_location
    if(number_of_tabs <= 0):
        return
    
    b_r_b = png.BOSS_READY_BUTTON
    b_g_b = png.BOSS_GO_BUTTON
    victory = png.BATTLE_VICTORY
    
    boss_button = b_g_b if number_of_tabs == 1 else b_r_b
    
    current_time = lambda : datetime.datetime.now()
    for iteration in xrange(number_of_fights):
        for tab in xrange(number_of_tabs - 1):
            sri.click(victory,1)
            sri.click_best_match(b_r_b,3)
            sri.switch_tab_left()
            
        sri.click(victory,1)
        sri.click(b_g_b,10)
        
        for tab in xrange(number_of_tabs):
            auto_battle(10-8*tab)
            
            sri.switch_tab_right()
            
        sri.switch_tab_left()
        sri.hover(hover_location)
        
        timing = current_time()

        #sri.click(png.battle_surrender_button,3)
        #sri.click(png.battle_confirm,3)
        sri.exists_array([victory,boss_button],1000)
        write_to_file("boss times.txt","a",(current_time()-timing).total_seconds())


def run_world_boss(number_of_tabs,number_of_fights):
    global hover_location
    if(number_of_tabs <= 0):
        return
    b_r_b = png.BOSS_READY_BUTTON
    b_g_b = png.BOSS_GO_BUTTON
    boss_button = b_g_b
    
    for tab in xrange(number_of_tabs - 1):
            sri.click_best_match(b_r_b)
            sri.switch_tab_left()
            time.sleep(1)
            
    for iteration in xrange(number_of_fights):
                        
        sri.exists(b_g_b,5)
        sri.click(b_g_b)
        
        for tab in xrange(number_of_tabs):
            auto_battle(10-8*tab)
            
            sri.switch_tab_right()
        sri.switch_browser_tabs(-1*number_of_tabs)
        sri.hover(hover_location)
        sri.exists(boss_button,1000)
        
def auto_towers(win_limit):
    victory = png.battle_victory
    c_b = png.tower_continue_button
    s_b = png.tower_start_button
    free_attempt = Pattern(png.tower_free_attempt).similar(0.90)
    
    current_wins = 0
    
    while(current_wins < win_limit):
        current_wins += sri.click(victory)
        
        if(sri.exists(free_attempt)):
            sri.click(s_b)
        sri.click(c_b)
        
        auto_battle(2)
        sri.switch_tab_right()
        time.sleep(1)
        
def complete_maps():
    pass

def collect_all_quests():
    pass

