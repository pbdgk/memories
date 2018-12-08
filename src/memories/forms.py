from django import forms
from django.core.exceptions import ValidationError

from urllib.parse import urlparse, parse_qs

from . import utils, constants, models


class MemoryForm(forms.ModelForm):
    class Meta:
        model = models.Memory
        fields = ('title', 'content', 'media')

    def clean_media(self):
        media = self.cleaned_data.get('media', None)
        if media is not None:
            mime = utils.check_in_memory_mime(media)
            if not utils.is_good_mimes(mime):
                raise ValidationError(f"Such file type '{mime}'\
                                        is restricted for this app"
                                      )
        return media


class EmbedForm(forms.Form):
    embed_id = forms.CharField()

    def clean_embed_id(self):
        cleaned_embed_url = self.cleaned_data.get('embed_id')
        parsed_url = urlparse(cleaned_embed_url)
        if parsed_url.netloc != constants.YOUTUBE_DOMAIN\
           or parsed_url.path != constants.YOUTUBE_PATH:
            raise ValidationError('Domain must be {}{}'.format(
                constants.YOUTUBE_DOMAIN,
                constants.YOUTUBE_PATH)
                )
        query_set = parse_qs(parsed_url.query)
        embed_id = query_set.get('v')
        if embed_id is None:
            raise ValidationError('No post id')
        return embed_id[0]

    def save(self, embed_id, user):
        data = utils.get_data_from_embed(embed_id, user)
        memory = models.Memory.objects.create(**data)
        return memory
