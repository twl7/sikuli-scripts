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


### Guild
def summon_guild_raids():
    d_t = 5
    for pic in [png.mainscreen_tab_guild, png.guild_war_room]:
        sri.click(pic,5)
    scroll_down = Pattern(png.guild_war_room_scroll_bottom).similar(0.99)
    summon = Pattern(png.guild_war_room_summon).similar(0.90)
    hov = sri.find(png.mainscreen_tab_guild_selected,d_t)
    for i in xrange(50):
        sri.click_all(summon)
        sri.click_all(scroll_down)
        time.sleep(0.5)
        sri.hover(hov)
    for pic in [png.guild_war_room_join_all,png.popup_choice_yes]:
        sri.click(pic, d_t)
    sri.click(png.mainscreen_tab_home)
        
def collect_guild_campaigns():
    default_time = d_t = 10
    completed = Pattern(png.guild_campaign_menu_tab_completed).similar(0.98)
    gtabselect = png.mainscreen_tab_guild_selected
    
    for pic in [png.mainscreen_tab_guild, png.guild_campaign, completed]:
        sri.click(pic, timeout = d_t )

    
    while(sri.exists(png.guild_campaign_menu_join,d_t)):

        ##collect
        ##count = 0
        ##for jo in sri.find_all(png.guild_campaign_menu_join):
        ##  count += 1
        time.sleep(1)
        sri.click_top(png.guild_campaign_menu_join)
        sri.click(png.guild_campaign_map_close_result,default_time)
        
        while(sri.exists(png.guild_campaign_map_node_collect, d_t)):
            for pic in [png.guild_campaign_map_node_collect, \
                        png.guild_campaign_map_node_loot] + [gtabselect]*4:
                sri.click(pic, d_t)
        for pic in [png.guild_campaign_map_close, png.guild_campaign, completed]:
            sri.click(pic,d_t)
        time.sleep(1)

        #loot
        #for i in xrange(count):
        for pic in [png.guild_campaign_menu_loot] + [gtabselect]*4:
            sri.click(pic,d_t)
        #end while menu join
    sri.click(png.mainscreen_tab_home)
    return True
    

###

def load_raid_information():
    pass
"""
called within raid attack screen
"""
def attack_and_exit_raid(share = True):
    pass

#call anywhere
def summon_and_hit_raids(num_to_summon, share):
    d_t = 10
    for pic in [png.mainscreen_tab_raid, png.raid_tab_summon, \
                png.raid_menu_available_summon]:
        sri.click(pic,d_t)
    for i in num_to_summon:
        pass

def hit_new_raids(damage_index):
    d_t = 5
    for pic in [png.mainscreen_tab_raid, png.raid_tab_new]:
        sri.click(pic,d_t)
    while(sri.exists(png.raid_menu_engage,d_t)):
        join_and_hit_raid(damage_index)

    sri.click(png.mainscreen_tab_home)

def join_raid():
    d_t = 5
    def check_popup():
        return sri.click(png.popup_ok_confirm, timeout = 1))
    
    for pic in [png.raid_menu_join, png.raid_menu_engage]:
        sri.click(pic, timeout = d_t)
        if(check_popup()):
            return False
    
    return True

def join_and_hit_raid(damage_index = 0,share = False):
    d_t = 5
    if(not join_raid()):
        return
    damage = [png.raid_battlescreen_s_1,png.raid_battlescreen_s_5,
              png.raid_battlescreen_s_20,png.raid_battlescreen_s_20x5]
    sri.click(damage[damage_index],d_t)
    if(sri.click(png.popup_ok_confirm,2)):
        return

    sri.click(png.raid_battlescreen_close)

def hit_raid_for_tier(tier = 1):
    pass


### stuff

def dismiss_logoff():
    sri.click(png.popup_logoff_dismiss,4)
    sri.click(png.popup_choice_yes)

