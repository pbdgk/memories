from django.http import Http404

import magic
import requests

from . import constants


def check_in_memory_mime(in_memory_file):
    # because of I don't find how to populate mime type in form class i have to get mime twice.
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


payload = {'key':'AIzaSyBjU9OWslGq1SuK9JM1XE4GMedSFXwml_k', 'part': 'snippet'}

def get_data_from_embed(embed_id, user):
    url = "https://www.googleapis.com/youtube/v3/videos"
    payload = {'key':'AIzaSyBjU9OWslGq1SuK9JM1XE4GMedSFXwml_k', 'part': 'snippet'}
    payload.update({"id": embed_id})
    data = requests.get(constants.YOUTUBE_API_URL, payload)
    data = data.json()
    try:
        title = data['items'][0]['snippet']['title']
        content = data['items'][0]['snippet']['description']
        created = data['items'][0]['snippet']['publishedAt']
    except (IndexError, KeyError) as e:
        raise Http404
    else:
        return {
            'author': user,
            'title': title,
            'content': content,
            'created': created,
            'embed_id': embed_id,
            'mime_type': 'embed'
        }