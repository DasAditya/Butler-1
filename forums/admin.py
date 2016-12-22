from django.contrib import admin

# Register your models here.
from forums.models import Post,Topic

admin.site.register(Post)
admin.site.register(Topic)