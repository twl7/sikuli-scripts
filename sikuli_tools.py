import io
import os, sys
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
        
### LOGGING
def to_str(obj):
    if(isinstance(obj,Pattern)):
        return obj.getFilename()

    else:
        return str(obj)
    
class SikuliRegionInterface(SingletonClass):
    default_region = Screen()
    
    def __init__(self, region = Screen()):
        self.region = region

        #match memory carries the last match from searching a pattern.
        #This match may not be tied to self.region
        self.match_memory = dict()

        super(SikuliRegionInterface, self).__init__()
        
    def set_region(self, region):
        self.region = region

    def reset_region(self):
        self.region = SikuliRegionInterface.default_region
    
    ## Interface

    def exists(self, pattern, timeout = 0, region = None):
        if(isinstance(pattern, Location) or isinstance(pattern,Match)):
           return False
        
        if(region == None):
            region = self.region
        try:
            found = region.exists(pattern, timeout)
            if(found):
                self.match_memory[pattern] = region.getLastMatch()
            return found
        except:
            Debug.log("Exist: Failed to find pattern " + str(pattern))
        return False
    
    def exists_array(self, patterns, timeout = 0, region = None):
        if(region == None):
            region = self.region
        try:
            start = time.time()
            while(int(time.time() - start) <= timeout):
                for pattern in patterns:
                    found = region.exists(pattern, 0)
                    if(found):
                        return found

        except:
            Debug.log("Exists Array: Failed to find pattern " + str(pattern))
        return False
        
    def click(self, pattern, timeout = 0, region = None, last_match = False):
        if(region == None):
            region = self.region
            
        if(isinstance(pattern, Location) or isinstance(pattern,Match)):
           region.click(pattern)
           return True
           
        mm = self.match_memory 
        try:
            if(last_match and pattern in mm and mm[pattern].nearby(5).exists(pattern)):
                region.click(mm[pattern])
                return True
                
            if(self.exists(pattern, timeout, region)):
                region.click(pattern)
                return True
        except:
            pass
        Debug.log("Click: Could not click pattern \"{}\"".format(str(pattern)))
        return False

    def find(self, pattern, timeout = 0, region = None, last_match = False):
        if(region == None):
            region = self.region
            
        find_last_match = last_match and \
        pattern in self.match_memory and \
        self.exists(pattern, 0, self.match_memory[pattern])
        
        if(find_last_match or self.exists(pattern, timeout, region)):
            return self.match_memory[pattern]
        Debug.log("Find: Could not find pattern \"{}\"".format(str(pattern)))
        return None
        
    def wait(self, pattern, timeout = 0.5):
        if(isinstance(pattern, Location) or isinstance(pattern,Match)):
           return True
        
        try:
            self.region.wait(pattern, timeout)
            return True
        except:
            Debug.log("Wait: Pattern \"{}\" did not appear after {} seconds".format(str(pattern), str(timeout)))
            
            return False

    def wait_array(self, patterns, timeout = 0.5):

        try:
            start = time.time()
            while(time.time() - start <= timeout):
                for pattern in patterns:
                    if(self.wait(patterns)):
                        return True
            
        except:
            Debug.log("Wait array: Awaited patterns \"{}\" did not appear after {} seconds".format(str(pattern), str(timeout)))

        return False
        
        
    def waitVanish(self, pattern, timeout = 0):
        self.region.waitVanish(pattern, timeout)
        
    def type(self, keys, key_modifiers):
        self.region.type(keys, key_modifiers)

    def hover(self, location):
        self.region.hover(location)

      ##observers

    def onAppear(self, pattern, handler):
        self.region.onAppear(pattern, handler)
        return

    def observe(self, seconds, background = True):
        self.region.observe(seconds, background)

    def stopObserver(self):
        self.region.stopObserver()
       ## /observers
    
    ## /Interface

        
    def getLastMatch(self):
        return self.region.getLastMatch()

    def getLastMatches(self):
        return self.region.getLastMatches()


    """
    Returns an array of matches
    """
    def find_all(self, search_image, region = None):
        if(region == None):
            region = self.region
        try:
            return [m for m in region.findAll(search_image)]
        except:
            Debug.log("find_all: No matches found")
            pass
        return []

    def click_all(self, image, wait_between = 0, region = None):
        if(region == None):
            region = self.region
        
        times_clicked = 0            
        for match in self.find_all(image, region):
            self.click(match, 0, region, False)
            times_clicked +=1
            time.sleep(wait_between)
            
        return times_clicked
    
    def find_best_match(self, image, timeout = 0, region = None):
        """
        if(region == None):
            region = self.region
            
        match = None
        try:
            if(region.exists(image, timeout)):
                match = region.getLastMatch()
        except:
            pass
        
        return match
        """
        
        return self.find(image, timeout, region)
    
    def click_best_match(self, image, timeout = 0, region = None):
        """
        if(region == None):
            region = self.region
            
        match = self.find_best_match(image, timeout, region)
        if(match is None):
            return False
        region.click(match)
        return True
        """
        return self.click(image, timeout, region, False)

    ### CUSTOM FUNCTIONS
    def click_top(self, pattern, timeout = 0):
        if(timeout > 0):
            self.exists(pattern,timeout)
        matches = self.find_all(pattern)
        if(len(matches) == 0):
            Debug.log("Click Top: No matches found")
            return False
        matches.sort(key = lambda m: m.y)
        self.click(matches[0])
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
    
    def switch_browser_tabs(self, distance):
        for i in xrange(distance):
            self.switch_tab_right()
        for i in xrange(distance, 0):
            self.switch_tab_left()
            
    def close_current_tab(self):
        ki = KeyInterface.get_instance()
        self.type("W", ki.KeyModifier.CTRL)

    
    
def SRI():
    return SikuliRegionInterface.get_instance()

###

"""
Load all the pngs described in the png manifest of the directory
This png manifest is populated via the populate_png script

Example:  directory/this/is/a_png.png
          will be loaded in the png_object as
          png_object.this_is_a_png
"""
def png_manifest(directory = current_directory):
    class png_object(object):
        def __init__(self, directory):
            self.sets = {}
            try:
                file_path = directory + "/png_manifest"
                Debug.log("opening " + file_path)
                with io.open(file_path, "r", encoding="UTF-16") as pngs:
                    for line in pngs:
                        arr = line.split(" ")
                        if(len(arr) < 2):
                            continue
                        constant = arr[0].strip().upper()
                        path = arr[1].strip()
                        setattr(self, constant, path)
                        setattr(self, constant.lower(), path)

            except Exception as e:
                logging.error(e, exc_info=True)
                Debug.log("FAILURE: Could not populate png's")
        def get_by_string(s):
            pass
    return png_object(directory) 

###Miscellaneous
def write_to_file(filename, options, content):
    fi = open(current_directory + "\\" + filename, options)
    fi.write(str(content) + "\n")
    fi.close()
