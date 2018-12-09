import magic
import requests

from . import constants


def check_in_memory_mime(in_memory_file):
    # because of I don't find how to populate mime type in form class
    # i have to get mime twice.
    # So i need to read from 0 point.
    in_memory_file.seek(0, 0)
    mime = magic.from_buffer(in_memory_file.read(1024), mime=True)
    return mime


def is_good_mimes(mime):
    mimes = ('video', 'image')
    for good_mime in mimes:
        if mime.startswith(good_mime):
            return True
    return False


def get_data_from_embed(embed_id):
    payload = constants.YOUTUBE_PAYLOAD_REQUEST.copy()
    payload.update({"id": embed_id})

    data = requests.get(constants.YOUTUBE_API_URL, payload)
    if not data.status_code == requests.codes.ok:
        return None

    try:
        data = data.json()
    except ValueError:
        return None

    try:
        return {
            'title': data['items'][0]['snippet']['title'],
            'content': data['items'][0]['snippet']['description'],
            'created': data['items'][0]['snippet']['publishedAt'],
            'embed_id': embed_id,
            'mime_type': 'embed'
        }
    except (IndexError, KeyError):
        return None
