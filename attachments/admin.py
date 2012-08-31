from django.contrib import admin
from attachments.models import Extension,Type,File
admin.site.register(Extension)
admin.site.register(Type)
admin.site.register(File)