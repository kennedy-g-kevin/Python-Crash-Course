def make_album(artist_name, album_title, number_of_songs=None):
    """This function takes input and returns output"""
    return {'artist_name': artist_name, 'album_title': album_title, 'number_of_songs': number_of_songs}

while True:
    print('Enter "q" to quit at any time.')

    artist_name = input('Please provide an artist name: ')
    if artist_name == 'q':
        break

    album_title = input('Please provide one of their albums titles: ')
    if album_title == 'q':
        break

    call_1 = make_album(artist_name, album_title)

    print(call_1)
