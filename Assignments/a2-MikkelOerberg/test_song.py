"""(Incomplete) Tests for Song class."""
from song import Song

# test empty song (defaults)
song = Song()
print(song)
assert song.artist == ""
assert song.title == ""
assert song.year == 0
assert song.is_required

# test initial-value song
song2 = Song("Amazing Grace", "John Newton", 1779, True)
print(song2)
print(song2.title)
assert song2.title == "Amazing Grace"
print(song2.artist)
assert song2.artist == "John Newton"
print(song2.year)
assert song2.year == 1779
print(song2.is_required)
assert song2.is_required is True
# DONE: write tests to show this initialisation works

# test mark_learned()
song2.mark_learned()
assert song2.is_required is False
print(song2)
song2.mark_learned(True)
assert song2.is_required is True
print(song2)
# DONE: write tests to show the mark_learned() method works
