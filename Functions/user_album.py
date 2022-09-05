def make_album(artist_name, album_title, tracks=''):
    play_list = {'Artist-name': artist_name, 'Album-title': album_title}
    if tracks:
        play_list['track-no'] = tracks

    return play_list


while True:
    print("\nPlease tell me Artist: name and album")
    print("(enter 'q' at any time to quit)")

    A_name = input("Artist full names: ")
    if A_name == 'q':
        break

    A_album = input("Artist Album: ")
    if A_album == 'q':
        break

    No_tracks = input("Album's total tracks: ")
    if No_tracks == 'q':
        break

    results = make_album(A_name, A_album, No_tracks)
    print(results)
