## Spotify Top Hits Ongoing Playlist
This app uses https://github.com/plamere/spotipy to interact with Spotify API.

This app will parse the Spotify 'Today's Top Hits' playlist and add those songs to a playlist.

### Running app
Setup ENV
```
export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
export SPOTIPY_REDIRECT_URI='your-app-redirect-url' (http://localhost/)
```
See https://spotipy.readthedocs.io/en/latest/#authorization-code-flow for more information

### Todos:
- Have app pull existing playlist IDs, delete playlist, create new playlist, add newest playlist songs, then add older songs to new playlist. This will ensure that the newest songs will always be at the top of the playlist.
- Create setup script to export variables, create playlists (above), etc.
- At the end of each month have Python create a Top Hits Playlist for that Month, at the end of the year combine that into a Yearly Top Hit Playlist.
- Set a max song limit to the 'main' playlist, default maybe at 200?
