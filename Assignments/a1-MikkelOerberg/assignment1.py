"""
Mikkel Oerberg Hansen
20/04/2018
https://github.com/CP1404-2017-2/a1-MikkelOerberg

program details
the program loads a list of songs
and lets the user choose between
- display a list
- add a song to list
- mark a song as being learned
- quitting the program

when user chooses to display a list
the list is sorted by artist
when the user chooses to add a song to the list
the input is error checked:
- no duplicate songs of title and artists
- input can not be blank
- and year of the song has to be a number of 4 digits and non-negative
when the user chooses to mark a song as learned
it checks if there are any songs left to be chosen and
it checks if user chooses a song that has not been learned yet.
it also checks for valid numbers.

after a choice the main menu is displayed asking for a new
choice. except if the choice is to quit, then the song list is saved
and the program stops.
"""
import csv


def main():
    print("Songs To Learn 1.0 - by <Mikkel Oerberg Hansen>")
    songs = load_songs()
    main_menu(songs)


def main_menu(songs):
    while True:
        menu = """
L - List songs
A - Add new song
C - Complete a song
Q - Quit"""
        print(menu)
        choice = input(">>> ").upper()
        choice = error_check(choice)

        if choice == "L":
            choice = ""
            songs = sorted(songs, key=lambda x: x[1].casefold())
            list_songs(songs)

        if choice == "C":
            choice = ""
            complete_a_song(songs)

        if choice == "A":
            choice = ""
            add_new_song(songs)

        if choice == "Q":
            print(str(len(songs)) + " songs saved to csv.")
            print("have a nice day :)")
            save_file(songs)
            raise SystemExit(0)


def error_check(choice):
    while choice != "Q" and choice != "L" and choice != "A" and choice != "C":
        print("wrong input. please try again")
        choice = input(">>> ").upper()
    return choice

# pseudo-code:
# def load_songs():
#   open("file-names.csv", "r") as file:
#   songs = list(csv.read(file))
#   print(str(len(songs)) + "songs loaded")
#   return songs


def load_songs():
    with open("songs.csv", "r") as file:
        songs = list(csv.reader(file))
        print(str(len(songs)) + " songs loaded")
        return songs


def list_songs(songs):
    list_index = 1
    learned_songs = 0
    for song in songs:
        print("{}. {} {:<30} - {:<30} ({})".format(
            str(list_index),
            "*" if (song[3] == "y") else " ",
            song[0], song[1], song[2]))
        list_index += 1
        if song[3] == "n":
            learned_songs += 1
    print("{} songs learned, {} songs still to learn".format(learned_songs, len(songs) - learned_songs))


# pseudo-code:
# def complete_a_song(list_of_songs):
#   learned_song = 0
#   for song in list_of_songs:
#       if song[3] = "n":
#           learned_song +=1
#   if learned_song == len(list_of_songs):
#       print("no more songs to learn")
#       print(main_menu)
#
#   while True:
#       try:
#           number = input("enter the number of a song to be marked as learned")
#           try:
#               number = int(number)
#           except ValueError
#               print("Error! input must be a number")
#               continue
#           if song_number <= 0:
#               print("number must be > 0")
#               raise ValueError()
#           if song_number > len(list_of_songs):
#               print("invalid song number")
#               raise ValueError()
#           song = list_of_songs[number-1]
#           if song[3] == "n":
#               print("you have already learned {}".format(song[0]))
#               raise ValueError()
#
#            print("{} by {} learned".format(song[0], song[1]))
#            song[3] = "n"
#            list_of_songs[number-1] = song
#            print(main menu)
#
#        except ValueError:
#            continue


def complete_a_song(songs):
    while True:
        learned_song = 0
        for song in songs:
            if song[3] == "n":
                learned_song += 1
        if learned_song == len(songs):
            print("No more songs to learn!")
            main_menu(songs)

        try:
            print("enter the number of a song to be marked as learned")
            song_number = input(">>> ")
            try:
                song_number = int(song_number)
            except ValueError:
                print("invalid input; enter a valid number")
                continue
            if song_number <= 0:
                print("number must be > 0")
                raise ValueError()
            if song_number > len(songs):
                print("invalid song number")
                raise ValueError()

            if songs[song_number - 1][3] == "n":
                print("you have already learned {}".format(songs[song_number-1][0]))
                raise ValueError()

            print("{} by {} learned".format(songs[song_number-1][0], songs[song_number-1][1]))
            songs[song_number-1][3] = "n"
            main_menu(songs)

        except ValueError:
            continue


def add_new_song(songs):
    song = []
    while True:
        try:
            title = input("Title: ")
            if not title:
                print("input can not be blank")
                raise ValueError()
            artist = input("Artist: ")
            if not artist:
                print("input can not be blank")
                raise ValueError
            for currentSong in songs:
                if title.lower() == str(currentSong[0]).lower() and artist.lower() == str(currentSong[1]).lower():
                    print("the song is already in the list")
                    raise ValueError()
            break
        except ValueError:
            continue

    while True:
        try:
            year = input("Year: ")
            try:
                year = int(year)
            except ValueError:
                print("invalid input; enter a valid year")
                continue
            if year < 0:
                print("The year must be >= 0")
                raise ValueError()
            if len(str(year)) < 4 or len(str(year)) > 4:
                print("the year must have 4 digits; enter a valid year")
                raise ValueError
            break
        except ValueError:
            continue

    song.append(title)
    song.append(artist)
    song.append(year)
    song.append("y")
    print("{} by {} ({}) added to song list".format(title, artist, year))
    songs.append(song)
    main_menu(songs)


def save_file(songs):
    with open("songs.csv", "w", newline="") as file:
        song_list = csv.writer(file)
        for song in songs:
            song_list.writerow(song)
    file.close()


if __name__ == '__main__':
    main()
