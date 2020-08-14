from bs4 import BeautifulSoup
import requests
import time
from os import system
from sys import platform


def create_soup(url):
    r = requests.get(url)
    if str(r.status_code) == '404':
        print("Couldn't find that artist. Make sure that artist is available on AZLyrics website")
    elif str(r.status_code) != '200':
        print("An unexpected error occurred.")
    else:
        data = r.text
        soup = BeautifulSoup(data, 'lxml')
        return soup


def get_all_songs(soup):
    all_songs = []
    albums = soup.find('div', id='listAlbum')
    for songs in albums.findAll('a'):
        all_songs.append(songs.text)

    return all_songs


def format_name(string):
    string = string.lower()
    string = string.replace(' ', '')
    string = string.replace('(', '')
    string = string.replace(')', '')
    string = string.replace('?', '')
    string = string.replace("!", '')
    string = string.replace(",", '')
    string = string.replace("'", '')
    return string


def create_song_url(song, band_name):
    song = format_name(song)
    return f'https://www.azlyrics.com/lyrics/{band_name}/' + song + '.html'


def get_lyrics(url):
    f = open('lyrics.txt', 'a')
    soup = create_soup(url)
    main_container = soup.find('div', attrs="col-xs-12 col-lg-8 text-center")
    lyrics = main_container.findAll('div')[5].text
    f.write(lyrics)
    f.close()


def clear_screen():
    operating_system = platform
    if operating_system == 'win32':
        system('cls')
    else:
        system('clear')


def main():
    clear_screen()
    band_name = format_name(str(input('Please type the name of the desired artist: ')))
    url = f'https://www.azlyrics.com/{band_name[0]}/{band_name}.html'

    try:
        songlist = get_all_songs(create_soup(url))

    except:
        return 1

    else:
        total = len(songlist)

        for song in songlist:
            song_url = create_song_url(song, band_name)
            get_lyrics(song_url)
            total -= 1
            clear_screen()
            print(f'Lyrics successfully saved. {total} songs left.')
            print(f'Estimated time left: {int((total * 5)/60)} minutes')
            time.sleep(5)


main()
