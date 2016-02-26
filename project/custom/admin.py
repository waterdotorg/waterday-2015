from django.contrib import admin
from custom.models import ShareImage


class ShareImageAdmin(admin.ModelAdmin):
    list_display = ['image_admin_thumb', 'remote_addr', 'published',
                    'created_date']
    search_fields = ('remote_addr', 'body')
    ordering = ['-id']

admin.site.register(ShareImage, ShareImageAdmin)
