import pafy
import os

def get_infos_about_playlist(playlist) -> str:
    title = playlist['title']
    author = playlist['author']

    return f'Title: \'{title}\' Author: \'{author}\''
def get_infos_about_video(video) -> str:
    title = video.title
    author = video.author
    duration = video.duration

    return f'Title: \'{title}\'  Author: \'{author}\'  Duration: \'{duration}\''


def iterate_playlist(out_type):
    urls = input('URLS(;): ').split(';')

    for playlist in urls:
        print('Infos: ' + get_infos_about_playlist(playlist))
        items = playlist['items']
        print(f'Length: {len(items)}')
        os.mkdir(playlist['title'])
        l = len(items)
        print(f'0%')
        for i in range(len(items)):
            item = items[i - 1]['pafy']
            if out_type.lower() == 'mp4':
                download = item.getbest().download(filepath=playlist['title'])
            if out_type.lower() == 'mp3':
                download = item.getbestaudio().download(filepath=playlist['title'])
            r = i
            procent = r / l
            procent = round(procent, 2)
            print(f'{procent * 100}%')
    print('Finished')
def iterate_video(out_type):
    videos = input('URLS(;): ').split(';')

    for video_raw in videos:
        video = pafy.new(video_raw)
        print('Infos: ' + get_infos_about_video(video))
        if out_type.lower() == 'mp3':
            download = video.getbestaudio().download()
        if out_type.lower() == 'mp4':
            download = video.getbest().download()
    print('Finished')
def setup_playlist(out_type):
    playlist = pafy.get_playlist(input('URL: '))

    print('Infos: ' + get_infos_about_playlist(playlist))
    items = playlist['items']
    i = input('See filesize y/n ')
    if i.lower() == 'y' or i.lower() == 'j':
        isg_filesize = 0
        for i in items:
            isg_filesize = isg_filesize + i['pafy'].getbest().get_filesize()
        ff = isg_filesize / 1000000000
        print(f'Filesize: {ff} GB')
    i = input('Download? y/n')
    if i.lower() == 'y' or i.lower() == 'j':


        print(f'Length: {len(items)}')
        os.mkdir(playlist['title'])
        l = len(items)
        print(f'0%')
        for i in range(len(items)):
            item = items[i - 1]['pafy']
            if out_type.lower() == 'mp4':
                download = item.getbest().download(filepath=playlist['title'])
            if out_type.lower() == 'mp3':
                download = item.getbestaudio().download(filepath=playlist['title'])
            r = i
            procent = r / l
            procent = round(procent, 2)
            print(f'{procent  * 100}%')
        print('Finished')
        return
    return
def setup_video(out_type):
    video =  pafy.new(input('URL: '))

    print('Infos: ' + get_infos_about_video(video))
    i = input('Download? y/n')
    if i.lower() == 'y' or i.lower() == 'j':
        if out_type.lower() == 'mp3':
            download = video.getbestaudio().download()
        if out_type.lower() == 'mp4':
            download = video.getbest().download()
        print('Finished')
    return
t = input('Type: ')
output = input('Output mp4/mp3 ')
if t.lower() == 'playlist':
    setup_playlist(output)
elif t.lower() == 'playlists':
    iterate_playlist(output)
elif t.lower() == 'videos':
    iterate_video(output)
else:
    setup_video(output)