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
import subprocess
import random
import easygui
import sndhdr
from mutagen.mp3 import MP3


###################################################################
# 2. FUNCTIONS
###################################################################

def gui_choose_directory():
    """ Get root directory from user """
    return easygui.diropenbox("Choose Music Folder", "NeedleDrop")


def get_all_mp3s(location, files):
    """ Make a list of all the valid mp3 files available from directory """
    mp3_list = []
    for i in range(0, len(files) - 1):
        if files[i].lower().endswith(".mp3"):
            mp3_list.append(files[i])
        elif sndhdr.what(location + files[i]) is not None:
            mp3_list.append(files[i])
        else:
            print("uh oh")
    return mp3_list


# Get user to choose which mp3 files will be randomized
def gui_choose_songs(song_list):
    """ User selects songs """
    return easygui.multchoicebox(msg="Select the songs you would like to study.", title="NeedleDrop", choices=song_list)


# Select a random song
def get_random_song(song_list):
    """ Get random song from user selected list """
    return random.randrange(len(songlist))


# Randomly selects a start time
def get_random_time(mp3_file):
    """ Get a random time from a song """
    if song_length > 60:
        time = random.randrange(song_length - 60)
    else:
        time = random.randrange(song_length)
    return time


def play_song_at_time(songnumber, songlist):
    if sys.platform == "win32":
        os.start(songlist[songnumber])
    else:
        opener = "open"
        subprocess.call([opener, songlist[songnumber]])
    # vlc.play(songlist[songnumber])
    pass

###################################################################
# 5. MAIN
###################################################################

###################################################################
# 6. TESTING
###################################################################

# 1. User chooses directory
# 2. Get list of files from directory
# 3. Filter list for mp3s
# 4. User chooses mp3s
# 5. Random song from user selected
# 6. Random time
# 7. Make a system readable string
# 8. Play song at random time


def windows_test():
#     windows_test_directory = "C:\\Users\\Nathan\ Mador-House\\Music\\Favs\\"
    easygui.msgbox("Select the songs you would like to study.", "NeedleDrop")

windows_test()

# def linux_test():
#     test_directory = "/home/musicnate/Music/favs"
#     test_directory_files = os.listdir(linux_test_directory)
#     test_user_choice_mp3s = []

#     test_mp3_list = get_all_mp3s(test_directory, test_directory_files)
#     test_list_of_user_chosen_mp3s = gui_choose_songs(test_mp3_list) USE PREMADE SELECTION
#     test_random_mp3 = get_random_song(test_list_of_user_chosen_mp3s)
#     print(test_random_mp3)

#     test_random_mp3 = "/home/musicnate/Music/favs/20. Signals.mp3"
#     test_random_time = 124

# test()


# PLAY MUSIC
# audio = MP3(test_song_path)
# print(audio.info.length)
# test_system_string = "os.startfile('test_random_mp3')"

