"""
(incomplete) Tests for SongList class
"""
from songlist import SongList
from song import Song

# test empty SongList
song_list = SongList()
print(song_list)
assert len(song_list.songs) == 0

# test loading songs
song_list.load_songs('songs.csv')
assert len(song_list.songs) == 6
print(song_list)
assert len(song_list.songs) > 0  # assuming CSV file is not empty

# Done: add tests below to show the various required methods work as expected
# test sorting songs
song_list.sort("artist")

# test adding a new Song
song_list.add_song(Song("Amazing Grace", "John Newton", 1779, True))
print(song_list)


# test get_song()
song1 = song_list.get_song("Macarena")
print(song1)
assert song1.title == "Macarena"
assert song1.artist == "Los Del Rio"
assert song1.year == 1996
assert song1.is_required is True

song2 = song_list.get_song("katchi")
assert song2 is None

# test getting the number of required and learned songs (separately)
print(song_list.get_required_songs())
print(song_list.get_learned_songs())
assert song_list.get_required_songs() == 3
assert song_list.get_learned_songs() == 4

# test saving songs (check CSV file manually to see results)
# song_list.save_songs()
