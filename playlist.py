# This file is a data modeling example based on a spotify playlist
playlist = {
    'title': 'patagonia bus',
    'author': 'sohail',
    'songs': [
        {'title': 'Song 1', 'artist':['blue'], 'duration':2.5},
        {'title': 'Song 2', 'artist':['blue', 'DJ Cat'], 'duration':5.5},
        {'title': 'Song 3', 'artist':['garfield'], 'duration':4.0}
    ]
}

total_length = 0
for song in playlist['songs']:
    total_length += song['duration']

print(total_length)
