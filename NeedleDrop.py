#!/usr/bin/env python3

"""####################
Author: Nathan Mador-House
####################"""

#######################
"""####################
Index:
    1. Imports and Readme
    2. Functions
    3. Main
    4. Testing
####################"""
#######################

###################################################################
# 1. IMPORTS AND README
###################################################################

import os
import sys
import random
import easygui
import sndhdr
from mutagen.mp3 import MP3

###################################################################
# 2. FUNCTIONS
###################################################################

def user_choose_directory():
    """ Get root directory from user """
    return easygui.diropenbox("Choose Music Folder", "NeedleDrop")

def get_all_mp3s(location, files):
    """ Make a list of all the valid mp3 files available """
    mp3_list = []
    for i in range(0, len(files) - 1):
        print(files[i])
        if files[i].lower().endswith(".mp3"):
            mp3_list.append(files[i])
        elif sndhdr.what(location + files[i]) != None:
            mp3_list.append(files[i])
        else:
            print("uh oh")
    return mp3_list

# Get user to choose which mp3 files will be randomized
def user_choose_songs(song_list):
    """ User selects songs """
    return easygui.multchoicebox(msg="Select the songs you would like to study.",\
                                 title="NeedleDrop", choices=song_list)

# Select a random song
def get_random_song(songlist):
    """ Get random song from user selected list """
    return random.randrange(len(songlist))

# Randomly selects a start time
def choose_random_time(song_length):
    """ Get a random time from a song """
    if limit > 60:
        time = random.randrange(limit - 60)
    else:
        time = random.randrange(limit)
    return time

def play_song_at_time(songnumber, songlist):
    # vlc.play(songlist[songnumber])
    pass

###################################################################
# 5. MAIN
###################################################################

###################################################################
# 6. TESTING
###################################################################

test_directory = "/home/musicnate/Music/favs"
test_directory_files = os.listdir(test_directory)
test_song_path = "/home/musicnate/Music/favs/20. Signals.mp3"


### 1. User chooses directory
# user_directory_choice = user_choose_directory()

### 2. Get list of files from directory 
# list_of_files = os.listdir(user_directory_choice)

### 3. Filter list for mp3s
# list_of_mp3s = get_all_mp3s(user_directory_choice, list_of_files)

### 4. User chooses mp3s
# list_of_user_chosen_mp3s = user_choose_songs(list_of_mp3s)

### 5. Random song from user selected
# random_mp3 = get_random_song(list_of_user_chosen_mp3s)

### 6. Random time
# random_time = choose_random_time(200)

### 7. Make a system readable string
# system_string = "vlc" + user_directory_choice + random_mp3

### 8. Play song at random time
# os.system(system_string)


def test():

    user_directory_choice = test_directory
    list_of_files = os.listdir(user_directory_choice)
    list_of_mp3s = get_all_mp3s(user_directory_choice, list_of_files)
    list_of_user_chosen_mp3s = user_choose_songs(list_of_mp3s)
    random_mp3 = get_random_song(list_of_user_chosen_mp3s)

test()

#audio = MP3(test_song_path)
#print(audio.info.length)


