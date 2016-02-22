from django.core.urlresolvers import reverse
from django.db import models


class ShareImage(models.Model):
    image = models.ImageField()
    body = models.TextField(blank=True)
    remote_addr = models.GenericIPAddressField(blank=True, null=True)
    published = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return u'%s' % self.image.title

    def get_absolute_url(self):
        return reverse('custom.views.share_image_detail', args=[str(self.pk)])
