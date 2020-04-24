import lyricsgenius as genius
from pandas impor DataFrame
from time import sleep

def collect_artist_lyrics(artist_list, nsongs=50, api_key):

    print("Searching for {} lyrics for {} and {}. Stand by...".format(nsongs,
    artist_list[0], artist_list[1]))

    api = genius.Genius('api_key')

    df = []
    for name in artist_list:
        try:
            artist_songs = api.search_artist(name, max_songs=nsongs)
            for i in range(len(artist_songs)):
                try:
                    df.append([artist_songs.songs[i].artist, artist_songs.songs[i].title , artist_songs.songs[i].lyrics])
                    time.sleep(0.5)
                except:
                    print('Failed to find {} by {}'.format(artist_songs.songs[i].artist, artist_songs.songs[i].title))
                    time.sleep(0.5)
        except:
            print('Failed on {}'.format(name))

        return pd.DataFrame(df, columns=['artist','song','lyrics'])
