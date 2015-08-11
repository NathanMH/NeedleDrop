#!/usr/bin/env python3

"""####################
Author: Nathan Mador-House
####################"""

#######################
"""####################
Index:
    1. Imports and Readme
    2. Initialization Functions
    3. Setup with supplied files
    4. General Functions
    5. Mai
    6. Testing
####################"""
#######################

###################################################################
# 1. IMPORTS AND README
###################################################################

import os
import sys
import random

from hsaudiotag import auto
import easygui

###################################################################
# 2. INITIALIZATION FUNCTIONS
###################################################################

fileArray = []
mp3Array = []
choices = []

def chooseDirectory():
    directory = easygui.diropenbox("Choose Music Folder", "NeedleDrop") + "\\"
    print(directory)
    return os.listdir(directory)

###################################################################
# 3. SETUP WITH SUPPLIED FILES
###################################################################

###################################################################
# 4. GENERAL FUNCTIONS
###################################################################

# Make a list of all the valid mp3 files available
def makeMp3Array():
    for i in range(0, len(fileArray) - 1):
        print(i)
        try:
            if auto.File(fileArray[i]).valid:
                mp3Array.append(fileArray[i])
                print("Added file to array")
        except:
            # This is only if the file has permission errors
            pass

# Get user to choose which mp3 files will be randomized
def chooseSongs():
	choices = []
	choices = easygui.multchoicebox(msg="Select the songs you would like to study.", title="NeedleDrop", choices=mp3Array)

def chooseRandomSong(songMax):
	randomSong = random.randrange(songMax) 
	return randomSong

# Randomly selects a start time
def chooseRandomTime(timeMax):
	if timeMax > 60:
		randomTime = random.randrange(timeMax - 60)
	else:
		randomTime = random.randrange(timeMax)
	return randomTime 



###################################################################
# 5. MAIN
###################################################################

###################################################################
# 6. TESTING
###################################################################

chooseDirectory()
print(fileArray[1])
#makeMp3Array()
#chooseSongs()

for i in mp3Array:
    print(i)
#randomSong = choices[chooseRandomSong(len(choices))]
#print("Now playing " + randomSong)

#randomSong = mp3Array[chooseRandomSong(len(mp3Array))]
#randomTime = chooseRandomTime(auto.File(randomSong).duration)

#playable = repr(randomSong)

# Play music
#os.system("mplayer "+ directory + playable + " -ss " + str(randomTime))

#print(playable)


