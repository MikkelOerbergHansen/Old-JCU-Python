# create your Song class in this file


class Song:
    def __init__(self, title="", artist="", year=0, required=True):
        self.title = title
        self.artist = artist
        self.year = year
        self.is_required = required

    def mark_learned(self, user_input=False):
        self.is_required = user_input

    def __str__(self):
        return "{} by {} ({}) is required to learn: {}".format(self.title, self.artist, self.year, self.is_required)

    pass
