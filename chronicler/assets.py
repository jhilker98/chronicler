"""
Contains the assets for an AAR.

The `chronicler.assets` module contains all the assets and resources for an AAR.
"""
class Character:
    
    def __init__(self):
        """
        Creates a Character.
        """
        self.__name = ""
        __culture = ""
        __birth_date = None
        __status = ""
        __age = 0
        __gender = ""
        __rank = ""
        #__homeland = None
        __regions_ruled = []
        #__dynasty = None
        __titles = []
        __traits = []
