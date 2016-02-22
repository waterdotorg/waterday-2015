from django import forms
from PIL import Image


class ShareImageForm(forms.Form):
    image = forms.ImageField()

    def clean_image(self):
        data = self.cleaned_data['image']
        im = Image.open(data)

        width, height = im.size
        if width < 600 or height < 500:
            raise forms.ValidationError("Minimum image width and height are "
                                        "600 x 500")

        try:
            im = im.convert("RGB")
        except:
            raise forms.ValidationError("Image mode not supported.")
