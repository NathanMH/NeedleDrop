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

import glob
import platform
import random
import easygui
import pygame
from mutagen.mp3 import MP3


###################################################################
# 2. FUNCTIONS
###################################################################

def gui_choose_directory():
    """ Get root directory from user """
    return easygui.diropenbox("Choose Music Folder", "NeedleDrop")


def get_all_songs(location):
    """ Make a list of all the valid mp3 files available from directory """
    mp3_list = glob.glob(location)
    return mp3_list


# Get user to choose which mp3 files will be randomized
def gui_choose_songs(song_list):
    """ User selects songs """
    return easygui.multchoicebox(msg="Select the songs you would like to study.", title="NeedleDrop", choices=song_list)


# Select a random song
def get_random_song(song_list):
    """ Get random song from user selected list """
    return random.randrange(len(song_list))


# Randomly selects a start time
def get_random_time(song):
    """ Get a random time from a song """
    audio = MP3(song)
    song_length = audio.info.length
    if song_length > 60:
        time = random.randrange(int(song_length) - 60)
    else:
        time = random.randrange(song_length)
    return time


def play_song_at_time(song, time):
    pygame.mixer.init()
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(1, time)

###################################################################
# 5. MAIN
###################################################################

def main():
    user_os = platform.system().lower()
    if user_os == "windows":
        directory = gui_choose_directory() + "\*.mp3"
    elif user_os == "linux":
        directory = gui_choose_directory() + "/*.mp3"
    elif user_os == "darwin":
        directory = gui_choose_directory() + "/*.mp3"

    songs_list = get_all_songs(directory)
    chosen_songs = gui_choose_songs(songs_list)
    random_song = chosen_songs[get_random_song(chosen_songs)]
    print(random_song)
    random_time = get_random_time(random_song)
    play_song_at_time(random_song, random_time)
    easygui.msgbox("Program is playing a song.", "NeedleDrop")
 
main()

###################################################################
# 6. TESTING
###################################################################

# 1. User chooses directory
# 2. Get list of songs from directory
# 3. User chooses mp3s
# 4. Random song from user selected
# 5. Random time
# 6. Make a system readable string
# 7. Play song at random time


