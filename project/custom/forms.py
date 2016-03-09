from django import forms
from django.conf import settings
from PIL import Image


class ShareImageForm(forms.Form):
    WORD_CHOICES = (
        ('', '2. WATER GIVES ME...'),
        ('joy', 'joy'),
        ('friendship', 'friendship'),
        ('life', 'life'),
        ('family', 'family'),
        ('nourishment', 'nourishment'),
        ('inspiration', 'inspiration'),
        ('strength', 'strength'),
    )
    image = forms.ImageField()
    word = forms.ChoiceField(choices=WORD_CHOICES)

    def clean_image(self):
        data = self.cleaned_data['image']
        im = Image.open(data)
        im_overlay = Image.open(settings.STATIC_ROOT + 'img/overlay/overlay-friendship.png')

        width, height = im.size
        if width < 300 or height < 250:
            raise forms.ValidationError("Minimum image width and height are "
                                        "600 x 500")

        if im.format not in ('JPEG', 'PNG', 'GIF'):
            raise forms.ValidationError("File type not supported. Please upload a JPG, PNG or GIF.")

        im = im.resize((600, 500))

        try:
            if im.mode != 'RGBA':
                im = im.convert('RGBA')
        except:
            raise forms.ValidationError("Image mode not supported.")

        try:
            im_out = Image.alpha_composite(im, im_overlay)
        except:
            raise forms.ValidationError("Sorry, this image is not compatible.")

        return data
