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
        if(cls.instance == None):
            cls.set_instance(cls())
        return cls.instance
    @classmethod
    def set_instance(cls, instance):
        cls.instance = instance


class KeyInterface(SingletonClass):    
    def __init__(self, key_class = Key , key_modifier_class = KeyModifier):
        self.Key = key_class
        self.KeyModifier = key_modifier_class
        super(KeyInterface, self).__init__()

class SikuliRegionInterface(SingletonClass):
    def __init__(self,region = Screen()):
        self.region = region        
        super(SikuliRegionInterface,self).__init__()


    def set_region(self,region):
        self.region = region

    def reset_region(self):
        self.region = Screen()

    ## Interface

    def exists(self,pattern, timeout = 0):
        try:
            return self.region.exists(pattern,timeout)
        except:
            Debug.log("Failed to find pattern " + str(pattern))
        return False
        
    def click(self,pattern,timeout = 0):
        try:
            if(self.exists(patterm,timeout)):
                self.region.click(self.region.getLastMatch())
                return True
        except:
            pass
        return False

    def type(self,keys,key_modifiers):
        self.region.type(keys,key_modifiers)
        
    ## /Interface

        
    
    def get_all_matches(self,search_image, region = None):
        if(region == None):
            region = self.region
        
        if(region.exists(search_image)):
            return region.findAll(search_image)
        return []

    def click_all(self,image,wait_between = 0,region = None):
        if(region == None):
            region = self.region
        
        times_clicked = 0            
        for match in self.get_all_matches(image,region):
            region.click(match)
            times_clicked +=1
            time.sleep(wait_between)
            
        return times_clicked
    
    def find_best_match(self,image,timeout = 0, region = None):
        if(region == None):
            region = self.region
            
        match = None
        try:
            if(region.exists(image,timeout)):
                match = region.getLastMatch()
        except:
            pass
        
        return match
    
    def click_best_match(self,image,timeout = 0,region = None):
        if(region == None):
            region = self.region
            
        match = self.find_best_match(image,timeout,region)
        if(match is None):
            return False
        region.click(match)
        return True

    ### BROWSER INTERACTION
    def switch_tab_right(self):
        ki = KeyInterface.get_instance()
        self.type(ki.Key.TAB, ki.KeyModifier.CTRL)
        return
    
    def switch_tab_left(self):
        ki = KeyInterface.get_instance()
        self.type(ki.Key.TAB, ki.KeyModifier.CTRL + ki.KeyModifier.SHIFT)
        return
    
    def switch_browser_tabs(self,distance):
        for i in xrange(distance):
            self.switch_tab_right()
        for i in xrange(distance,0):
            self.switch_tab_left()
            
    def close_current_tab(self):
        ki = KeyInterface.get_instance()
        self.type("W", ki.KeyModifier.CTRL)


def SRI():
    return SikuliRegionInterface.get_instance()

###
def png_manifest(directory = current_directory):
    class png_object(object):
        def __init__(self,directory):
            try:
                file_path = directory + "/png_manifest"
                Debug.log("opening " + file_path)
                with io.open(file_path,"r",encoding="UTF-16") as pngs:
                    for line in pngs:
                        arr = line.split(" ")
                        if(len(arr) < 2):
                            continue
                        constant = arr[0].strip().upper()
                        path = arr[1].strip()
                        setattr(self,constant,path)
                        setattr(self,constant.lower(),path)
                
            except Exception as e:
                logging.error(e, exc_info=True)
                Debug.log("FAILURE: Could not populate png's")
    
    return png_object(directory) 

###Miscellaneous
def write_to_file(filename,options,content):
    fi = open(current_directory + "\\" + filename,options)
    fi.write(str(content) + "\n")
    fi.close()
