import sys
from json.decoder import JSONDecodeError
import requests
from requests.exceptions import HTTPError

ITUNES_API_ENDPOINT = 'https://itunes.apple.com/search'


class GetFirstAlbumError(Exception):
    """Failed to get first album"""


class QueryAlbumError(Exception):
    """Failed to get album list"""


def command_first_album():
    """通过脚本输入查找并打印歌手的第一张专辑信息"""
    if not len(sys.argv) == 2:
        print(f'usage: python {sys.argv[0]} {{SEARCH_TERM}}')
        sys.exit(1)

    artist = sys.argv[1]
    try:
        album = get_first_album(artist)
    except GetFirstAlbumError as e:
        print(f"error: {e}", file=sys.stderr)
        sys.exit(2)

    print(f"{artist}'s first album:")
    print(f" * Name: {album['name']}")
    print(f" * Genre: {album['genre_name']}")
    print(f" * Released at: {album['release_date']}")


def get_first_album(artist):
    """Get first album in the album list

    :param artist: name of artist
    :return: fist album
    :raises: raise GetFirstAlbumError when error happens
    """
    try:
        albums = query_all_albums(artist)
    except QueryAlbumError as e:
        raise GetFirstAlbumError(str(e))

    sorted_albums = sorted(albums, key=lambda item: item['releaseDate'])
    first_album = sorted_albums[0]

    release_date = first_album['releaseDate'].split('T')[0]
    return {
        'name': first_album['collectionName'],
        'genre_name': first_album['primaryGenreName'],
        'release_date': release_date,
    }


def query_all_albums(artist):
    """Search all album list by artis's name"""
    resp = requests.get(
        ITUNES_API_ENDPOINT,
        {
            'term': artist,
            'media': 'music',
            'entity': 'album',
            'attribute': 'artistTerm',
            'limit': 200,
        },
    )
    try:
        resp.raise_for_status()
    except HTTPError as e:
        raise QueryAlbumError(f'failed to call iTunes API, {e}')

    try:
        albums = resp.json()['results']
    except JSONDecodeError:
        raise QueryAlbumError('response is not valid JSON format')

    if not albums:
        raise QueryAlbumError(f'no albums found for artist "{artist}"')
    return albums


if __name__ == '__main__':
    command_first_album()
