import io

import os,sys
current_directory = sys.path[0]

import logging
LOG_FILENAME = current_directory + '/error_log.txt'
logging.basicConfig(filename=LOG_FILENAME, level=logging.DEBUG)

from org.sikuli.basics import *
from org.sikuli.script import *
import time

class SingletonClass(object):
    instance = None
    def __init__(self):
        type(self).set_instance(self)
        
    @classmethod
    def get_instance(cls):
        return cls.instance
    @classmethod
    def set_instance(cls, inst):
        cls.instance = inst


      
class SikuliInterface(SingletonClass):    
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
        super(SikuliInterface, self).__init__()
        
class KeyInterface(SingletonClass):    
    def __init__(self, key_class, key_modifier_class):
        self.Key = key_class
        self.KeyModifier = key_modifier_class
        super(KeyInterface, self).__init__()
            
def get_all_matches(search_image):
    instance = SikuliInterface.get_instance()
    if(instance.exists(search_image)):
        return instance.findAll(search_image)
    return []
get_all = get_all_matches

def click_all(image):
    instance = SikuliInterface.get_instance()

    times_clicked = 0            
    for match in get_all_matches(image):
        instance.click(match)
        times_clicked +=1
        time.sleep(1)
        
    return times_clicked


def click_best_match(image,timeout = 0):
    instance = SikuliInterface.get_instance()
    
    try:
        if(instance.exists(image,timeout)):
            instance.click(image)
            return True
    except:
        pass
    return False

### BROWSER TAB FUNCTIONS
def switch_tab_right():
    ki = KeyInterface.get_instance()
    SikuliInterface.get_instance().type(ki.Key.TAB, ki.KeyModifier.CTRL)
    
def switch_tab_left():
    ki = KeyInterface.get_instance()
    SikuliInterface.get_instance().type(ki.Key.TAB, ki.KeyModifier.CTRL + ki.KeyModifier.SHIFT)
    return 
def switch_browser_tabs(distance):
    for i in xrange(distance):
        switch_tab_right()
    for i in xrange(distance,0):
        switch_tab_left()
        
def close_current_tab():
    ki = KeyInterface.get_instance()
    SikuliInterface.instance.type("W", ki.KeyModifier.CTRL)

        


### /BROWSER TAB FUNCTIONS



###Miscellaneous
def write_to_file(filename,options,content):
    fi = open(current_directory + "\\" + filename,options)
    fi.write(str(content) + "\n")
    fi.close()







class SikuliRegionInterface(SingletonClass):
    def __init__(self):
        self.region = SCREEN        
        super(SikuliRegionInterface,self).__init__()

    def get_all_matches(self,search_image):
        region = self.region
        if(region.exists(search_image)):
            return region.findAll(search_image)
        return []

    def click_all(self,image,wait_between = 0):
        region = self.region

        times_clicked = 0            
        for match in self.get_all_matches(image):
            region.click(match)
            times_clicked +=1
            time.sleep(wait_between)
            
        return times_clicked

    def click_best_match(self,image,timeout = 0):
        region = self.region
        
        try:
            if(region.exists(image,timeout)):
                region.click(image)
                return True
        except:
            pass
        return False

    
    def switch_tab_right():
        ki = KeyInterface.get_instance()
        SikuliInterface.get_instance().type(ki.Key.TAB, ki.KeyModifier.CTRL)
        
    def switch_tab_left():
        ki = KeyInterface.get_instance()
        SikuliInterface.get_instance().type(ki.Key.TAB, ki.KeyModifier.CTRL + ki.KeyModifier.SHIFT)
        return 
    def switch_browser_tabs(distance):
        for i in xrange(distance):
            switch_tab_right()
        for i in xrange(distance,0):
            switch_tab_left()
            
    def close_current_tab():
        ki = KeyInterface.get_instance()
        SikuliInterface.instance.type("W", ki.KeyModifier.CTRL)


def SRI():
    return SikuliRegionInterface.get_instance()


def png_manifest():
    class filler_object(object):
        def __init__(self):
            try:
                Debug.log(current_directory + "\\png_manifest")
                with io.open(current_directory + "\\png_manifest","r",encoding="UTF-16") as pngs:
                    for line in pngs:
                        arr = line.split(" ")
                        if(len(arr) < 2):
                            continue
                        constant = arr[0]
                        path = arr[1]
                        Debug.log(constant + " " + path)
                        setattr(self,constant,path)
                
            except Exception as e:
                logging.error(e, exc_info=True)
                Debug.log("FAILED TO POPULATE")
    
    return filler_object() 

