"""
Name: Mikkel Oerberg Hansen
Date: 20 may 2018
Brief Project Description:
GitHub URL: https://github.com/CP1404-2018-51/a2-MikkelOerberg
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty
from songlist import SongList
from song import Song

# Create your main program in this file, using the SongsToLearnApp class


class SongsToLearnApp(App):
    status_text = StringProperty()
    is_required_text = StringProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.my_song_list = SongList()
        self.my_song_list.load_songs("Assignments/a2-MikkelOerberg/songs.csv")
        self.song_list = self.my_song_list.songs
        self.sort_options = ["title", "artist", "year", "is_required"]
        self.current_sort = self.sort_options[2]

    def build(self):
        self.title = "Songs To Learn 2.0"
        self.root = Builder.load_file('app.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        learned_songs = self.my_song_list.get_learned_songs()
        required_songs = self.my_song_list.get_required_songs()
        for song in self.song_list:
            title = song.title
            artist = song.artist
            year = song.year
            learned = song.is_required
            if learned is False:
                my_text = '"{}" by {} ({}) (Learned)'.format(title, artist, year)
                button_color = [1, 1, 0, 1]
            else:
                my_text = '"{}" by {} ({})'.format(title, artist, year)
                button_color = [0, 1, 1, 1]
            temp_button = Button(text=my_text,id=title, background_color=button_color)
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.entries_box.add_widget(temp_button)
        self.is_required_text = "To learn: {}, Learned: {}".format(required_songs, learned_songs)

    def press_entry(self, instance):
        name = instance.id
        song1 = self.my_song_list.get_song(name)
        if song1.is_required is False:
            self.status_text = "you have marked '{}' as required".format(song1.title)
            song1.mark_learned(True)
        else:
            self.status_text = "you have marked '{}' as learned".format(song1.title)
            song1.mark_learned(False)
        self.root.ids.entries_box.clear_widgets()
        self.create_widgets()

    def add_song(self):
        title = self.root.ids.input_title.text
        artist = self.root.ids.input_artist.text
        year = self.root.ids.input_year.text
        check_status = self.error_check(title, artist, year)
        if check_status is True:
            self.clear_all()
            new_song = Song(title.title(), artist.title(), int(year))
            self.my_song_list.add_song(new_song)
            self.song_list = self.my_song_list.songs
            self.status_text = "you have added '{}' by {} ({})".format(new_song.title, new_song.artist, new_song.year)
            button_text = '"{}" by {} ({})'.format(new_song.title, new_song.artist, new_song.year)
            temp_button = Button(text=button_text, id=new_song.title, background_color=[0, 1, 1, 1])
            temp_button.bind(on_release=self.press_entry)
            self.root.ids.entries_box.add_widget(temp_button)
            learned_songs = self.my_song_list.get_learned_songs()
            required_songs = self.my_song_list.get_required_songs()
            self.is_required_text = "To learn: {}, Learned: {}".format(required_songs, learned_songs)

    def clear_all(self):
        self.root.ids.input_title.text = ""
        self.root.ids.input_artist.text = ""
        self.root.ids.input_year.text = ""
        self.status_text = ""

    def change_sort(self, sorting_choice):
        self.status_text = "songs have been sorted by: {}".format(sorting_choice)
        self.my_song_list.sort(sorting_choice)
        self.song_list = self.my_song_list.songs
        self.root.ids.entries_box.clear_widgets()
        self.create_widgets()
        sort_index = self.sort_options.index(sorting_choice)
        self.current_sort = self.sort_options[sort_index]

    def on_stop(self):
        self.my_song_list.save_songs()

    def error_check(self, title, artist, year):
        try:
            if not title:
                self.status_text = "all files must be completed"
                raise ValueError()
            if not artist:
                self.status_text = "all files must be completed"
                raise ValueError()
            if not year:
                self.status_text = "all files must be completed"
                raise ValueError()
        except ValueError:
            return False
        try:
            int(year)
        except ValueError:
            self.status_text = "please enter a valid number"
            return False
        try:
            if not int(year) > 0:
                self.status_text = "please enter a valid number"
                raise ValueError()
        except ValueError:
            return False
        return True

    pass


SongsToLearnApp().run()
