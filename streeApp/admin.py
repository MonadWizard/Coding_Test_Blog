from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Posts, Tags

admin.site.register(Posts)

admin.site.register(Tags, MPTTModelAdmin)
