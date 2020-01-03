import sys
import pprint
import spotipy
import spotipy.util as util

scope = 'playlist-read-private playlist-modify-public'
top_hits_id = '37i9dQZF1DXcBWIGoYBM5M'
playlist_id = '5QZxZRZlOBJuVDRky3Uqh6'


def get_tracks(username, playlist):
    results = spotify.user_playlist(username, playlist, fields="tracks")
    tracks = results['tracks']
    track_ids = []

    for item in tracks['items']:
        track = item['track']
        track_ids.append(track['id'])
        # track_name = track['name']
        # track_artist = track['artists'][0]['name']
        # print(f"{track_name} By: {track_artist} ID: {track_id}")
    return track_ids


if __name__ == '__main__':
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("Usage: {0} username".format(sys.argv[0]))
        sys.exit()

    token = util.prompt_for_user_token(username, scope)
    spotify = spotipy.Spotify(auth=token)

    if token:
        new_tracks = get_tracks(username, top_hits_id)
        existing_tracks = get_tracks(username, playlist_id)
        tracks_to_add = []
        for track in new_tracks:
            if track not in existing_tracks:
                tracks_to_add.append(track)
        # print(tracks_to_add)
        results = spotify.user_playlist_add_tracks(username, playlist_id, tracks_to_add)
        pprint.pprint(results)
    else:
        print("Can't get token for", username)
