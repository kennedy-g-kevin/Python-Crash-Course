def make_album(artist_name, album_title, number_of_songs=None):
    """This function takes input and returns output"""
    return {'artist_name': artist_name, 'album_title': album_title, 'number_of_songs': number_of_songs}


call_1 = make_album('Artist 1', 'Album 1')
call_2 = make_album('Artist 2', 'Album 2')
call_3 = make_album('Artist 3', 'Album 3', 6)

print(call_1)
print(call_2)
print(call_3)
