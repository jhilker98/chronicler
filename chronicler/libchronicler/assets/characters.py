#!/usr/bin/env python3
"""
Contains the assets for a character.

The `libchronicler.assets.characters` module contains all the assets and resources for a single character in a single campaign.
"""

from enum import Enum



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
