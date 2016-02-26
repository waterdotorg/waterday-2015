from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from PIL import Image


class ShareImage(models.Model):
    image = models.ImageField(upload_to='share-image')
    body = models.TextField(blank=True)
    remote_addr = models.GenericIPAddressField(blank=True, null=True)
    published = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'Share Image %d' % self.pk

    def get_absolute_url(self):
        return reverse('custom.views.share_image_detail', args=[str(self.pk)])

    def image_admin_thumb(self):
        return u'<img width="240" height="200" src="%s" />' % self.image.url
    image_admin_thumb.short_description = 'Thumb'
    image_admin_thumb.allow_tags = True

    def image_overlay(self, word):
        size = (600, 500)
        crop_type = 'middle'

        img = Image.open(self.image)
        img_overlay_word = 'img/overlay/overlay-%s.png' % word
        img_overlay = Image.open(settings.STATIC_ROOT + img_overlay_word)

        img_ratio = img.size[0] / float(img.size[1])
        ratio = size[0] / float(size[1])

        if ratio > img_ratio:
            img = img.resize((size[0], int(round(size[0] * img.size[1] / img.size[0]))),
                    Image.ANTIALIAS)

            # Crop in the top, middle or bottom
            if crop_type == 'top':
                box = (0, 0, img.size[0], size[1])
            elif crop_type == 'middle':
                box = (0, int(round((img.size[1] - size[1]) / 2)), img.size[0],
                    int(round((img.size[1] + size[1]) / 2)))
            elif crop_type == 'bottom':
                box = (0, img.size[1] - size[1], img.size[0], img.size[1])
            img = img.crop(box)

        elif ratio < img_ratio:
            img = img.resize((int(round(size[1] * img.size[0] / img.size[1])), size[1]),
                    Image.ANTIALIAS)
            # Crop in the top, middle or bottom
            if crop_type == 'top':
                box = (0, 0, size[0], img.size[1])
            elif crop_type == 'middle':
                box = (int(round((img.size[0] - size[0]) / 2)), 0,
                    int(round((img.size[0] + size[0]) / 2)), img.size[1])
            elif crop_type == 'bottom':
                box = (img.size[0] - size[0], 0, img.size[0], img.size[1])
            img = img.crop(box)

        else:
            # If the scale is the same, we do not need to crop
            img = img.resize((size[0], size[1]), Image.ANTIALIAS)

        if img.mode != 'RGBA':
            img = img.convert('RGBA')

        img_out = Image.alpha_composite(img, img_overlay)
        img_out.save(self.image.path)
