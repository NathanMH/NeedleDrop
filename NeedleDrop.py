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

# import os # Deprecated in lieu of subprocess and glob
import easygui
import random
from mutagen.mp3 import MP3
import glob
import pygame


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
def get_random_time(song_length):
    """ Get a random time from a song """
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
    test_directory = "C:/Users/Nathan Mador-House/Music/*.mp3"
    test_songs_list = get_all_songs(test_directory)
    test_list_chosen_songs = gui_choose_songs(test_songs_list)
    test_random_song = test_list_chosen_songs[get_random_song(test_list_chosen_songs)]
    audio = MP3(test_random_song)
    test_random_time = get_random_time(audio.info.length)
    print(test_random_song)
    print(test_random_time)
    play_song_at_time(test_random_song, test_random_time)

    easygui.msgbox("Program is finished.", "NeedleDrop")

windows_test()

# def linux_test():
#     test_directory = "/home/musicnate/Music/favs"

#       TRY USING GLOB INSTEAD OF os.listdir()
#     test_directory_files = os.listdir(test_directory)
#     test_user_choice_songs = []

#     test_songs_list = get_all_songs(test_directory, test_directory_files)
#     test_list_of_user_chosen_songs = gui_choose_songs(test_songs_list)
#     test_random_song = get_random_song(test_list_of_user_chosen_songs)
#     print(test_random_song)

#     test_random_mp3 = "/home/musicnate/Music/favs/20. Signals.mp3"
#     test_random_time = 124

#     easygui.msgbox("Program is finished.", "NeedleDrop")

# test()


