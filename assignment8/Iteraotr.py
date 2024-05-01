class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def __repr__(self):
        return f"{self.title} by {self.artist}"

class Iterator:
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def hasNext(self):
        return self.index < len(self.collection)

    def next(self):
        if self.hasNext():
            song = self.collection[self.index]
            self.index += 1
            return song
        else:
            raise StopIteration

class Playlist:
    def createIterator(self):
        raise NotImplementedError

    def addSong(self, song):
        raise NotImplementedError

class PlaylistImpl(Playlist):
    def __init__(self):
        self.songs = []

    def addSong(self, song):
        self.songs.append(song)

    def createIterator(self):
        return Iterator(self.songs)

if __name__ == "__main__":
    my_playlist = PlaylistImpl()
    my_playlist.addSong(Song("Yesterday", "The Beatles"))
    my_playlist.addSong(Song("Stairway to Heaven", "Led Zeppelin"))
    my_playlist.addSong(Song("Hotel California", "The Eagles"))

    song_iterator = my_playlist.createIterator()

    print("Songs in the playlist:")
    while song_iterator.hasNext():
        print(song_iterator.next())
