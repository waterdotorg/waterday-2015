from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('custom.views',
    url(r'^i/share-image/$', 'share_image', name='share_image'),
    url(r'^i/(?P<pk>\d+)/$', 'share_image_detail', name='share_image_detail'),
    url(r'^$', TemplateView.as_view(template_name='homepage.html'), name='homepage'),
)