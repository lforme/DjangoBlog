from django.contrib import admin
from .models import AboutmeInfo


class AboutmeAdmin(admin.ModelAdmin):
    list_display = ['text', 'weibo', 'github', 'twitter']

admin.site.register(AboutmeInfo, AboutmeAdmin)