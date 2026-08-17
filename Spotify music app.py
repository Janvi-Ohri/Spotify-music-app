# SPOTIFY MUSIC APP

class Music:
    def __init__(self, title, artist, genre):
        self.title = title
        self.artist = artist
        self.genre = genre

    def display(self):
        print("Title:", self.title)
        print("Artist:", self.artist)
        print("Genre:", self.genre)


class Song(Music):
    def __init__(self, title, artist, genre, duration):
        super().__init__(title, artist, genre)
        self.duration = duration

    def display(self):
        super().display()
        print("Duration:", self.duration)


class Playlist:
    def __init__(self, name, songs):
        self.name = name
        self.songs = songs

    def add_song(self, song):
        self.songs.append(song)

    def show_playlist(self):
        print("Playlist Name:", self.name)

        if len(self.songs) == 0:
            print("No songs in the playlist")
        else:
            for song in self.songs:
                print(song.title, "-", song.artist)


song1 = Song("Shape of You", "Ed Sheeran", "Pop", 3.5)
song2 = Song("Tum hi ho", "Arijit Singh", "Romantic", 4)
song3 = Song("Bekhayali", "Arijit Singh", "Pop", 4.5)
song4 = Song("Boyfriend", "Karan Aujla", "Romantic", 4)

songs = [song1, song2, song3, song4]

playlist = Playlist("My Playlist", songs)

# Main Menu
while True:

    print("\n===== SPOTIFY MUSIC APP =====")
    print("1. Show All Songs")
    print("2. Search Song")
    print("3. Play Song")
    print("4. Add Song to Playlist")
    print("5. Show Playlist")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n===== ALL SONGS =====")

        for song in songs:
            print()
            song.display()

    elif choice == "2":
        search = input("Enter song title: ")
        found = False

        for song in songs:
            if search.lower() in song.title.lower():
                print("\nSong Found:")
                song.display()
                found = True

        if found == False:
            print("Song not found.")

    elif choice == "3":
        search = input("Enter song title to play: ")
        found = False

        for song in songs:
            if search.lower() == song.title.lower():
                print("\nNow Playing 🎵")
                print(song.title, "-", song.artist)
                found = True

        if found == False:
            print("Song not found.")

    elif choice == "4":
        search = input("Enter song title: ")
        found = False

        for song in songs:
            if search.lower() == song.title.lower():
                playlist.add_song(song)
                print("Song added to playlist.")
                found = True

        if found == False:
            print("Song not found.")

    elif choice == "5":
        playlist.show_playlist()

    elif choice == "6":
        print("Thank you for using Spotify Music App!")
        break

    else:
        print("Invalid choice. Please try again.")