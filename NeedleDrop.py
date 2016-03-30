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
import random
# from hsaudiotag import auto
import easygui

###################################################################
# 2. FUNCTIONS
###################################################################

def user_choose_directory():
    """ Get root directory from user """
    return os.listdir(easygui.diropenbox("Choose Music Folder", "NeedleDrop"))

def get_all_mp3s(files):
    """ Make a list of all the valid mp3 files available """
    mp3_list = []
    for i in range(0, len(files) - 1):
        print(files[i])
        try:
            if auto.File(files[i]).valid:
                mp3_list.append(directory + fileArray[i])
                print("Added file to array")
        except:
            print("uh oh")
            # This is only if the file has permission errors
    return mp3_list

# Get user to choose which mp3 files will be randomized
def user_choose_songs(song_list):
    """ User selects songs """
    return easygui.multchoicebox(msg="Select the songs you would like to study.",\
                                 title="NeedleDrop", choices=song_list)

# Select a random song
def get_random_song(songlist):
    """ Get random song from user selected list """
    return random.randrange(limit)

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

# 1. directory
# 2. list of mp3s
# 3. user chooses mp3s
# 4. random song from user selected
# 5. random time
# 6. play song at random time


def test():
    """"""
    #song = get_random_song(user_choose_songs(get_all_mp3s(user_choose_directory())))
    #time = choose_random_time(200)
    chosen_directory = user_choose_directory()
    list_of_all_mp3s = get_all_mp3s(chosen_directory)
    list_of_user_chosen_mp3s = user_choose_songs()
    random_mp3 = get_random_song()

    print(directory)


    #return os.listdir(directory)

