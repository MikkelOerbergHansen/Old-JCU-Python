# create your SongList class in this file

import csv
from song import Song
from operator import attrgetter


class SongList:

    def __init__(self):
        self.songs = []

    def load_songs(self, file="Assignments/a2-MikkelOerberg/songs.csv"):
        with open(file, "r") as csv_file:
            song_array = list(csv.reader(csv_file))
        for song in song_array:
            if song[3] == "n":
                new_song = Song(song[0], song[1], int(song[2]), True)
            else:
                new_song = Song(song[0], song[1], int(song[2]), False)
            self.songs.append(new_song)

    def save_songs(self):
        with open("Assignments/a2-MikkelOerberg/songs.csv", "w", newline="") as file:
            song_list = csv.writer(file)
            for song in self.songs:
                save_song = [song.title, song.artist, song.year, "y" if (song.is_required is False) else "n"]
                song_list.writerow(save_song)
        file.close()
        print(str(len(self.songs)) + " songs saved to csv")

    def sort(self, key):
        self.songs = sorted(self.songs, key=attrgetter(key, "title"))

    def get_learned_songs(self):
        learned_songs = 0
        for song in self.songs:
            if song.is_required is False:
                learned_songs += 1
        return learned_songs

    def get_required_songs(self):
        required_songs = 0
        for song in self.songs:
            if song.is_required is True:
                required_songs += 1
        return required_songs

    def get_song(self, user_title=""):
        for song in self.songs:
            if user_title == song.title:
                return song
        return None

    def add_song(self, song):
        self.songs.append(song)

    def __str__(self):
        list_index = 1
        string_for_print = "Song List:\n"
        for song in self.songs:
            string_for_print = string_for_print + "{}. {} {:<30} - {:<30} ({})\n".format(
                str(list_index),
                "*" if (song.is_required is False) else " ",
                song.title, song.artist, song.year)
            list_index += 1
        return string_for_print

    pass
