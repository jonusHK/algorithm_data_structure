def get_ext(file_name):
    return file_name.split('.')[-1]


def get_size(file_size):
    return int(file_size[:-1])


def solution(str):
    try:
        music_ext = ['mp3', 'aac', 'flac']
        image_ext = ['jpg', 'bmp', 'gif']
        movie_ext = ['mp4', 'avi', 'mkv']

        str_li = str.split()
        print('str_li - ', str_li)
        music_size = 0
        image_size = 0
        movie_size = 0
        other_size = 0

        for i in range(0, len(str_li), 2):
            file_ext = get_ext(str_li[i])
            file_size = get_size(str_li[i + 1])
            if file_ext in music_ext:
                music_size += file_size
            elif file_ext in image_ext:
                image_size += file_size
            elif file_ext in movie_ext:
                movie_size += file_size
            else:
                other_size += file_size
        
        return f'music {music_size}b\nimages {image_size}b\nmovies {movie_size}b\nother {other_size}b'

    except Exception as e:
        raise e

print(solution('my.song.mp3 11b greatSong.flac 1000b not3.txt 5b video.mp4 200b game.exe 100b mov!e.mkv 10000b'))
