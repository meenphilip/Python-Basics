def make_album(artist_name, album_title, tracks=''):
    play_list = {'Artist-name': artist_name, 'Album-title': album_title}
    if tracks:
        play_list['track-no'] = tracks

    return play_list


music = make_album('Tylor swift', '22', 15)
print(music)
music = make_album('Byrson tiller', 'Trap Soul')
print(music)
music = make_album('Chris Brown', 'X')
print(music)
music = make_album('August Alsina', 'Testimony')
print(music)
